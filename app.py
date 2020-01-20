from flask import Flask, render_template, request, redirect,url_for,flash
import requests
import pprint
import csv  
from datetime import date
import datetime
app = Flask(__name__)

app.config['DEBUG']=True
app.config['SECRET_KEY'] = 'thisisasecret'

def get_weather_data(city):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={ city }&units=metric&cnt=40&appid=bf30a89feee164c98eed57318f9d91e9'
    #cnt = 40 (max)
    r = requests.get(url).json()
    return r
        
@app.route('/')
def index_get():
    city='Topola'
    with open('city.csv', newline='',mode='r') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            city = row[0]
    r = get_weather_data(city)

    weather = {
            'today': today.strftime("%B %d, %Y"),
            'city' : city,
            'country' : r['city']['country'],
            #zasto svega ima po 5 puta, pa zato sto treba 5 dana vremenske prognoze (ako je cnt max 40 i krece da broji od trenutka poziva (cele sate), 
            # Od trenutka slanja zahteva ide na sledeci ceo sat [0] je prvi dan, [8] je drugi dan, [16] je treci dan, [24] cetvrti dan, [32] je peti dan)
            'temperature1' : r['list'][0]['main']['temp'],
            'temperature2' : r['list'][8]['main']['temp'], 
            'temperature3' : r['list'][16]['main']['temp'],
            'temperature4' : r['list'][24]['main']['temp'],
            'temperature5' : r['list'][32]['main']['temp'],
            'day1' : d1,
            'day2' : d2,
            'day3' : d3,
            'day4' : d4,
            'day5' : d5,
            'description1' : r['list'][0]['weather'][0]['description'],
            'description2' : r['list'][8]['weather'][0]['description'],
            'description3' : r['list'][16]['weather'][0]['description'],
            'description4' : r['list'][24]['weather'][0]['description'],
            'description5' : r['list'][32]['weather'][0]['description'],
            'icon1' : r['list'][0]['weather'][0]['icon'],
            'icon2' : r['list'][8]['weather'][0]['icon'],
            'icon3' : r['list'][16]['weather'][0]['icon'],
            'icon4' : r['list'][24]['weather'][0]['icon'],
            'icon5' : r['list'][32]['weather'][0]['icon'],
            'feels_like1' : r['list'][0]['main']['feels_like'],
            'feels_like2' : r['list'][8]['main']['feels_like'],
            'feels_like3' : r['list'][16]['main']['feels_like'],
            'feels_like4' : r['list'][24]['main']['feels_like'],
            'feels_like5' : r['list'][32]['main']['feels_like'],
            'pressure1' : r['list'][0]['main']['pressure'],
            'pressure2' : r['list'][8]['main']['pressure'],
            'pressure3' : r['list'][16]['main']['pressure'],
            'pressure4' : r['list'][24]['main']['pressure'],
            'pressure5' : r['list'][32]['main']['pressure'],
            'humidity1' : r['list'][0]['main']['humidity'],
            'humidity2' : r['list'][8]['main']['humidity'],
            'humidity3' : r['list'][16]['main']['humidity'],
            'humidity4' : r['list'][24]['main']['humidity'],
            'humidity5' : r['list'][32]['main']['humidity'],
            'wind_speed1' : r['list'][0]['wind']['speed'],
            'wind_speed2' : r['list'][8]['wind']['speed'],
            'wind_speed3' : r['list'][16]['wind']['speed'],
            'wind_speed4' : r['list'][24]['wind']['speed'],
            'wind_speed5' : r['list'][32]['wind']['speed']
        }
    return render_template('index.html', weather=weather)

@app.route('/', methods=['POST'])
def index_post():
    err_msg = ''
    new_city = request.form.get('city')
        
    if new_city:

        if new_city:
            new_city_data = get_weather_data(new_city)

            if new_city_data['cod'] == '200':
                with open('city.csv', 'w', newline='') as csvfile:
                    spamwriter = csv.writer(csvfile, delimiter=',')
                    spamwriter.writerow([new_city])
            else:
                err_msg = 'City does not exist in the world!'
        else:
            err_msg = 'City already exists in the database!'

            #Mozes da ubacis neku notifikaciju a i ne mora


    return redirect(url_for('index_get'))   

today=date.today()
prvi = datetime.date.today()
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