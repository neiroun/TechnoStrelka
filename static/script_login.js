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
            localStorage.setItem('button', '1')
            document.location='table'
        }
        else {
            document.getElementById('sign_in').addEventListener('click', function(){
                Swal.fire("Ой!", "Кажется, что вы ввели неверный пароль, попробуйте еще раз", "error");
              });
        }
    }
    document.getElementById('sign_like_guest').onclick = () => {
        localStorage.setItem('button', '0')
        document.location='table'
    }
}
