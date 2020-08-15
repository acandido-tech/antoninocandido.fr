from django.templatetags.static import static

ASSETS_CONFIG = {
    "Home": {
        "js_list": [
            "https://cdnjs.cloudflare.com/ajax/libs/jquery-easing/1.4.1/jquery.easing.min.js",
            static("webapp/js/external/jquery.color.js"),
            static("webapp/js/galerie.js"),
            static("webapp/js/home.js"),
        ],
        "css_list": [],
    },
    "Portfolio": {
        "js_list": [
            "https://cdnjs.cloudflare.com/ajax/libs/jquery-easing/1.4.1/jquery.easing.min.js",
            "https://cdnjs.cloudflare.com/ajax/libs/coin-slider/1.0.0/coin-slider.min.js",
            static("webapp/js/external/jquery.scrollTo.js"),
            static("webapp/js/effect.js"),
        ],
        "css_list": [],
    },
    "About": {"js_list": [], "css_list": []},
    "Contact": {
        "js_list": [
            "https://cdnjs.cloudflare.com/ajax/libs/jquery-easing/1.4.1/jquery.easing.min.js",
            "http://maps.google.com/maps/api/js?sensor=false",
            static("webapp/js/effect.js"),
        ],
        "css_list": [],
    },
}

PROJECTS_CONFIG = {
    "apero": {
        "client_info_list": [
            "<b>IUT SRC de Saint-Raphaël</b>",
            "| Contrat : <b>Alternance</b>",
            "| Diplôme : <b>DUT SRC</b>",
            "| Date : <b>2009</b>",
        ],
        "project_img_path": "projets/galerie/projet-11/logo-apero.png",
        "project_details": [
            'Maquette de site internet pour le projet "l\'apero.net".',
            "Il s'agit d'un projet de site internet réalisé dans le cadre de mon DUT SRC.",
            "Projet actuellement en Stand-by.",
        ],
        "project_app": ["Photoshop CS4", "Illustrator CS4"],
        "project_galerie": [
            {
                "path": "projets/galerie/projet-11/lapero-1.jpg",
                "alt": "l'apéro.net - 1",
            },
            {
                "path": "projets/galerie/projet-11/lapero-2.jpg",
                "alt": "l'apéro.net - 2",
            },
        ],
    },
}
