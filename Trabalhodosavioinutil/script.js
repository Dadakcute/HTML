const input = document.getElementById('tarefa');
const lista = document.getElementById('lista');
const contador = document.getElementById('contador');

function atualizarContador() {
    contador.textContent = lista.children.length;
}

function adicionarTarefa() {
    const texto = input.value.trim();

    if (texto === '') {
        alert('Digite uma tarefa!');
        return;
    }

    const li = document.createElement('li');

    const span = document.createElement('span');
    span.textContent = texto;

    span.addEventListener('click', () => {
        span.classList.toggle('concluida');
    });

    const botaoRemover = document.createElement('button');
    botaoRemover.textContent = 'X';
    botaoRemover.classList.add('remover');

    botaoRemover.addEventListener('click', () => {
        li.remove();
        atualizarContador();
    });

    li.appendChild(span);
    li.appendChild(botaoRemover);

    lista.appendChild(li);

    input.value = '';

    atualizarContador();
}

function limparTarefas() {
    lista.innerHTML = '';
    atualizarContador();
}