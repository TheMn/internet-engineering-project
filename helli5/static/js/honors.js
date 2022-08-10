/** @type {HTMLSelectElement} */
const subjectSelect = document.getElementById('firstSelector')
/** @type {HTMLSelectElement} */
const periodSelect = document.getElementById('selectorTwo')
/** @type {HTMLInputElement} */
const searchInput = document.getElementById('quicksearch')
const notFound = document.getElementById('not-found')
const items = document.querySelectorAll('.item')

function filter() {
  const selectedPeriodNumber = periodSelect.selectedIndex // zero if nothing is selected
  const subject = subjectSelect.value // empty string if nothing is selected
  const searchQuery = searchInput.value
  
  let found = false
  for (const item of items) {
    const itemName = item.querySelector('.honor-name').textContent
    const itemPeriod = item.querySelector('.honor-period').textContent
    const itemText = item.querySelector('.honor-text').textContent
    const itemPeriodNumber = parseInt(itemPeriod.match(/\d+/)[0])
    if (
      (!selectedPeriodNumber || selectedPeriodNumber === itemPeriodNumber) &&
      (!searchQuery || itemName.includes(searchQuery) || itemText.includes(searchQuery)) &&
      (!subject || item.classList.contains(subject))
    ) {
      item.classList.remove('d-none')
      found = true
    } else {
      item.classList.add('d-none')
    }
  }

  if (!found) {
    notFound.classList.remove('d-none')
  } else {
    notFound.classList.add('d-none')
  }
}

subjectSelect.addEventListener('change', filter)
periodSelect.addEventListener('change', filter)
searchInput.addEventListener('input', filter)
searchInput.addEventListener('change', filter)
