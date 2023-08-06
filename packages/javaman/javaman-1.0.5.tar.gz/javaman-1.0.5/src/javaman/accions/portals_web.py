from javaman import JManCon


class PortalsWeb:
    url = '/portals_web/{num_portal}'

    def __init__(self, con: JManCon):
        self._con = con

    def get_portal_web(self, portal_web_id: int):
        tmp_url = PortalsWeb.url.format(num_portal=portal_web_id)
        req = self._con.get(url=tmp_url)
        return req.json()
