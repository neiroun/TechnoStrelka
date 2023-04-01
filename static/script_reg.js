window.onload = () => {
    document.getElementById('back').onclick = () => {
        document.location='table'
    }
    document.getElementById('delet').onclick = () => {
        let req = new XMLHttpRequest();
        req.open('GET', '/del?id=' + document.getElementById('del').value, true);
        req.send();
        Swal.fire("Успех!", "Преподаватель успешно удален", "success");
    }
    document.getElementById('add').onclick = () => {
        let req = new XMLHttpRequest();
        req.open('GET', '/add?FIO=' + document.getElementById('FIO').value + '&obj=' + document.getElementById('subject').value, true)
        req.send();
        Swal.fire("Успех!", "Преподаватель успешно добавлен", "success");
    }
}