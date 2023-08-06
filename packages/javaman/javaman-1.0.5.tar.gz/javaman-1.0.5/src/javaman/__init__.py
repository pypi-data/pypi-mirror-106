__all__ = ['JMan', 'JManFb', 'JManError', 'JManCon']

import fdb
import json
import requests
from . import fb_consultes
from . import accions
from .errors import *


class ConfigJavaman:

    __slots__ = '_config'
    
    def __init__(self, config_data: dict):
        self._config = config_data

    def url(self):
        return self._config["url"]

    def instancia_guid(self):
        return self._config["instancia_guid"]

    def empresa_guid(self):
        return self._config["empresa_guid"]

    def usuari_manager(self):
        return self._config["usuari_manager"]

    def password_manager(self):
        return self._config["password_manager"]

    def maquina_manager(self):
        return self._config["maquina_manager"]

    def portal_web_order(self):
        return self._config["portal_web_order"]

    def portal_web_store(self):
        return self._config["portal_web_store"]

    def erp_id(self):
        return self._config["erp_manager_id"]

    def magatzem_silo_id(self):
        return self._config["magatzem_silo_id"]

    def magatzem_gdis_id(self):
        return self._config["magatzem_gdis_id"]

    def magatzem_santa_llogaia_id(self):
        return self._config["magatzem_santa_llogaia_id"]

    def magatzem_botiga_id(self):
        return self._config["magatzem_botiga_id"]

    def magatzem_envasat_id(self):
        return self._config["magatzem_envasat_id"]

    def tipus_unitat_logistica_id_palet(self):
        return self._config["unitat_logistica_tipus_palet_id"]

    def tipus_unitat_logistica_id_caixa(self):
        return self._config["unitat_logistica_tipus_caixa_id"]


class JManCon:
    __slots__ = '_usuari_token', '_config'

    def __init__(self, config_data: dict):
        self._config = ConfigJavaman(config_data=config_data)
        data = {
            "user_login": self._config.usuari_manager(),
            "user_password": self._config.password_manager(),
            "instancia_guid": self._config.instancia_guid(),
            "empresa_guid": self._config.empresa_guid()
        }
        headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json'
        }
        req = requests.post(url=self._config.url() + '/login/usuari', headers=headers, data=json.dumps(data))
        if req.status_code not in [200, 201]:
            raise JManErrorUnauthorized()
        self._usuari_token = req.json()['token']

    @property
    def config(self) -> ConfigJavaman:
        return self._config

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
            req = requests.post(url=self._config.url() + url, headers=headers, data=data)
        except requests.exceptions.RequestException:
            raise JManErrorConnection()
        if req.status_code < 200:
            raise JManErrorConnection()
        if req.status_code < 200 or 200 < req.status_code <= 300 or req.status_code >= 500:
            raise JManErrorApp()
        if 400 <= req.status_code < 500:
            raise JManErrorClient()
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
            req = requests.put(url=self._config.url() + url, headers=headers, data=data)
        except requests.exceptions.RequestException:
            raise JManErrorConnection()
        if req.status_code < 200:
            raise JManErrorConnection()
        if req.status_code < 200 or 200 < req.status_code <= 300 or req.status_code >= 500:
            raise JManErrorApp()
        if 400 <= req.status_code < 500:
            raise JManErrorClient()
        return req

    def get(self, url: str) -> requests:
        headers = {
            'Accept': 'application/json',
            'authorization': "Bearer " + self.usuari_token
        }
        try:
            req = requests.get(url=self._config.url() + url, headers=headers)
        except requests.exceptions.RequestException:
            raise JManErrorConnection()
        if req.status_code < 200:
            raise JManErrorConnection()
        if req.status_code < 200 or 200 < req.status_code <= 300 or req.status_code >= 500:
            raise JManErrorApp()
        if 400 <= req.status_code < 500:
            raise JManErrorClient()
        return req

    def delete(self, url: str) -> requests:
        headers = {'authorization': "Bearer " + self.usuari_token}
        try:
            req = requests.delete(url=self._config.url() + url, headers=headers)
        except requests.exceptions.RequestException:
            raise JManErrorConnection()
        if req.status_code < 200:
            raise JManErrorConnection()
        if req.status_code < 200 or 200 < req.status_code <= 300 or req.status_code >= 500:
            raise JManErrorApp()
        if 400 <= req.status_code < 500:
            raise JManErrorClient()
        return req

    def __del__(self):
        self.delete(url='/logout')


class JMan:

    __slots__ = '_con'

    def __init__(self, config_data: dict):
        self._con = JManCon(config_data=config_data)

    @property
    def config(self) -> ConfigJavaman:
        return self._con.config

    @property
    def clients(self):
        return accions.Clients(con=self._con)

    @property
    def articles(self):
        return accions.Articles(con=self._con)

    @property
    def usuaris(self):
        return accions.Usuaris(con=self._con)

    @property
    def pobles(self):
        return accions.Pobles(con=self._con)

    @property
    def comandes(self):
        return accions.Comandes(con=self._con)

    @property
    def regularitzacions(self):
        return accions.Regularitzacions(con=self._con)

    @property
    def portals_web(self):
        return accions.PortalsWeb(con=self._con)

    @property
    def wms(self):
        return accions.Wms(con=self._con)


class JManFb:
    __slots__ = '_con'

    def __init__(self, config_data: dict):
        self._con = fdb.connect(
            user=config_data["user"],
            password=config_data["password"],
            host=config_data["host"],
            port=config_data["port"],
            database=config_data["database"],
            charset=config_data["charset"],
        )

    def select(self, sql: str, args: tuple = None) -> list:
        cur = self._con.cursor()
        cur.execute(operation=sql, parameters=args)
        res = cur.fetchall()
        cur.close()
        return res

    def c_sync_clients(self):
        return self.select(sql=fb_consultes.sync_clients)

    def c_sync_productes(self):
        return self.select(sql=fb_consultes.sync_productes)

    def c_sync_transportistes(self):
        return self.select(sql=fb_consultes.sync_transportistes)

    def c_sync_comandes_pendents(self):
        return self.select(sql=fb_consultes.sync_comandes_pendents)

    def c_sync_comanda(self, comanda_id: int):
        return self.select(sql=fb_consultes.sync_comanda, args=(comanda_id,))[0]

    def c_sync_comanda_linies(self, comanda_id: int):
        return self.select(sql=fb_consultes.sync_comanda_linies, args=(comanda_id,))
