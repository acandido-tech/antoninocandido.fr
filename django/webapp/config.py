from django.templatetags.static import static

CONFIG = {
    "Home": {
        "js_list": [
            "https://cdnjs.cloudflare.com/ajax/libs/jquery-easing/1.4.1/jquery.easing.min.js",
            static("webapp/js/jquery.color.js"),
            static("webapp/js/galerie.js"),
            static("webapp/js/scripts.js"),
        ],
        "css_list": [],
    },
    "Portfolio": {
        "js_list": [
            "https://cdnjs.cloudflare.com/ajax/libs/jquery-easing/1.4.1/jquery.easing.min.js",
            "https://cdnjs.cloudflare.com/ajax/libs/coin-slider/1.0.0/coin-slider.min.js",
            static("webapp/js/jquery.scrollTo.js"),
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
