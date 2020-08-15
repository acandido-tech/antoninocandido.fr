var couleur = '';

$(document).ready(function () {
	$('.item li div.info_cache').css("opacity", 0);
	function reset_thumbs() {
		$('div.info_cache').removeClass('current');
		$('div.info_cache').css({ 'opacity': '0', 'cursor': 'pointer' });
	}

	var galeriePos = new Array;
	var nbr_images = new Array;
	galeriePos[0] = new Array();
	nbr_images[0] = new Array();

	$.each($('ul.item img'), function (i, item) {
		nbr_images[0][i] = $(item).attr('src');
	});

	var idprojet, substr, num_projet;
	var vignettes = $('div.info_cache');

	$(vignettes).stop().bind('click', function (e) {
		e.preventDefault();
		displayProject(this);
	});

	/**
	 * 
	 * @param {*} event 
	 */
	function displayProject(event) {

		$(vignettes).css({ 'opacity': '0', 'cursor': 'pointer' });
		$(event).css({ 'opacity': '0.9', 'cursor': 'default' });


		//on récupère la valeur de la propriété id
		idprojet = $(event).attr("id");
		num_projet = $(event).attr("class");
		substr = num_projet.split(' ');
		galeriePos[0] = substr[1];


		// j'arrete la fonction si le projet de la vignette cliqué est déjà ouvert
		if ($(event).is('.current')) {
			return false;
		}

		//je teste si la div qui affiche le contenu d'un projet n'est pas déjà ouvert et j'effectue une animation differente
		if ($('.cont1').is('.open')) {

			$(vignettes).removeClass('current');
			$(event).addClass('current');

			$('#contenu-client').animate({ opacity: 0 }, 500, function () {
				recup_projet(idprojet, 0, galeriePos[0]);
			});
			return false;
		}

		//sinon j'effectue les animations qui affichent le projet choisi dans les vignettes
		$(vignettes).removeClass('current');
		$(event).addClass('current');
		$.scrollTo('body', 800, {});
		$('.cont1').slideUp("slow", function () {
			$('.cont2').slideDown("slow");
			recup_projet(idprojet, 0, galeriePos[0]);
		});
		$(event).addClass('current');
		$('.cont1').addClass('open');
		return false;
	}

	//function qui récupère l'id de la vignette cliqu� et charge son contenu dans la div cach� 
	function recup_projet(id, etat, num_projet) {
		couleur = couleur_fond(num_projet);
		$('.pxs_container_projekt').css("background", "none");
		$('.pxs_container_projekt').css("background-color", couleur);
		$('#pxs_container').append('<div class="pxs_loading" id="portfolio">Chargement...</div>');
		$('.pxs_loading').fadeIn(540);
		if ($('.action_js_galerie')) { $('#action_js_galerie').remove(); }
		if (etat == '1') {
			$('#contenu-client').animate({ opacity: 0 }, 800, function () {
				$('#contenu-client').css({ 'display': 'none' });
				load_project(id);
			});
			return false;
		}

		$('#contenu-client').css({ 'opacity': '0', 'display': 'none' });
		$.scrollTo('body', 800, {});
		$('#thumb-portfolio,.footer').fadeOut("slow", function () {
			load_project(id);
		});
		return false;
	};

	$.changeprojet = function (direction) {

		reset_thumbs();
		if (direction == 'prev')
			galeriePos[0]--;
		else
			galeriePos[0]++;
		if (galeriePos[0] == nbr_images[0].length) { galeriePos[0] = 0; }
		if (galeriePos[0] == -1) { galeriePos[0] = nbr_images[0].length - 1; }
		//idprojet = $(nbr_images[0][galeriePos[0]]).attr("id");
		idprojet = $('div.' + galeriePos[0]).attr("id");
		$('div#' + idprojet).addClass('current');
		$('div#' + idprojet).css({ 'opacity': '0.9', 'cursor': 'default' });
		recup_projet(idprojet, 1, galeriePos[0]);
	};

	/**
	 * Load project into container
	 * 
	 * @param {*} project_id 
	 */
	function load_project(project_id) {
		$('#contenu-client').hide().load('projects/' + project_id.replace(/\/?#/, ""), function () {
			if ($('#contenu-client').find("img").length > 0) {
				var img_projet = $('#pxs_container img'),
					nbr_img_projet = img_projet.length
					;

				img_projet.load(function () {
					nbr_img_projet--;
					if (nbr_img_projet == 0) {
						$('.pxs_loading').fadeOut(540, function () {
							$('.pxs_container_projekt').css("background", couleur + " url(" + image_path + "/projets/background/" + project_id + ".jpg) no-repeat top center");
							$('#contenu-client').css({ 'display': 'block' });
							$('.pxs_loading').remove();
							$('<div class="action_js_galerie"><script type="text/javascript" src="' + js_path + '/galerie-client.js"></script></div>').insertAfter($('div#contenu-client .contenair-client'));
							$('#contenu-client').animate({ opacity: 1 }, 940);
							$('#thumb-portfolio,.footer').fadeIn("slow");
						});
					}

				});
			}
		});

	}

	function getAbsolutePath() {
		var currentURL = window.location.toString().split("/");
		return currentURL[currentURL.length - 1].split("?");
	}

	var projetURL = getAbsolutePath();
	if (projetURL[1]) {
		$('#' + projetURL[1]).click();
	}

	//SCRIPT ANIMATION VIGNETTE PORTFOLIO
	$('.menu li a').stop().click(function (e) {
		e.preventDefault();
		$('.menu li').removeClass('selected');
		$(this).parent('li').addClass('selected');
		thisItem = $(this).attr('rel');
		if (thisItem != "all") {
			$('.item li[rel=' + thisItem + ']').stop()
				.animate({ 'width': '220px', 'opacity': 1 }, 1500);
			$("#thumb-portfolio").stop().animate({ height: "600px" }, 1500);

			$('.item li[rel!=' + thisItem + ']').stop()
				.animate({ 'width': 0, 'opacity': 0 }, 1500, function () {
				});
		}
		else {
			$('.item li').stop()
				.animate({ 'opacity': 1, 'width': '220px' }, 1500);
			$("#thumb-portfolio").stop().animate({ height: "1100px" }, 1500);
		}
	});

	$('.item li div.info_cache').hover(function () {
		if (!$(this).is('.current')) {
			$(this).stop().fadeTo("fast", 0.9);
		}
	}, function () {
		if (!$(this).is('.current')) {
			$(this).stop().fadeTo("fast", 0);
		}
	});
});

function couleur_fond(id) {
	var couleurs_fond = ["#a6a6a7", "#68b2e2", "#acba91", "#afc5ce", "#c8c9ca", "#c8c9ca", "#81cdef", "#a8c1ba", "#c8c9ca", "#c8c9ca", "#c8c9ca", "#c8c9ca", "#a8c1ba", "#a8c1ba", "#a8c1ba", "#a8c1ba", "#c8c9ca"];
	return couleurs_fond[id];
}

/*
 CODE GOOGLE MAP
*/
function initialiser() {

	var styleArray = [
		{
			featureType: "road",
			stylers: [{ hue: "#242831" }, { lightness: 10 }, { saturation: -95 }, { visibility: "simplified" }]
		}, {
		},
		{
			featureType: "poi",
			stylers: [{ hue: "#91ff00" }, { visibility: "on" }, { saturation: -45 }]
		}, {
		},
		{
			featureType: "landscape",
			stylers: [{ hue: "#242831" }, { lightness: 10 }, { saturation: -95 }, { visibility: "simplified" }]
		}, {
		},
		{
			elementType: "labels",
			stylers: [{ hue: "#242831" }, { lightness: 40 }, { saturation: -100 }]
		}, {
		}
	];

	var customMapStyle = new google.maps.StyledMapType(styleArray, { name: "Antonino Candido" });

	var latlng = new google.maps.LatLng(43.350556, 5.604822);

	var options = {
		center: latlng,
		zoom: 15,
		mapTypeId: google.maps.MapTypeId.ROADMAP,
		mapTypeControlOptions: {
			mapTypeIds: ['custom']
		}


	};

	var carte = new google.maps.Map(document.getElementById("carte"), options);
	carte.mapTypes.set('custom', customMapStyle); //(2)
	carte.setMapTypeId('custom');

	var styledMapOptions = {
		name: "Antonino Candido"
	}



	/****************Nouveau code****************/

	//création du marqueur
	var marqueur = new google.maps.Marker({
		position: new google.maps.LatLng(43.350556, 5.604822),
		map: carte,
		icon: "images/marqueur.png"

	});


	//var contenuInfoBulle = '<img alt="Antonino Candido Logo" src="candidoLogo.png">';
	var contenuInfoBulle = '<p style="font-family:Calibri;font-size:16px;color:#333"><strong>Antonino Candido</strong><br/>1, place de l\'h�tel de ville <br/> 13360 Roquevaire</p>';
	var infoBulle = new google.maps.InfoWindow({
		content: contenuInfoBulle
	})
	/* lier l'infobulle � un marker */
	google.maps.event.addListener(marqueur, 'click', function () {
		infoBulle.open(carte, marqueur);
	});
	google.maps.event.addListener(carte, 'click', function () {
		infoBulle.close(carte, marqueur);
	});

	/********************************************/
}

