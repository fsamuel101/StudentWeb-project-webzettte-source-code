const hamburger = document.querySelector('.hamburger');
const left = document.querySelector('.left-white');
const right = document.querySelector('.forum-sidebar-lefts')

hamburger.addEventListener('click', () => {
  left.classList.toggle('active');
  right.classList.toggle('active');
  hamburger.classList.toggle('active');
});