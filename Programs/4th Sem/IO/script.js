const form = document.querySelector('form');
const usernameInput = document.getElementById('username');
const passwordInput = document.getElementById('password');
const errorMessage = document.getElementById('error-message');

form.addEventListener('submit', (e) => {
  e.preventDefault();
  const username = usernameInput.value.trim();
  const password = passwordInput.value.trim();
  
  if (username === 'admin' && password === 'admin') {
    window.location.href = 'dashboard.html';
  } else {
    errorMessage.innerHTML = '';
    
    if (username !== 'admin') {
      errorMessage.innerHTML += '<p>Invalid username</p>';
    }
    
    if (password !== 'admin') {
      errorMessage.innerHTML += '<p>Invalid password</p>';
    }
    
    errorMessage.classList.add('error-message');
  }
});
