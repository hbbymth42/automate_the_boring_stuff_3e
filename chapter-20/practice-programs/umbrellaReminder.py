#! python3
# umbrellaReminder.py - Sends a text to pack an umbrella before leaving the house when it's raining for the day - In Honolulu, Hawaii

import bs4, requests, re

notify_topic = '[Enter ntfy topic link]'

res = requests.get('https://forecast.weather.gov/MapClick.php?lat=21.306940000000054&lon=-157.85832999999997')
res.raise_for_status()
weatherSoup = bs4.BeautifulSoup(res.text, 'html.parser')
weatherElems = weatherSoup.select("div[class='col-sm-10 forecast-text']")

if re.findall(r"showers",str(weatherElems[0]),re.IGNORECASE) != []:
    requests.post(notify_topic, "Don't forget to bring an Umbrella!")
