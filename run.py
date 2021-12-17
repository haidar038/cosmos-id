from flask import Flask, render_template
import requests
import schedule
import datetime
import locale

# Set locale time
locale.setlocale(locale.LC_ALL, 'id')

# App declaration
app = Flask(__name__)


@app.route('/')
def data():
    # Data Kasus
    response_kasus = requests.get(
        'https://apicovid19indonesia-v2.vercel.app/api/indonesia')
    response_vaksin = requests.get(
        'https://vaksincovid19-api.vercel.app/api/vaksin')
    result_vaksin = response_vaksin.json()
    result_kasus = response_kasus.json()
    positif = result_kasus['positif']
    sembuh = result_kasus['sembuh']
    meninggal = result_kasus['meninggal']
    positif_formatted = f"{positif:,}"
    sembuh_formatted = f"{sembuh:,}"
    meninggal_formatted = f"{meninggal:,}"
# Data Vaksin
    target = result_vaksin['totalsasaran']
    stage1 = result_vaksin['vaksinasi1']
    stage2 = result_vaksin['vaksinasi2']
    stage1_formatted = f"{stage1:,}"
    stage2_formatted = f"{stage2:,}"
    # target_formatted =
# Last Update
    update = result_kasus['lastUpdate']
    vaksin_update = result_vaksin['lastUpdate']
    parse_update = datetime.datetime.strptime(update, '%Y-%m-%dT%H:%M:%S.%fZ')
    tanggal = parse_update.strftime('%A, %d %B %Y Pukul %H:%M:%S WIB')
    parse_update2 = datetime.datetime.strptime(vaksin_update, '%Y-%m-%dT%H:%M:%S.%f')
    tanggal2 = parse_update2.strftime('%A, %d %B %Y Pukul %H:%M:%S WIB')
    return render_template('index.html', positif=positif_formatted, sembuh=sembuh_formatted, meninggal=meninggal_formatted, tanggal=tanggal, tanggal2=tanggal2, tahap1=stage1_formatted, tahap2=stage2_formatted)


if __name__ == "__main__":
    app.run(debug=True)
