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
    document.getElementById('sign_in').onclick = function(){
        document.location='table'
    }
}