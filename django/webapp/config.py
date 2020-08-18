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
            static("webapp/js/portfolio.js"),
        ],
        "css_list": [],
    },
    "About": {"js_list": [static("webapp/js/about.js"),], "css_list": []},
    "Contact": {
        "js_list": [
            "https://cdnjs.cloudflare.com/ajax/libs/jquery-easing/1.4.1/jquery.easing.min.js",
            "http://maps.google.com/maps/api/js?sensor=false",
            static("webapp/js/contact.js"),
        ],
        "css_list": [],
    },
}

PROJECT_USED_KEY = "used"
PROJECT_MADE_KEY = "made"
