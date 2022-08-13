const navbar = document.getElementById('nav')
const toggler = navbar.querySelector('.navbar-toggler')
const collapse = navbar.querySelector('.navbar-collapse')

const inactiveClasses = ['navbar-dark', 'bg-transparent']
const activeClasses = ['navbar-light', 'bg-light', 'blur', 'shadow-sm']

function handleNoHeader() {
  navbar.classList.remove(...inactiveClasses, 'fixed-top')
  navbar.classList.add(...activeClasses, 'sticky-top')
}

let open = false
let scrolled = window.scrollY > 0

function setCorrectClasses() {
  const isActive = open || scrolled
  for (const activeClass of activeClasses) {
    navbar.classList.toggle(activeClass, isActive)
  }
  for (const inactiveClass of inactiveClasses) {
    navbar.classList.toggle(inactiveClass, !isActive)
  }
}

setCorrectClasses()

if (navbar.nextElementSibling.tagName.toLowerCase() !== 'header') {
  handleNoHeader()
} else {
  window.addEventListener('scroll', () => {
    scrolled = window.scrollY > 0
    setCorrectClasses()
  }, { passive: true })
  toggler.addEventListener('click', () => {
    open = !toggler.classList.contains('collapsed')
    setCorrectClasses()
  })
}
