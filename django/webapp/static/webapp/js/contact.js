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

$(document).ready(function () {
	initialiser();
});