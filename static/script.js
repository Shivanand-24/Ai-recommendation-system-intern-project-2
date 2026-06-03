document.addEventListener('DOMContentLoaded', () => {
    const toggle = document.querySelector('#theme-toggle');
    const body = document.body;
    const storedTheme = localStorage.getItem('aiTheme');

    if (storedTheme === 'dark') {
        body.classList.add('dark-mode');
    }

    toggle?.addEventListener('click', () => {
        body.classList.toggle('dark-mode');
        const activeTheme = body.classList.contains('dark-mode') ? 'dark' : 'light';
        localStorage.setItem('aiTheme', activeTheme);
    });

    const predictionForm = document.querySelector('#prediction-form');
    predictionForm?.addEventListener('submit', (event) => {
        const inputs = document.querySelectorAll('#prediction-form input[type="number"]');
        let valid = true;

        inputs.forEach((input) => {
            const value = input.value.trim();
            if (value === '' || Number.isNaN(Number(value))) {
                input.classList.add('invalid');
                valid = false;
            } else {
                input.classList.remove('invalid');
            }
        });

        if (!valid) {
            event.preventDefault();
            alert('Please enter valid numeric values for all fields.');
        }
    });
});
