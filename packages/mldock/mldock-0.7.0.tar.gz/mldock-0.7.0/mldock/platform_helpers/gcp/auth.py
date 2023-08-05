"""
    GCP Auth utilities
"""
import os
from google.auth import default
from google.auth.transport.requests import Request

from mldock.platform_helpers.utils import strip_scheme

# def get_sdk_credentials_volume_mount(host_path='~/.config/gcloud'):
#     """
#         configures a volume mount for providing provider resource
#         permissions.
#     """
#     host_volume = Path(os.path.expanduser(host_path)).absolute().as_posix()
#     container_path = '/root/.config/gcloud'
#     container_volume = {'bind': container_path, 'mode': 'rw'}
#     return host_volume, container_volume

def get_gcp_gcr(region: str):
    """
        Get Authentication credentials for google.auth

        args:
            region (str): Region to Authenticate GCR registry in
        
        return:
            username (str): username to use in docker client auth
            password (str): password token to use in docker client auth
            registry (str): registry url to use
    """
    credentials, project = default(
        scopes=['https://www.googleapis.com/auth/cloud-platform']
    )
    # creds.valid is False, and creds.token is None
    # Need to refresh credentials to populate those
    auth_req = Request()
    credentials.refresh(auth_req)
    # set docker creds
    username = 'oauth2accesstoken'
    password = credentials.token
    if region == 'eu':
        registry = 'https://eu.gcr.io'
    elif region == 'us':
        registry = 'https://us.gcr.io'
    elif region == 'asia':
        registry = 'https://asia.gcr.io'
    else:
        registry = 'https://gcr.io'

    registry = os.path.join(registry, project)
    # return docker credentials
    cloud_repository = strip_scheme(registry)
    # return docker credentials
    return username, password, registry, cloud_repository
