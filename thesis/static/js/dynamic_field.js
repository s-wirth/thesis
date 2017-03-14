$(document).ready(function () {
  var OPTION_ID = 1;
  $('#pollForm')
  // Add button click handler
    .on('click', '.addButton', function () {
      var optionsList = $('.options');
      var optionTemplate = $('#optionTemplate').text();
      var newOption = $.parseHTML(optionTemplate);
      OPTION_ID += 1;
      var new_name = 'option' + OPTION_ID;
      $(newOption).find('input').attr('id', new_name);
      $(newOption).find('label').attr('for', new_name).text("Option " + OPTION_ID);

      optionsList.append(newOption);
    })

    // Remove button click handler
    .on('click', '.removeButton', function () {
      var $row = $(this).parents('.form-group');
      $row.remove();
    })
});