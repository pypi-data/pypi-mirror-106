import requests
import json
from libs.errors import Errors
import config


class JManCon:
    __slots__ = '_usuari_token'

    def __init__(self):
        data = {
            "user_login": config.Manager.usuari_manager(),
            "user_password": config.Manager.password_manager(),
            "instancia_guid": config.Manager.instancia_guid(),
            "empresa_guid": config.Manager.empresa_guid()
        }
        headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json'
        }
        req = requests.post(url=config.Manager.url() + '/login/usuari', headers=headers, data=json.dumps(data))
        if req.status_code not in [200, 201]:
            raise Errors.Unauthorized()
        self._usuari_token = req.json()['token']

    @property
    def config(self) -> config.Manager:
        return config.Manager()

    @property
    def usuari_token(self) -> str:
        return self._usuari_token

    def post(self, url: str, data: [list, dict, None]) -> requests:
        headers = {
            'Accept': 'application/json',
            'authorization': "Bearer " + self.usuari_token
        }
        if data is not None:
            headers['Content-type'] = 'application/json'
        if data is not None:
            data = json.dumps(data)
        try:
            req = requests.post(url=self.config.url() + url, headers=headers, data=data)
        except requests.exceptions.RequestException:
            raise Errors.AppError('error connexio manager')
        if req.status_code < 200 or req.status_code >= 300:
            raise Errors.AppError('Manager error. status: ' + str(req.status_code))
        return req

    def put(self, url: str, data: [list, dict, None]) -> requests:
        headers = {
            'Accept': 'application/json',
            'authorization': "Bearer " + self.usuari_token
        }
        if data is not None:
            headers['Content-type'] = 'application/json'
        if data is not None:
            data = json.dumps(data)
        try:
            req = requests.put(url=self.config.url() + url, headers=headers, data=data)
        except requests.exceptions.RequestException:
            raise Errors.AppError('error connexio manager')
        if req.status_code < 200 or req.status_code >= 300:
            raise Errors.AppError('Manager error. status: ' + str(req.status_code))
        return req

    def get(self, url: str) -> requests:
        headers = {
            'Accept': 'application/json',
            'authorization': "Bearer " + self.usuari_token
        }
        try:
            req = requests.get(url=self.config.url() + url, headers=headers)
        except requests.exceptions.RequestException:
            raise Errors.AppError('error connexio manager')
        if req.status_code < 200 or req.status_code >= 300:
            raise Errors.AppError('Manager error. status: ' + str(req.status_code))
        return req

    def delete(self, url: str) -> requests:
        headers = {'authorization': "Bearer " + self.usuari_token}
        try:
            req = requests.delete(url=self.config.url() + url, headers=headers)
        except requests.exceptions.RequestException:
            raise Errors.AppError('error connexio manager')
        if req.status_code < 200 or req.status_code >= 300:
            raise Errors.AppError('Manager error. status: ' + str(req.status_code))
        return

    def __del__(self):
        self.delete(url='/logout')
