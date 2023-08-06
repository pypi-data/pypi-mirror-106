from .accions.clients import Clients
from .accions.pobles import Pobles
from .accions.portals_web import PortalsWeb
from .accions.regularitzacions import Regularitzacions
from .accions.usuaris import Usuaris
from .accions.comandes import Comandes
from .accions.articles import Articles
from .accions.wms import Wms
from .connexio import JManCon
import config


class JMan:

    def __init__(self):
        self._con = JManCon()

    @property
    def config(self) -> config.Manager:
        return self._con.config

    @property
    def clients(self):
        return Clients(con=self._con)

    @property
    def articles(self):
        return Articles(con=self._con)

    @property
    def usuaris(self):
        return Usuaris(con=self._con)

    @property
    def pobles(self):
        return Pobles(con=self._con)

    @property
    def comandes(self):
        return Comandes(con=self._con)

    @property
    def regularitzacions(self):
        return Regularitzacions(con=self._con)

    @property
    def portals_web(self):
        return PortalsWeb(con=self._con)

    @property
    def wms(self):
        return Wms(con=self._con)
