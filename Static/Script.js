const form = document.querySelector('form');
form.addEventListener('submit', function (e) {
    const name = document.getElementById('name').value;
    if (name === "") {
        e.preventDefault();
        alert('Name is required');
    }
});