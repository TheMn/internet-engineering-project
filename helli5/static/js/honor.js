// quick search regex
var qsRegex;
var buttonFilter;
var buttonFilter2;

// init Isotope
var $grid = $('.grid').isotope({
  itemSelector: '.element-item',
  layoutMode: 'fitRows',
  filter: function() {
    var $this = $(this);
    var searchResult = qsRegex ? $this.text().match( qsRegex ) : true;
    var buttonResult = buttonFilter ? $this.is( buttonFilter ) : true;
    var buttonResult2 = buttonFilter2 ? $this.is( buttonFilter2 ) : true;
    return searchResult && buttonResult2 && buttonResult ;
  }
});

// bind filter on select change
$('.filters-select').on( 'change', function() {
  // get filter value from option value
  // var filterValue = this.value;
  // use filterFn if matches value
  buttonFilter = this.value;
  //$grid.isotope({ filter: filterValue });
  $grid.isotope();
});

// bind filter on select change
$('.filters-select2').on( 'change', function() {
  // get filter value from option value
  // var filterValue = this.value;
  // use filterFn if matches value
  buttonFilter2 = this.value;
  //$grid.isotope({ filter: filterValue });
  $grid.isotope();
});

// use value of search field to filter
var $quicksearch = $('#quicksearch').keyup( debounce( function() {
  qsRegex = new RegExp( $quicksearch.val(), 'gi' );
  $grid.isotope();
}) );

// debounce so filtering doesn't happen every millisecond
function debounce( fn, threshold ) {
  var timeout;
  return function debounced() {
    if ( timeout ) {
      clearTimeout( timeout );
    }
    function delayed() {
      fn();
      timeout = null;
    }
    setTimeout( delayed, threshold || 100 );
  };
}