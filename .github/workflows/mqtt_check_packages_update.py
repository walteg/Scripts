#!/usr/bin/env python3

import subprocess
import configparser


# Реквизиты для подключения к MQTT
config = configparser.ConfigParser()
config.read('/home/walteg/scripts/other/settings.ini')
ip = config.get('MQTT', 'ip')
usr = config.get('MQTT', 'usr')
password = config.get('MQTT', 'password')

# Выполнение команды и получение вывода
result = subprocess.run(['apt', 'list', '--upgradable'], capture_output=True, text=True)

# Извлечение числового значения
output = result.stdout
package_count = len(output.split('\n')) - 1

# Формирование строки для отправки в MQTT
packages = format(package_count)
subprocess.run(['mosquitto_pub', '-h', ip, '-t', 'srv/system/packeges/count', '-m', packages, '-r', '-u', usr, '-P', password])
