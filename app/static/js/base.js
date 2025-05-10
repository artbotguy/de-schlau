// Анимация переворота
function flipCard(card) {
    card.classList.toggle('flipped');

    // Анимация через animate.css
    card.classList.add('animate__animated', 'animate__flipInY');
    setTimeout(() => {
        card.classList.remove('animate__animated', 'animate__flipInY');
    }, 500);
}

// Загрузка новых карточек без перезагрузки страницы (AJAX)
document.querySelector('.pagination').addEventListener('click', async (e) => {
    e.preventDefault();
    if (e.target.tagName === 'A') {
        const response = await fetch(e.target.href);
        const html = await response.text();
        document.querySelector('.cards-container').innerHTML =
            new DOMParser().parseFromString(html, 'text/html')
                .querySelector('.cards-container').innerHTML;
    }
});