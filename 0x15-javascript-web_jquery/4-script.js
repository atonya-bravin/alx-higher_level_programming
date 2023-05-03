$('document').ready(
	$('#toggle_header').click(
		function toggleCssClass()
		{
			$('header').toggleClass('red green');
		}
	)
);
