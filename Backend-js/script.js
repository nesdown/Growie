jQuery('document').ready(function() {
  let curTask = jQuery("#content").text();
  let intTask = parseInt(curTask);

  jQuery(".fw-button-next").on('click', function(){
    intTask += 1;
    console.log(curTask);
    console.log(intTask);

    jQuery("#content").text(intTask.toString());
  });

  jQuery(".fw-button-previous").on('click', function(){
    intTask -= 1;
    console.log(curTask);
    console.log(intTask);

    jQuery("#content").text(intTask.toString());
  });
});
