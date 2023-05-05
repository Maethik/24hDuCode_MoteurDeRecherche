const searchIcon = document.getElementById('search-icon');
const form = document.querySelector('form');

searchIcon.addEventListener('click', function(event) {
  event.preventDefault();
  form.submit();
});
