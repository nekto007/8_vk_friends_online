# Watcher of Friends Online
Этот скрипт показывает в терминале список ваших друзей в Интернете в vk.
Перед первым запуском вы должны получить **"APP_ID"** . Чтобы получить **"APP_ID"**,
Вы должны зарегистрировать свое приложение на: **https://vk.com/dev**.
После этого Вы получите: **"APP_ID"**, Вы должны открыть код и изменить параметр: **"APP_ID"**.

```bash
. . .

import vk

APP_ID = 0 # Change APP_ID


def get_user_login():
. . .
```

# Пример Запуска
Откройте терминал, перейдите в каталог, в котором находится файл
и запустить **"python vk_friends_online.py"**, если python 3 не является значением по умолчанию
запустите **"python3 vk_friends_online.py"**


```bash

$ python vk_friends_online.py
Введите Ваше имя пользователя vk:
<Ваш VK логин>
Введите Ваш пароль vk:
<Ваш VK логин>
Список Ваших друзей в сети:
<Имя1> <Фамилия1>
<Имя2> <Фамилия2>

. . .


```

# How to Install

Python 3 должен быть проинсталлирован.
Используйте **pip3** для установки зависимостей:

```bash
pip3 install -r requirements.txt
```

Remember, it is recommended to use [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) for better isolation.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)