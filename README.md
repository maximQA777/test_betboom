# Проект автотеста сайта "Betboom"
___

### Используемый стек:  
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-plain-wordmark.svg" height="40" width="40" /> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/selenium/selenium-original.svg" height="40" width="40" /> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/chrome/chrome-original-wordmark.svg" height="40" width="40" /> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jenkins/jenkins-original.svg" height="40" width="40" /> <img src="https://avatars.githubusercontent.com/u/5879127?s=200&v=4" width="40" height="40"/> <img src="https://raw.githubusercontent.com/Vyroum/Vyroum/refs/heads/main/icons/icons8-telegram.svg" width="40" height="40"/> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pytest/pytest-original.svg" width="40" height="40"/>
          
## Что тестируется

### Игры
- Проверка наличия игр в списке (например, "Экспресс 37", "Экспресс 38", "Нарды").

### Авторизация
- Открытие формы авторизации.
- Ввод неверных данных (телефон и пароль).
- Проверка текста ошибок при неверном вводе.

### Регистрация
- Открытие формы регистрации.
- Проверка текста на странице регистрации (например, "Сбер ID", "Т-Банк").

### Бонусы и акции
- Открытие разделов "Акции и бонусы", "Клуб", "Статус".
- Проверка текста в этих разделах (например, "Приведи друга", "Boom Статус").

### Киберспорт
- Открытие раздела "Киберспорт".
- Проверка наличия популярных киберспортивных игр (например, "CS2", "Dota 2", "LoL", "Valorant").

---

### Запуск проекта автотеста в Jenkins:
1. Откройте [проект]([https://jenkins.autotests.cloud/job/betboom_allur/14/allure/])
2. Выберите ``Build with parameters``
3. Измените параметры, если требуется
4. Нажмите ``Build``
5. После сборки, результат работы можно увидеть в ``Allure Report``

>**Доступные параметры**:
>- Chrome версии 127.0
>- Chrome версии 128.0

___
## Пример отчёта в Allure

### Общий отчёт о пройденном тесте
<img src="https://github.com/maximQA777/test_betboom/bloob/main/icons/Screenshot_31.png" width="630" height="320"/>

### Детальный отчёт о пройденном тесте

<img src="https://github.com/maximQA777/test_betboom/bloob/main/icons/Screenshot_32.png" width="630" height="320"/>

### Видеопрохождение одного из теста

<img src="https://github.com/maximQA777/test_betboom/bloob/main/icons/8dc7845fdebf344ca7b6d23570118e32.mp4" width="630" height="320"/>

### Отчёт о прохождении теста в Telegram

<img src="https://github.com/maximQA777/test_betboom/bloob/main/icons/Screenshot_30.png" width="300" height="320"/>
