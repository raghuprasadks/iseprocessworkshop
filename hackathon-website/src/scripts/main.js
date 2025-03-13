document.addEventListener('DOMContentLoaded', () => {
    const registrationForm = document.getElementById('registration-form');
    
    if (registrationForm) {
        registrationForm.addEventListener('submit', (event) => {
            event.preventDefault();
            const formData = new FormData(registrationForm);
            const data = Object.fromEntries(formData.entries());
            console.log('Registration Data:', data);
            alert('Thank you for registering! We will get back to you soon.');
            registrationForm.reset();
        });
    }

    const trendsSection = document.getElementById('trends');
    if (trendsSection) {
        const trends = [
            'AI-generated art and music',
            'Natural language processing advancements',
            'Generative adversarial networks (GANs)',
            'AI in gaming and virtual environments',
            'Ethics and implications of generative AI'
        ];

        const trendsList = document.createElement('ul');
        trends.forEach(trend => {
            const listItem = document.createElement('li');
            listItem.textContent = trend;
            trendsList.appendChild(listItem);
        });
        trendsSection.appendChild(trendsList);
    }
});