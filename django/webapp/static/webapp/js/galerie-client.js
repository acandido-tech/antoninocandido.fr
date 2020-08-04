			 $(document).ready(function(){ 	
			 var exec = 0;
$('#retour').click(function(e) {
	e.preventDefault(); 
	$('div.info_cache').removeClass('current');
    $('div.info_cache').css({'opacity' : '0', 'cursor' : 'pointer'});
	$('.cont2').slideUp("slow", function() {
		$('.cont1').slideDown("slow");
		$('.cont1').removeClass('open');	
		$.scrollTo('#bandeau_menu', 800, {});  
	});
});
							
$('#galerie-client').coinslider({ 
hoverPause: true
});


$('#projet-prev-galerie-client').click(function(e){
	e.preventDefault();
	if(exec == 0)	{
	$.changeprojet('prev');
	exec++;
	}
	});

$('#projet-next-galerie-client').click(function(e){
	e.preventDefault();
	if(exec == 0)	{
		$.changeprojet('next');
		exec++;
	}
	});
	
	
	
	});