jQuery('document').ready(function() {
	milestone = jQuery('p2').val().slice(-1);

	jQuery('button').on('click', function() {
		milestone = milestone + 1;
		jQuery('p2').append(milestone);
	});
}