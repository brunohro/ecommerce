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

// Função para atualizar o preço total de um item
function atualizarPrecoTotal(id) {
    // Seleciona o campo de quantidade e o preço do produto
    const quantidadeInput = document.querySelector(`input[data-id="${id}"]`);
    const precoUnitario = parseFloat(quantidadeInput.getAttribute('data-preco'));
    const quantidade = parseInt(quantidadeInput.value);

    // Calcula o novo preço total
    const precoTotal = precoUnitario * quantidade;

    // Atualiza o campo de preço total na página
    const precoTotalElement = document.getElementById(`preco-total-${id}`);
    precoTotalElement.textContent = `Preço total: R$ ${precoTotal.toFixed(2)}`;
}

console.log("OIIIIII")

// Adiciona evento 'input' para atualizar o preço total ao mudar a quantidade
document.querySelectorAll('.quantidade').forEach(input => {
    console.log("Elemento detectado:", input);
    input.addEventListener('input', (event) => {
        const id = event.target.getAttribute('data-id');
        console.log(id)
        atualizarPrecoTotal(id);
    });
});