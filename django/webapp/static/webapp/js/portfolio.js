$(document).ready(function () {
	var galeriePos = new Array,
		nbr_images = new Array,
		idprojet,
		substr,
		num_projet,
		vignettes = $('div.info_cache');

	vignettes.css("opacity", 0);

	$.each($('ul.item img'), function (i, item) {
		nbr_images[i] = $(item).attr('src');
	});

	$(vignettes).stop().bind('click', function (e) {
		e.preventDefault();
		displayProject(this);
	});

	/**
	 * Reset thumbs
	 */
	function reset_thumbs() {
		vignettes.removeClass('current');
		vignettes.css({ 'opacity': '0', 'cursor': 'pointer' });
	}

	/**
	 * 
	 * @param {*} event 
	 */
	function displayProject(event) {

		$(vignettes).css({ 'opacity': '0', 'cursor': 'pointer' });
		$(event).css({ 'opacity': '0.9', 'cursor': 'default' });


		//on récupère la valeur de la propriété id
		idprojet = $(event).attr('id');
		num_projet = $(event).attr("class");;
		substr = num_projet.split(' ');
		galeriePos = substr[1];


		// j'arrete la fonction si le projet de la vignette cliqué est déjà ouvert
		if ($(event).is('.current')) {
			return false;
		}

		//je teste si la div qui affiche le contenu d'un projet n'est pas déjà ouvert et j'effectue une animation differente
		if ($('.cont1').is('.open')) {

			$(vignettes).removeClass('current');
			$(event).addClass('current');

			$('#contenu-client').animate({ opacity: 0 }, 500, function () {
				recup_projet(idprojet, 0);
			});
			return false;
		}

		//sinon j'effectue les animations qui affichent le projet choisi dans les vignettes
		$(vignettes).removeClass('current');
		$(event).addClass('current');
		$.scrollTo('body', 800, {});
		$('.cont1').slideUp("slow", function () {
			$('.cont2').slideDown("slow");
			recup_projet(idprojet, 0);
		});
		$(event).addClass('current');
		$('.cont1').addClass('open');
		return false;
	}

	//function qui récupère l'id de la vignette cliqu� et charge son contenu dans la div cach� 
	function recup_projet(project_id, etat) {
		$('.pxs_container_projekt').css("background", "none");
		$('.pxs_container_projekt').css("background-color", get_project_color(project_id));
		$('#pxs_container').append('<div class="pxs_loading" id="portfolio">Chargement...</div>');
		$('.pxs_loading').fadeIn(540);
		if (etat == '1') {
			$('#contenu-client').animate({ opacity: 0 }, 800, function () {
				$('#contenu-client').css({ 'display': 'none' });
				load_project(project_id);
			});
			return false;
		}

		$('#contenu-client').css({ 'opacity': '0', 'display': 'none' });
		$.scrollTo('body', 800, {});
		$('#thumb-portfolio,.footer').fadeOut("slow", function () {
			load_project(project_id);
		});
		return false;
	};

	$.changeprojet = function (direction) {

		reset_thumbs();
		if (direction == 'prev')
			galeriePos--;
		else
			galeriePos++;
		if (galeriePos == nbr_images.length) { galeriePos = 0; }
		if (galeriePos == -1) { galeriePos = nbr_images.length - 1; }
		//idprojet = $(nbr_images[galeriePos]).attr("id");
		idprojet = $('div.' + galeriePos).attr("id");
		$('div#' + idprojet).addClass('current');
		$('div#' + idprojet).css({ 'opacity': '0.9', 'cursor': 'default' });
		recup_projet(idprojet, 1);
	};

	/**
	 * Get project color values
	 * @param {*} project_id
	 */
	function get_project_color(project_id) {
		// project_settings - global variable
		if (typeof project_settings.color_hash[project_id] === "undefined") {
			return "#c8c9ca"; // default value
		}
		return project_settings.color_hash[project_id];
	}

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
							$('.pxs_container_projekt').css(
								"background",
								[
									get_project_color(project_id),
									"url(" + image_path + "/projets/background/" + project_id + ".jpg)",
									"no-repeat top center"
								].join(' ')
							);
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

