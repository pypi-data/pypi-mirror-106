import os.path

from clint.textui.progress import Bar as ProgressBar
from requests_toolbelt import MultipartEncoder, MultipartEncoderMonitor

from .exceptions import LoginException, UploadException

import requests


def undef_response_exp(r):
    raise Exception("Unhandled error. Contact the admins for help. Response code from server: {} \n Response from "
                    "server: {}".format(r.status_code, r.json()))


def login_to_server(username, password, server_url):
    """ Logs in to server and returns authorization token """
    login_url = "{}/maintainers/api/login/".format(server_url)
    r = requests.post(login_url, data={'username': username, 'password': password})

    if r.status_code == 200:
        data = r.json()
        return data['token']
    elif r.status_code == 400:
        if r.json()['error'] == "blank_username_or_password":
            raise LoginException("Username or password must not be blank.")
    elif r.status_code == 404:
        if r.json()['error'] == "invalid_credential":
            raise LoginException("Invalid credentials!")
    else:
        undef_response_exp(r)


def upload_to_server(build_file, checksum_file, server_url, token, use_chunked_upload=False):
    device_id = -1

    import os.path
    # Get codename from build_file
    build_file_name, _ = os.path.splitext(build_file)
    try:
        _, _, codename, _, _, _ = build_file_name.split('-')
    except ValueError:
        raise UploadException("The file name is mangled!")

    # Get device ID from server
    device_id_url = "{}/maintainers/api/device/id/".format(server_url)
    print("Fetching device ID for device {}...".format(codename))
    r = requests.get(device_id_url, headers={"Authorization": "Token {}".format(token)}, data={"codename": codename})

    if r.status_code == 200:
        device_id = r.json()['id']
    elif r.status_code == 400:
        if r.json()['error'] == "invalid_codename":
            raise UploadException("The device with the specified codename does not exist.")
    elif r.status_code == 401:
        if r.json()['error'] == "insufficient_permissions":
            raise UploadException("You are not authorized to upload with this device.")
    else:
        print("A problem occurred while querying the device ID.")
        undef_response_exp(r)

    print("Uploading build {}...".format(build_file))

    if use_chunked_upload:
        chunked_upload(server_url, device_id, build_file, checksum_file, token)
    else:
        direct_upload(server_url, device_id, build_file, checksum_file, token, codename)


def chunked_upload(server_url, device_id, build_file, checksum_file, token):
    device_upload_url = "{}/maintainers/api/device/{}/chunked_upload/".format(server_url, device_id)

    # Split file up into 100 KB segments
    chunk_size = 10000
    current_chunk = 0
    total_file_size = os.path.getsize(build_file)

    bar = ProgressBar(expected_size=total_file_size, filled_char='=')

    with open(build_file, 'rb') as build_file_raw:
        while chunk_data := build_file_raw.read(chunk_size):
            r = requests.put(device_upload_url, headers={
                "Authorization": "Token {}".format(token),
                "Content-Range": "bytes {}-{}/{}".format(current_chunk * chunk_size + 1,
                                                         current_chunk * chunk_size + len(chunk_data),
                                                         total_file_size)
            },
                             data={'file': chunk_data})

            if r.status_code == 200:
                if current_chunk == 0:
                    # Get new URL and expiry date
                    device_upload_url = r.json()['url']
                    print("Upload started. Expiry (upload before): {}\n".format(r.json()['expires']))
                bar.show((current_chunk + 1) * chunk_size)
            else:
                raise UploadException("Something went wrong during the upload. Exiting...")
        current_chunk += 1

    # Complete upload
    r = requests.post(device_upload_url, headers={"Authorization": "Token {}".format(token)},
                      data={'md5': get_md5_from_file(checksum_file)})

    if r.status_code == 200:
        print("Successfully uploaded the build {}!".format(build_file))
    else:
        raise UploadException("Something went wrong during upload finalization. Exiting...")


def get_md5_from_file(checksum_file):
    with open(checksum_file, 'r') as checksum_file_raw:
        line = checksum_file_raw.readline()
        values = line.split(" ")
        return values[0]


def direct_upload(server_url, device_id, build_file, checksum_file, token, codename):
    device_upload_url = "{}/maintainers/api/device/{}/upload/".format(server_url, device_id)

    e = MultipartEncoder(fields={
        'build_file': (build_file, open(build_file, 'rb'), 'text/plain'),
        'checksum_file': (checksum_file, open(checksum_file, 'rb'), 'text/plain'),
    })

    bar = ProgressBar(expected_size=e.len, filled_char='=')

    def callback(monitor):
        bar.show(monitor.bytes_read)

    m = MultipartEncoderMonitor(e, callback)

    r = requests.post(device_upload_url, headers={
        "Authorization": "Token {}".format(token),
        "Content-Type": e.content_type
    }, data=m)

    if r.status_code == 200:
        print("Successfully uploaded the build {}!".format(build_file))
    elif r.status_code == 400:
        if r.json()['error'] == "duplicate_build":
            raise UploadException("This build already exists in the system!")
        if r.json()['error'] == "missing_files":
            raise UploadException("One of the required fields are missing!")
        if r.json()['error'] == "file_name_mismatch":
            raise UploadException("The build file name does not match the checksum file name!")
        if r.json()['error'] == "invalid_file_name":
            raise UploadException("The file name was malformed!")
        if r.json()['error'] == "not_official":
            raise UploadException("The build is not official!")
        if r.json()['error'] == "codename_mismatch":
            raise UploadException("The codename does not match the build file name!")
    elif r.status_code == 401:
        if r.json()['error'] == "insufficient_permissions":
            raise UploadException("You are not allowed to upload for the device {}!".format(codename))
    elif r.status_code == 500:
        raise UploadException("An internal server error occurred. Contact the administrators for help.")
    else:
        print("A problem occurred while uploading your build.")
        undef_response_exp(r)
