const input = document.getElementById('login');

if (input){
    input.addEventListener('click', () => {
        if (input.setSelectionRange) {
            setTimeout(() => {
                input.setSelectionRange(0, 0);
                input.focus();
            }, 1);
        }
    });
}

window.onload = () => {
    document.getElementById('sign_in').onclick = () => {
        this.login = document.getElementById('login').value;
        this.password = document.getElementById('password').value;
        if (this.login === 'admin' & this.password === 'admin'){
            document.location='table'
        }
        else {
            alert('Вы ввели неверный пароль')
        }
    }
    document.getElementById('sign_like_guest').onclick = () => {
        document.location='table'
    }
}
