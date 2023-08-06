# Copyright 2019 MISHMASH I O OOD
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import json
import uuid
import traceback
import time

import jwt
import requests
from Crypto.PublicKey import RSA


class MishmashWrongCredentialsException(Exception):
    pass


class MishmashUnauthorizedException(Exception):
    pass


class MishmashAuth():

    DEFAULT_CONFIG_FILE_PATHS = [

        "/etc/mishmashio/client.json",
        "/etc/mishmashio/client-python.json",
        "~/.mishmashio/client.json",
        "~/.mishmashio/client-python.json",
        "./client.json",
        "./client-python.json"
    ]

    VALID_TIME = 30  # valid time for signed token in seconds

    def __init__(self, config_file_path=None):

        config_data = self.get_config(config_file_path)

        if not config_data:
            raise MishmashWrongCredentialsException

        self.__auth_app_id = config_data["MISHMASHIO_APP_ID"]
        self.__auth_server_url = config_data["MISHMASHIO_AUTH_SERVER"]
        self.__auth_server_url_token = config_data["MISHMASHIO_AUTH_SERVER"] + \
            "/protocol/openid-connect/token"
        self.__auth_private_key_string = config_data["MISHMASHIO_AUTH_PRIVATE_KEY"]

        self.__access_token = None

    def config_file_paths(self, config_file_path):

        config_file_paths = []
        if isinstance(config_file_path, str):
            self.config_file_paths.append(config_file_path)

        config_file_paths += self.DEFAULT_CONFIG_FILE_PATHS

        return config_file_paths

    def get_config(self, config_file_path):

        config = self.get_config_from_env()

        if not config:
            config = self.get_config_from_file(config_file_path)

        return config

    def get_config_from_file(self, config_file_path):

        config_file_paths = self.config_file_paths(config_file_path)

        for file_path in config_file_paths:
            try:
                with open(file_path, "r") as f:
                    return json.load(f)

            except FileNotFoundError:
                pass

        return None

    def get_config_from_env(self):

        config = {
            "MISHMASHIO_APP_ID": os.environ.get("MISHMASHIO_APP_ID", None),
            "MISHMASHIO_AUTH_PRIVATE_KEY": os.environ.get("MISHMASHIO_AUTH_PRIVATE_KEY", None),
            "MISHMASHIO_AUTH_SERVER": os.environ.get("MISHMASHIO_AUTH_SERVER", None),
        }

        for k, v in config.items():
            if v is None:
                return None

        return config

    def add_pem_headers_to_private_key(self, key_without_pem_headers):

        pem_key = "-----BEGIN RSA PRIVATE KEY-----\n"
        pem_key += key_without_pem_headers
        pem_key += "\n-----END RSA PRIVATE KEY-----"
        return pem_key

    def get_or_create_access_token(self):

        if self.__access_token is None:
            self.__access_token = self.generate_new_access_token()
            return self.__access_token

        try:
            jwt.decode(self.__access_token, options={
                       "verify_signature": False})
        except jwt.ExpiredSignatureError:
            self.__access_token = self.generate_new_access_token()

        return self.__access_token

    def sign_token(self):

        iat = time.time()
        exp = iat + self.VALID_TIME

        payload = {
            "exp": exp,
            "iat": iat,
            "iss": self.__auth_app_id,
            "sub": self.__auth_app_id,
            "aud": self.__auth_server_url,
            "jti": str(uuid.uuid4()),
            "uid": self.__auth_app_id
        }

        private_key = RSA.importKey(
            self.add_pem_headers_to_private_key(self.__auth_private_key_string))

        token = jwt.encode(payload,
                           private_key.exportKey('PEM'),
                           algorithm='RS256')

        return token

    def generate_new_access_token(self):

        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = {
            "client_id": self.__auth_app_id,
            "scope": "openid",
            "grant_type": "client_credentials",
            "client_assertion_type": 'urn:ietf:params:oauth:client-assertion-type:jwt-bearer',
            "client_assertion": self.sign_token()
        }

        try:
            response = requests.post(self.__auth_server_url_token,
                                     data=data, headers=headers).json()
        except Exception as e:
            traceback.print_tb(e.__traceback__, e.args)
            return None

        if "error" in response:
            raise MishmashWrongCredentialsException(
                f"error: {response['error_description']}")
        else:
            return response.get("access_token", None)

    @property
    def authorization_header(self):

        access_token = self.get_or_create_access_token()
        if not access_token:
            raise MishmashUnauthorizedException
        return f"Bearer {access_token}"

    @property
    def access_token(self):

        access_token = self.get_or_create_access_token()
        if not access_token:
            raise MishmashUnauthorizedException
        return access_token

    @property
    def app_id(self):
        return self.__auth_app_id
