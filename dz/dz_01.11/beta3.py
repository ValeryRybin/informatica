import requests

city = 'Долгопрудный'

url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=ru&appid=2e446065206cfc6d7bafbb82078c86f5'
# отправляем запрос на сервер и сразу получаем результат
weather_data = requests.get(url).json()
# получаем данные о температуре и о том, как она ощущается
temperature = round(weather_data['main']['temp'])
temperature_feels = round(weather_data['main']['feels_like'])
# выводим значения на экран
print('Сейчас в городе', city, str(temperature), '°C')
print('Ощущается как', str(temperature_feels), '°C')