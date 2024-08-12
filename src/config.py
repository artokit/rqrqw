import configparser

config = configparser.ConfigParser()
config.read('settings.ini')

BOT_TOKEN = config['bot']['token']

ADMIN_ID = [int(admin_id) for admin_id in config['bot']['admin_id'].split(',')]
