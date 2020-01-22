from flask import Flask, render_template, request, redirect,url_for,flash #Flask biblioteke, 
import requests #Neophodno je kako bi aplikacija komunicirala sa openWeatherMap API-jem
import csv  #Služi kako bi mogli da skladištimo ime grada koji se pretražuje
from datetime import date 
import datetime #Prikaz datuma na web sajtu u odgovarajućem formatu

app = Flask(__name__)

app.config['DEBUG']=True #Aktivira debug mod, prilikom razvijanja aplikacije.
app.config['SECRET_KEY'] = 'thisisasecret' #This is a secret..

def get_weather_data(city): # definisanje funkcije koja prihvata ime grada i pravi request
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={ city }&units=metric&cnt=40&appid=bf30a89feee164c98eed57318f9d91e9'
    #cnt = 40 (max)
    #units=metric kako bi imali jedinice u metričkom sistemu
    #forecast nam služi kako bi dobili vremensku prognozu
    r = requests.get(url).json()
    return r

@app.route('/') #Flask putanja za GET metod
def index_get(): #definicija funkcije index_get
    city='Topola'
    with open('city.csv', newline='',mode='r') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            city = row[0]
    r = get_weather_data(city) #pozivamo funkicju koja je prethodno definisana

    weather = {
            'today': today.strftime("%B %d, %Y"),
            'city' : city,
            'country' : r['city']['country'],
            #zasto svega ima po 5 puta, pa zato sto treba 5 dana vremenske prognoze (ako je cnt max 40 i krece da broji od trenutka poziva (cele sate), 
            # Od trenutka slanja zahteva ide na sledeci ceo sat [0] je prvi dan, [8] je drugi dan, [16] je treci dan, [24] cetvrti dan, [32] je peti dan)
            'temperature1' : round(r['list'][0]['main']['temp']), #Temperatura
            'temperature2' : round(r['list'][8]['main']['temp']), 
            'temperature3' : round(r['list'][16]['main']['temp']),
            'temperature4' : round(r['list'][24]['main']['temp']),
            'temperature5' : round(r['list'][32]['main']['temp']),
            'day1' : d1, #Dani
            'day2' : d2,
            'day3' : d3,
            'day4' : d4,
            'day5' : d5,
            'description1' : r['list'][0]['weather'][0]['description'], #"Description" na sajtu
            'description2' : r['list'][8]['weather'][0]['description'],
            'description3' : r['list'][16]['weather'][0]['description'],
            'description4' : r['list'][24]['weather'][0]['description'],
            'description5' : r['list'][32]['weather'][0]['description'],
            'icon1' : r['list'][0]['weather'][0]['icon'], #"Ikonica koja daje detaljniji prikaz vremena za odgovarajući dan"
            'icon2' : r['list'][8]['weather'][0]['icon'],
            'icon3' : r['list'][16]['weather'][0]['icon'],
            'icon4' : r['list'][24]['weather'][0]['icon'],
            'icon5' : r['list'][32]['weather'][0]['icon'],
            'feels_like1' : round(r['list'][0]['main']['feels_like']), #Subjektivni osećaj
            'feels_like2' : round(r['list'][8]['main']['feels_like']),
            'feels_like3' : round(r['list'][16]['main']['feels_like']),
            'feels_like4' : round(r['list'][24]['main']['feels_like']),
            'feels_like5' : round(r['list'][32]['main']['feels_like']),
            'pressure1' : r['list'][0]['main']['pressure'], #Atmosferski pritisak
            'pressure2' : r['list'][8]['main']['pressure'],
            'pressure3' : r['list'][16]['main']['pressure'],
            'pressure4' : r['list'][24]['main']['pressure'],
            'pressure5' : r['list'][32]['main']['pressure'],
            'humidity1' : r['list'][0]['main']['humidity'], #Vlažnost vazduha
            'humidity2' : r['list'][8]['main']['humidity'],
            'humidity3' : r['list'][16]['main']['humidity'],
            'humidity4' : r['list'][24]['main']['humidity'],
            'humidity5' : r['list'][32]['main']['humidity'],
            'wind_speed1' : r['list'][0]['wind']['speed'], #Brzina vetra
            'wind_speed2' : r['list'][8]['wind']['speed'],
            'wind_speed3' : r['list'][16]['wind']['speed'],
            'wind_speed4' : r['list'][24]['wind']['speed'],
            'wind_speed5' : r['list'][32]['wind']['speed']
        }
    return render_template('index.html', weather=weather) #Funkcija vraća renderovan templejt

@app.route('/', methods=['POST']) #Flask putanja za POST metod
def index_post(): #definicija index_post
    err_msg = ''
    new_city = request.form.get('city') #Prihvatamo grad koji je korisnik
        
    if new_city:

        if new_city:
            new_city_data = get_weather_data(new_city)

            if new_city_data['cod'] == '200': #provera da li grad postoji koji je korisnik uneo
                with open('city.csv', 'w', newline='') as csvfile:
                    spamwriter = csv.writer(csvfile, delimiter=',')
                    spamwriter.writerow([new_city])
            else:
                err_msg = 'City does not exist in the world!'
        else:
            err_msg = 'City already exists in the database!'

    return redirect(url_for('index_get'))   

today=date.today() #Današnji dan
prvi = datetime.date.today() #Dan posle danas, itd.
drugi = prvi + datetime.timedelta(days=1)
treci = drugi + datetime.timedelta(days=1)
cetvrti = treci+datetime.timedelta(days=1)
peti = cetvrti+ datetime.timedelta(days=1)
dan1 = prvi.weekday()
dan2 = drugi.weekday()
dan3 = treci.weekday()
dan4 = cetvrti.weekday()
dan5 = peti.weekday()

if dan1 == 0:
    d1="Mon"
if dan1 == 1:
    d1="Tue"
if dan1 == 2:
    d1="Wed"
if dan1 == 3:
    d1 ="Thr"
if dan1==4:
    d1="Fri"
if dan1==5:
    d1="Sat"
if dan1==6:
    d1="Sun"

if dan2 == 0:
    d2="Mon"
if dan2 == 1:
    d2="Tue"
if dan2 == 2:
    d2="Wed"
if dan2 == 3:
    d2 ="Thr"
if dan2==4:
    d2="Fri"
if dan2==5:
    d2="Sat"
if dan2==6:
    d2="Sun"

if dan3 == 0:
    d3="Mon"
if dan3 == 1:
    d3="Tue"
if dan3 == 2:
    d3="Wed"
if dan3 == 3:
    d3 ="Thr"
if dan3==4:
    d3="Fri"
if dan3==5:
    d3="Sat"
if dan3==6:
    d3="Sun"

if dan4 == 0:
    d4="Mon"
if dan4 == 1:
    d4="Tue"
if dan4== 2:
    d4="Wed"
if dan4 == 3:
    d4 ="Thr"
if dan4==4:
    d4="Fri"
if dan4==5:
    d4="Sat"
if dan4==6:
    d4="Sun"

if dan5 == 0:
    d5="Mon"
if dan5 == 1:
    d5="Tue"
if dan5 == 2:
    d5="Wed"
if dan5 == 3:
    d5 ="Thr"
if dan5==4:
    d5="Fri"
if dan5==5:
    d5="Sat"
if dan5==6:
    d5="Sun"
