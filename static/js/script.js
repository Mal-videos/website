// Example: simple scroll animation
document.addEventListener('DOMContentLoaded', () => {
    const cards = document.querySelectorAll('.card');
    cards.forEach(card => {
        card.style.opacity = 0;
    });

    window.addEventListener('scroll', () => {
        const triggerBottom = window.innerHeight / 5 * 4;
        cards.forEach(card => {
            const cardTop = card.getBoundingClientRect().top;
            if(cardTop < triggerBottom){
                card.style.transition = "0.5s";
                card.style.opacity = 1;
                card.style.transform = "translateY(0)";
            }
        });
    });
});
