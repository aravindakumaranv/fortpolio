document.getElementById('theme-toggle').addEventListener('click', function() {
    document.documentElement.classList.toggle('light-mode');
    document.body.classList.toggle('light-mode');
    const sunIcon = document.querySelector('.sun-icon');
    const moonIcon = document.querySelector('.moon-icon');
    if (document.body.classList.contains('light-mode')) {
        sunIcon.style.display = 'none';
        moonIcon.style.display = 'inline';
    } else {
        sunIcon.style.display = 'inline';
        moonIcon.style.display = 'none';
    }
});
