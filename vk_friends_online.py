from getpass import getpass
import vk
import sys

APP_ID = 0


def get_user_login():
    login = input('Введите Ваше имя пользователя vk: ')
    return login


def get_user_password():
    password = getpass('Введите Ваш пароль vk: ')
    return password


def get_online_friends(
        login,
        password,
        api_version='5.73',
        api_lang='ru',
        api_timeout=10
        ):
    try:
        session = vk.AuthSession(
            app_id=APP_ID,
            user_login=login,
            user_password=password,
            scope='friends',
        )
        api = vk.API(session, v=api_version, api_lang=api_lang, api_timeout=api_timeout)
        friends_online_ids = api.friends.getOnline()
        friends_online = (api.users.get(user_ids=friends_online_ids))
        return friends_online
    except vk.exceptions.VkAuthError:
        print('Логин или пароль некорректные, запустите скрипт заново')
        sys.exit(0)


def output_friends_to_console(friends_online):
    if friends_online:
        print('Список Ваших друзей в сети:')
        for friend in friends_online:
            print(friend['first_name'], friend['last_name'])
    else:
        print('Все Ваши друзья оффлайн')

if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
