from javaman import JManCon


class Comandes:
    url = '/portals_web/{numcom}/comanda'
    url_pendent_servir = '/comandes/{id_com}/pendent_servir'
    url_bloqueig = '/comandes/{id_com}/magatzem_retingut'
    url_comencar = '/comandes/{id_com}/iniciar'
    url_cancelar = '/comandes/{id_com}/cancelar'
    url_albarans = '/comandes/{id_com}/albarans'

    def __init__(self, con: JManCon):
        self._con = con

    def crear(self, portal_web_token: str, comanda: dict):
        tmp_url = Comandes.url.format(numcom=portal_web_token)
        req = self._con.post(url=tmp_url, data=comanda)
        return req.json()

    def bloquejar(self, comanda_id: int):
        req = self._con.post(url=Comandes.url_bloqueig.format(id_com=comanda_id), data=None)
        return req.json()

    def pendent_servir(self, comanda_id: int):
        req = self._con.post(url=Comandes.url_pendent_servir.format(id_com=comanda_id), data=None)
        return req.json()

    def comencar(self, comanda_id: int):
        req = self._con.post(url=Comandes.url_comencar.format(id_com=comanda_id), data=None)
        return req.json()

    def albarans(self, comanda_id: int):
        req = self._con.get(url=Comandes.url_albarans.format(id_com=comanda_id))
        return req.json()

    def assignar_usuari(self, comanda_id: int, emplat_id: int):
        req = self._con.post(url='/comandes/' + str(comanda_id) + '/assignar', data={'id': emplat_id})
        return req.json()

    def pausar(self, comanda_id: int):
        req = self._con.post(url='/comandes/' + str(comanda_id) + '/pausar', data=None)
        return req.json()

    def cancelar_albara(self, albara_id: int):
        req = self._con.get(url=Comandes.url_cancelar.format(id_com=albara_id))
        return req.json()
