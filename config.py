#telegram
<<<<<<< HEAD
TOKEN_API = ''

#DB
DB_PATH = "bills.db"

# USER_IDS
ADMIN_ID = '' # для оповещения админа

# webhook settings
WEBAPP_HOST = '0.0.0.0'  # public dns/ip or 0.0.0.0


WEBAPP_PORT = 8443 # aiohttp в состсаве с aiogram работает только с 443 или 8443

# WEBHOOK_HOST = f'{WEBAPP_HOST}:{WEBAPP_PORT}' # использовать на проде
WEBHOOK_HOST = '' # для теста может использовать ngrok адрес

WEBHOOK_PATH = f'/bot{TOKEN_API}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

# использовать на проде
# WEBHOOK_SSL_CERT = '/etc/letsencrypt/live/<FQDN_OF_YOUR_HOST>/fullchain.pem'  # Path to the ssl certificate
# WEBHOOK_SSL_PRIV = '/etc/letsencrypt/live/<FQDN_OF_YOUR_HOST>/privkey.pem'  # Path to the ssl private key
=======
TOKEN_API = '' # Ваш Telegram API токен

#DB
DB_PATH = "./persistant_data/bills.db"

# Настройки оповещений
ADMIN_ID = '' # укажите ваш id. Работает для оповещения администратора о работе бота (старт/завершение работы)
ALLOW_IDS = [] # укажите список id пользователей (используется в notify.py и create_bot.py)

# webhook settings
WEBAPP_HOST = '0.0.0.0' # public dns/ip or 0.0.0.0
WEBAPP_PORT = 443 # aiogram работает с 80, 88, 443, 8443
DOMAIN_NAME = '' # укажите ваше доменное имя сервера, на котором запускается бот
WEBHOOK_HOST = f'{DOMAIN_NAME}:{WEBAPP_PORT}'
WEBHOOK_PATH = f'/bot{TOKEN_API}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'
WEBHOOK_SSL_CERT = './persistant_data/certs/fullchain.pem'  # разметстите здесь ваш сертификат
WEBHOOK_SSL_PRIV = './persistant_data/certs/privkey.pem'  # разместите здесь приватный ключ сертификата
>>>>>>> main
