$(document).ready(function(){
    $('select').material_select();
    $('.button-collapse').sideNav({
      menuWidth: 200, // Default is 300
      edge: 'left', // Choose the horizontal origin
      closeOnClick: true, // Closes side-nav on <a> clicks, useful for Angular/Meteor
      draggable: true // Choose whether you can drag to open on touch screens
    }
  );
  $('.slider').slider({
      height: 480,
      indicators: false
  });

  $("#id_prefered_block").on("change", function(){
      // This code will fire every time the user selects something
      var selected = $(this).val();
      $("#selected-block").html("<b>" + selected + "</b>");
  });

  $("#id_prefered_room").on("change", function(){
      // This code will fire every time the user selects something
      var selected = $(this).val();
      $("#selected-room").html("<b>" + selected + "</b>");
  })

  $("#id_prefered_bed").on("change", function(){
      // This code will fire every time the user selects something
      var selected = $(this).val();
      $("#selected-bed").html("<b>" + selected + "</b>");
  })

});
