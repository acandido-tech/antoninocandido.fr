from .base import BaseView


class PortfolioView(BaseView):
    template_name = "webapp/portfolio.html"
    view_name = "Portfolio"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.build_portfolio_data())
        return context

    def build_portfolio_data(self):
        """ Build data to manage portfolio view"""
        # todo replace by database calls
        return {
            "project_menu": [
                {"rel": "sites", "label": "Sites Internet"},
                {"rel": "webdesigns", "label": "Webdesign"},
                {"rel": "flash", "label": "Flash AS2 / AS3"},
                {"rel": "videos-3d", "label": "3D et Vidéo"},
            ],
            "project_list": [
                {
                    "name": "edition-limitee",
                    "title": "EDITION-LIMITEE",
                    "sub_title": "Site E-commerce",
                    "type": "sites",
                    "img_hash": {
                        "path": "clients/edition-limitee.jpg",
                        "alt": "vignette edition limitee",
                    },
                },
                {
                    "name": "ferme-des-sonnailles",
                    "title": "Ferme des Sonnailles",
                    "sub_title": "Site Vitrine",
                    "type": "sites",
                    "img_hash": {
                        "path": "clients/sonnailles.jpg",
                        "alt": "vignette ferme des sonnailles",
                    },
                },
                {
                    "name": "domaine-saint-andree",
                    "title": "Domaine des Sonnailles",
                    "sub_title": "Site Vitrine",
                    "type": "sites",
                    "img_hash": {
                        "path": "clients/domaine-saint-andre.jpg",
                        "alt": "vignette domaine saint andre",
                    },
                },
                {
                    "name": "internet-cmwa",
                    "title": "Internet-cmwa",
                    "sub_title": "Site Vitrine",
                    "type": "sites",
                    "img_hash": {
                        "path": "clients/internet-cmwa.jpg",
                        "alt": "vignette internet cmwa",
                    },
                },
                {
                    "name": "menuiserie-candido",
                    "title": "Menuiserie Candido",
                    "sub_title": "Site Vitrine",
                    "type": "sites",
                    "img_hash": {
                        "path": "clients/menuiserie-candido.jpg",
                        "alt": "vignette menuiserie candido",
                    },
                },
                {
                    "name": "intranet-ft",
                    "title": "France Télécom",
                    "sub_title": "Intranet",
                    "type": "sites",
                    "img_hash": {
                        "path": "clients/orange.jpg",
                        "alt": "vignette france télécom",
                    },
                },
                {
                    "name": "credit-agricole",
                    "title": "Crédit Agricole",
                    "sub_title": "Webdesign",
                    "type": "webdesigns",
                    "img_hash": {
                        "path": "clients/credit-agricole.jpg",
                        "alt": "vignette crédit agricole",
                    },
                },
            ],
        }

    """

                <li class="item" rel="webdesigns">
                    <div class="info_cache 7" id="bnp-paribas-web">
                        <p>
                            <span>BNP PARIBAS CARDIF</span>
                            <br />Divers Webdesign
                        </p>
                    </div>
                    <img src="{% static 'webapp/assets/img/clients/bnp-paribas-web.jpg' %}"
                        alt="vignette BNP Paribas web" />
                </li>

                <li class="item" rel="webdesigns">
                    <div class="info_cache 8" id="intranet-gap">
                        <p>
                            <span>Mairie de Gap</span>
                            <br />Intranet
                        </p>
                    </div>
                    <img src="{% static 'webapp/assets/img/clients/intranet-gap.jpg' %}"
                        alt="vignette mairie de Gap" />
                </li>

                <li class="item" rel="webdesigns">
                    <div class="info_cache 9" id="cnad">
                        <p>
                            <span>Chez-soi Services</span>
                            <br />Webdesign
                        </p>
                    </div>
                    <img src="{% static 'webapp/assets/img/clients/cnad.jpg' %}" alt="vignette CNAD" />
                </li>

                <li class="item" rel="webdesigns">
                    <div class="info_cache 10" id="apero">
                        <p>
                            <span>L'Apero.net</span>
                            <br />Webdesign
                        </p>
                    </div>
                    <img src="{% static 'webapp/assets/img/clients/lapero-net.jpg' %}" alt="vignette lapero.net" />
                </li>

                <li class="item" rel="flash">
                    <div class="info_cache 11" id="etsi">
                        <p>
                            <span>ETSI</span>
                            <br />Flash
                        </p>
                    </div>
                    <img src="{% static 'webapp/assets/img/clients/etsi.jpg' %}" alt="vignette ETSI" />
                </li>

                <li class="item" rel="flash">
                    <div class="info_cache 12" id="bnp-senegal">
                        <p>
                            <span>BNP Paribas - Sénégal</span>
                            <br />Flash
                        </p>
                    </div>
                    <img src="{% static 'webapp/assets/img/clients/bnp-senegal.jpg' %}"
                        alt="vignette BNP Paribas - senegal" />
                </li>

                <li class="item" rel="flash">
                    <div class="info_cache 13" id="bnp-carte-france">
                        <p class="autre_2">
                            <span>BNP Paribas<br />Carte de France</span>
                            <br />Flash
                        </p>
                    </div>
                    <img src="{% static 'webapp/assets/img/clients/bnp-carte-france.jpg' %}"
                        alt="vignette BNP Paribas - carte de France" />
                </li>

                <li class="item" rel="flash">
                    <div class="info_cache 14" id="bnp-banniere">
                        <p>
                            <span>BNP Paribas</span>
                            <br />Bannières Flash
                        </p>
                    </div>
                    <img src="{% static 'webapp/assets/img/clients/bnp-mix.jpg' %}"
                        alt="vignette BNP Paribas - bannières" />
                </li>

                <li class="item" rel="videos-3d">
                    <div class="info_cache 15" id="bnp-paribas-video">
                        <p>
                            <span>BNP Paribas</span>
                            <br />Vidéos
                        </p>
                    </div>
                    <img src="{% static 'webapp/assets/img/clients/bnp-paribas-video.jpg' %}"
                        alt="vignette BNP Paribas - vidéos" />
                </li>

                <li class="item" rel="videos-3d">
                    <div class="info_cache 16" id="domaine-3d">
                        <p>
                            <span>Domaine Saint-André/span>
                                <br />Modélisation 3D
                        </p>
                    </div>
                    <img src="{% static 'webapp/assets/img/clients/domaine-saint-andre-3d.jpg' %}"
                        alt="vignette 3D domaine saint andre" />
                </li>
    """
