// // quick search regex
// var qsRegex;
// var buttonFilter;
// var buttonFilter2;

// // init Isotope
// var $grid = $('.grid').isotope({
//   itemSelector: '.element-item',
//   layoutMode: 'fitRows',
//   filter: function() {
//     var $this = $(this);
//     var searchResult = qsRegex ? $this.text().match( qsRegex ) : true;
//     var buttonResult = buttonFilter ? $this.is( buttonFilter ) : true;
//     var buttonResult2 = buttonFilter2 ? $this.is( buttonFilter2 ) : true;
//     return searchResult && buttonResult2 && buttonResult ;
//   }
// });

// // bind filter on select change
// $('.filters-select').on( 'change', function() {
//   // get filter value from option value
//   // var filterValue = this.value;
//   // use filterFn if matches value
//   buttonFilter = this.value;
//   //$grid.isotope({ filter: filterValue });
//   $grid.isotope();
// });

// // bind filter on select change
// $('.filters-select2').on( 'change', function() {
//   // get filter value from option value
//   // var filterValue = this.value;
//   // use filterFn if matches value
//   buttonFilter2 = this.value;
//   //$grid.isotope({ filter: filterValue });
//   $grid.isotope();
// });

// // use value of search field to filter
// var $quicksearch = $('#quicksearch').keyup( debounce( function() {
//   qsRegex = new RegExp( $quicksearch.val(), 'gi' );
//   $grid.isotope();
// }) );

// // debounce so filtering doesn't happen every millisecond
// function debounce( fn, threshold ) {
//   var timeout;
//   return function debounced() {
//     if ( timeout ) {
//       clearTimeout( timeout );
//     }
//     function delayed() {
//       fn();
//       timeout = null;
//     }
//     setTimeout( delayed, threshold || 100 );
//   };
// }

/** @type {HTMLSelectElement} */
const subjectSelect = document.getElementById('firstSelector')
/** @type {HTMLSelectElement} */
const periodSelect = document.getElementById('selectorTwo')
/** @type {HTMLInputElement} */
const searchInput = document.getElementById('quicksearch')
const items = document.querySelectorAll('.item')

function filter() {
  const period = periodSelect.selectedIndex // zero if nothing is selected
  const subject = subjectSelect.value // empty string if nothing is selected
  const searchQuery = searchInput.value
  for (const item of items) {
    const itemName = item.getAttribute('data-name')
    const itemPeriodNumber = parseInt(item.getAttribute('data-period').match(/\d+/)[0])
    if (
      (!period || period === itemPeriodNumber) &&
      (!searchQuery || itemName.includes(searchQuery)) &&
      (!subject || item.classList.contains(subject))
    ) {
      item.classList.remove('d-none')
    } else {
      item.classList.add('d-none')
    }
  }
}

subjectSelect.addEventListener('change', filter)
periodSelect.addEventListener('change', filter)
searchInput.addEventListener('input', filter)
searchInput.addEventListener('change', filter)
