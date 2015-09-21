// result from solve.py
var steps = '(4, 1), (1, 1), (0, 2), (2, 4), (1, 4), (3, 1), (2, 2), (1, 4), (0, 0), (3, 4), (0, 1), (2, 3), (4, 2), (1, 2), (1, 3), (4, 2), (3, 0), (4, 0), (0, 0), (3, 3), (0, 4)';

// dealy in clicking in milliseconds
var delay = 500;

// create js array
steps = steps.replace(/[(]/g, '');
steps = steps.replace(/[)]/g, '');
steps = steps.replace(/([0-9]+),\s([0-9]+),\s/g, '$1, $2; ');
steps = steps.replace(/[ ]/g, '');
steps = steps.split(';');

// go each position
steps.forEach(function (position, index) {

  // do after dealy time
  setTimeout(function () {
    // click on circle
    $('[data-position="' + position + '"]').trigger('click');

    // log position
    console.log(position);
  }, index * delay);

});
