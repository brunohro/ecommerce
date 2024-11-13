// Verificação básica de senhas
const form = document.querySelector('form');
const password = document.getElementById('password');
const confirmPassword = document.getElementById('confirm-password');
const passwordError = document.getElementById('password-error');

form.addEventListener('submit', function(event) {
    if (password.value !== confirmPassword.value) {
        event.preventDefault(); // Impede o envio do formulário
        passwordError.style.display = 'block'; // Mostra a mensagem de erro
    }
});

// ------------------------------------------------------------------------------------------------------------------
