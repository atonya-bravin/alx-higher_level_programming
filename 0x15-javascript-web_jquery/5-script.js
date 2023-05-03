$('document').ready(
	$('#add_item').click(
		function addElement()
		{
			let list_item = $('<li></li>').text("Item");
			$('UL.my_list').prepend(list_item);
		}
	)
);
