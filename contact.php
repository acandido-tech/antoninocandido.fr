<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="fr">
<head>
				<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />	
  <meta name="robots" content="index, follow" />
  <meta name="keywords" content="antonino candido, antonino, candido, graphiste multimédia, graphiste, developpeur, developpeur multimedia, webdesigner, paca, toulon, paris" />
  <meta name="description" content="Polyvalent, autonome, tout en m'intégrant parfaitement à une équipe, je suis passionné par tout ce qui touche au monde du web, que ce soit dans le domaine du webdesign ou du développement d'applications." />
  <meta name="generator" content="Antonino Candido - Portfolio 2012" />

		<title>Antonino Candido - Développeur Multimédia</title>
       
	   <!-- Le JavaScript -->
		<script type="text/javascript" src="js/jquery-1.6.1.min.js?<?php echo time(); ?>"></script>
		<script type="text/javascript" src="js/jquery.easing.1.3.js?<?php echo time(); ?>"></script>
		<script type="text/javascript" src="js/effect.js?<?php echo time(); ?>"></script>

		<meta name="viewport" content="initial-scale=1.0, user-scalable=no" />
		<!-- Inclusion de l'API Google MAPS -->
		<!-- Le param�tre "sensor" indique si cette application utilise d�tecteur pour d�terminer la position de l'utilisateur -->
		<script type="text/javascript" src="http://maps.google.com/maps/api/js?sensor=false"></script>

		<!-- Le CSS -->
        <link rel="stylesheet" type="text/css" href="css/style.css" />		
		<!--[if IE 7]> <link rel="stylesheet" href="css/ie7.css" type="text/css" media="screen" /> <![endif]-->
	<script type="text/javascript">

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-28641345-1']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

</script>		
</head>
<body>
    <div id="bandeau_menu" >
         <a href="index.php"><img id="logo_up" src="images/logo.jpg" alt="logo antonino candido"/></a>
        <ul id="nav">
                <li><a href="index.php">ACCUEIL</a></li>
				<li><a href="portfolio.php">PORTFOLIO</a></li>

				<li><a href="about.php">A PROPOS</a></li>
				<li><a href="contact.php" class="activ">CONTACT</a></li>
        </ul>
    </div><!-- end header -->	
	<div class="cont1"></div>
	
	<div  id="container_contact_bg">
		<div id="container_contact">	
			<div id="div_titre_bouton">
				<h1 class="titre_h1">Contactez moi</h1>
			</div><br/>
			<div id="carte"></div>		
			<div id="background_ipad">
				<img src="images/ipad.png" alt="ipad - contact"/>
			</div>

			<div id="contact_info">
				<p class="questions">
					N'hésitez pas à me contacter pour toute question ou demande <br/> de devis, je vous répondrai dès que possible !<br/><br/>
				</p><hr/><br/>
				<p>
					<span class="title">Adresse	</span><br/><br/>
				<span>1, place de l'hôtel de ville<br/>
				13360 Roquevaire</span>
				</p><br/><hr/><br/>
				<p>
					<span class="title">Téléphone &amp; Mail
					</span><br/><br/>
				06.66.60.77.72<br/>
				<a class="mailto" href="mailto:candido.antonino@gmail.com">candido.antonino@gmail.com</a>
				</p>
			</div>


		</div>
				
			</div>
		
		<?php include('footer.php');?>
		
		<script type="text/javascript">
			$(document).ready(function() {
				initialiser();
			});
		</script>
    </body>
</html>