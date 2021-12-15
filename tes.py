from flask.sessions import SecureCookieSession
import requests
import datetime
import locale

# Set locale time
locale.setlocale(locale.LC_ALL, 'id')

# Making a get request
response = requests.get(
    'https://apicovid19indonesia-v2.vercel.app/api/indonesia')
result = response.json()
positif = result['positif']
sembuh = result['sembuh']
meninggal = result['meninggal']
update = result['lastUpdate']
parse_update = datetime.datetime.strptime(
    update, '%Y-%m-%dT%H:%M:%S.%fZ')
# print json content
# print(f'{positif:,}')
print("Tanggal :", parse_update.strftime('%d %B %Y'))
print("Pukul   :", parse_update.strftime('%A, %H:%M:%S'), "WIB")
print(result)
