
async function gerarHash() {

    const username = document.getElementById('username').value;

    // Obtendo o texto do campo de input
    const texto = document.getElementById('password').value;
    
    // Transformando o texto em um buffer
    const encoder = new TextEncoder();
    const data = encoder.encode(texto);
    
    // Gerando o hash SHA-256
    const hashBuffer = await crypto.subtle.digest('SHA-256', data);
    
    // Convertendo o hash de ArrayBuffer para string hexadecimal
    const hashArray = Array.from(new Uint8Array(hashBuffer));
    const hashHex = hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
    
    const errorMessage = document.getElementById('error-message');

    if (username === 'admin' && hashHex === '5c5a6fc39e510ac2dc87e6421dd794e93154879ae4b4723b992f75e0b6d500a5') {
        sessionStorage.setItem('role', 'admin');
        window.location.href = '/admin';
        return false;
    } else {
        errorMessage.textContent = 'Usuário ou senha incorretos';
        return false;
    }
}
