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
	
		<!-- Le CSS -->
        <link rel="stylesheet" type="text/css" href="css/style.css" />	

		<script type="text/javascript" src="js/jquery-1.6.1.min.js?<?php echo time(); ?>"></script>
		
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

				<li><a href="about.php" class="activ">A PROPOS</a></li>
				<li><a href="contact.php">CONTACT</a></li>
        </ul>
    </div><!-- end header -->	
	<div class="cont1">
	</div>
		<div id="container_a_propos_bg">
			<div id="container_a_propos">
				
				<div id="div_titre_bouton">
					<div id="div_titre">
						<h1 class="titre_h1" >à propos de moi
						</h1>
					</div>
					<div id="div_bouton"><br/>
						<p id="btn_cv">
							<a href="projets/cv-antonino-candido.pdf" target="_blank">Consulter mon cv
							</a>
						</p>
					</div>
				</div><br/>		
			
				<div id="div_presentation">
						<?php 
						/* Antonino Candido, de retour de <strong>Paris après 18 mois</strong>
						passés chez <strong>BNP Paribas Cardif</strong> dans le cadre de ma licence de Concepteur Réalisateur Web à EFFICOM,
						j'ai décidé de m'installer dans <strong>le Sud de la France</strong>.
						Mon objectif aujourd'hui est de décrocher <strong>mon premier emploi en CDI</strong> dans le domaine du multimédia.*/

						$currentDate = new DateTime();
						$startVpDate  = new DateTime('2017-03-01 09:30:00');
//Je travaille en tant que Tech Lead chez <b>Voyageprive.com</b>, <br/> depuis <?php echo $currentDate->diff($startVpDate)->format('%y ans %m mois %d jours et %h heures')
						?>
						
						Je travaille en tant que Tech Lead chez <b>voyage-prive.com</b>, depuis Mars 2017.<br><br>
						<!--<b><u><center>je ne suis pas à l'écoute du marché.</center></u></b><br/>-->

						

					Polyvalent, autonome, tout en m'intégrant parfaitement à une équipe, je suis passionné par tout ce qui touche au monde du web, que ce soit dans <strong>le domaine du webdesign ou du développement d'applications.</strong><br/><br/>

					Les projets que j'ai menés à bien m'ont permis de développer mes compétences au sein <strong>d'entreprises de premier plan</strong> (France Télécom, BNP Paribas, Crédit Agricole, Mairie de Gap...)<br/>
					<br/>
					Aujourd'hui, mon expérience s'étend également à différents domaines tels que :<br/>
					
					<ul >
						<li>Le développement en PHP orienté objet (Symfony 1.4, Phalcon, CodeIgniter)</li>
						<li>Environnement Linux / Windows - Versionning "GitHub" - Méthode Agile</li>
						<li>JavaScript orienté objet (library Jquery)</li>
						<li>Webdesign et Intégration HTML5/CSS3</li>
						<li>Responsive Design - Formation "Intégration en Responsive Design"</li>
						<li>Les CMS du type Joomla, Wordpress</li>
					</ul>
				</div>

				<div id="photo_a_propos">
					<img src="images/photo-profil.jpg" alt="photo-antonino"/>
				</div>
			</div>	
		<div id="clients_logo">
			<div class="contenair_logo">
				<div>
					<img class="logo-couleurs" border="0" src="images/clients/logos/bnp-paribas-color.png" alt="logo bnp paribas"/>
					<img border="0" src="images/clients/logos/bnp-paribas.png" alt="logo bnp paribas"/>
				</div>
			</div>
			<div class="contenair_logo">
				<div>
					<img border="0" class="logo-couleurs" src="images/clients/logos/france-telecom-color.png" alt="logo france t�l�com"/>
					<img border="0" src="images/clients/logos/france-telecom.png" alt="logo france t�l�com"/>
				</div>
			</div>
			<div class="contenair_logo">
				<div>
					<img border="0" class="logo-couleurs" src="images/clients/logos/orange-color.png" alt="logo orange"/>
					<img border="0" src="images/clients/logos/orange.png" alt="logo orange"/>
				</div>
			</div>
			<div class="contenair_logo">
				<div>
					<img border="0" class="logo-couleurs" src="images/clients/logos/internet-cmwa-color.png" alt="logo internet-cmwa"/>
					<img border="0" src="images/clients/logos/internet-cmwa.png" alt="logo internet-cmwa"/>
				</div>
			</div>
			<div class="contenair_logo">
				<div>
					<img border="0" class="logo-couleurs" src="images/clients/logos/mairie-de-gap-color.png" alt="logo ville de Gap(05)"/>
					<img border="0" src="images/clients/logos/mairie-de-gap.png" alt="logo ville de Gap(05)"/>
				</div>
			</div>
			<div class="contenair_logo">
				<div>
					<img border="0" class="logo-couleurs" src="images/clients/logos/etsi-color.png" alt="logo etsi"/>
					<img border="0" src="images/clients/logos/etsi.png" alt="logo etsi"/>
				</div>
			</div>
			<div class="contenair_logo">
				<div>
					<img border="0" class="logo-couleurs" src="images/clients/logos/vox-company-color.png" alt="logo vox company"/>
					<img border="0" src="images/clients/logos/vox-company.png" alt="logo vox company"/>
				</div>
			</div>
			<div class="contenair_logo">
				<div>
					<img border="0" class="logo-couleurs" src="images/clients/logos/kior-management-color.png" alt="logo kior management"/>
					<img border="0" src="images/clients/logos/kior-management.png" alt="logo kior management"/>
				</div>
			</div>
			<div class="contenair_logo">
				<div>
					<img border="0" class="logo-couleurs" src="images/clients/logos/sonnailles-color.png" alt="logo ferme des sonnailles"/>
					<img border="0" src="images/clients/logos/sonnailles.png" alt="logo ferme des sonnailles"/>
				</div>
			</div>
			<div class="contenair_logo">
				<div>
					<img border="0" class="logo-couleurs" src="images/clients/logos/services-a-la-personne-color.png" alt="logo services � la personne"/>
					<img border="0" src="images/clients/logos/services-a-la-personne.png" alt="logo services � la personne"/>
				</div>
			</div>
		</div>
			
		</div>
		
						<?php include('footer.php');?>
	<script type="text/javascript">
	$("div .logo-couleurs").css("opacity", 0);
	 $(".logo-couleurs").hover(function(){
			   $(this).fadeTo("fast", 1.0); // This should set the opacity to 100% on hover
			   },function(){
			   $(this).fadeTo("fast", 0); // This should set the opacity back to 0% on mouseout
			   });
			   </script>
    </body>
</html>