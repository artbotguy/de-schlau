
// Функция для загрузки списка слов
async function loadWords() {
    const response = await fetch('/words');
    const words = await response.json();
    const list = document.getElementById('wordList');
    list.innerHTML = words.map(w =>
        `<li>${w.word} - ${w.translation}</li>`
    ).join('');
}

// Загружаем слова при открытии страницы
loadWords();

// Обновляем список после добавления нового слова
// Добавьте это в обработчик успешной отправки формы:
// loadWords();

document.getElementById('wordForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const formData = {
        word: e.target.word.value,
        translation: e.target.translation.value
    };

    try {
        const response = await fetch('/words/add', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData)
        });

        const result = await response.json();

        const messageEl = document.getElementById('message');
        messageEl.style.display = 'block';

        if (response.ok) {
            messageEl.textContent = `Успешно добавлено: ${formData.word} - ${formData.translation}`;
            messageEl.className = 'message success';
            e.target.reset(); // Очищаем форму
        } else {
            messageEl.textContent = `Ошибка: ${result.error || 'Неизвестная ошибка'}`;
            messageEl.className = 'message error';
        }
    } catch (error) {
        console.error('Ошибка:', error);
    }
});
