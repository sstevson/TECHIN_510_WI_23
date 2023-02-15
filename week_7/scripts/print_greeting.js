const dynamic = document.getElementById('dynamic')

dynamic.addEventListener('click', printHello);
function printHello() {
    const greeting = 'Greetings!';
    window.alert(greeting);
}