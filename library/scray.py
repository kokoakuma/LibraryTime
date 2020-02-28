from bs4 import BeautifulSoup
import requests

def scray():
  url = 'http://library.rikkyo.ac.jp/schedule/'

  response = requests.get(url)
  soup = BeautifulSoup(response.text, "html.parser")
  result = soup.find(id="areaIkebukuro")
  result = result.find_all("td")

  array = []
  arrayS = []

  for entry in result:
    text = entry.get_text()
    validatedText = text.replace('\xa0', 'notDate')
    if entry.has_attr("bgcolor") and "#" in entry.attrs['bgcolor'] and len(validatedText) < 7:
      array.append(entry.attrs['bgcolor'])
  print(array)
  print(len(array))

  colors = [ "#E60012", "#796BAF", "#FFF67F", "#61C1BE", "#EE87B4", ]
  times = [ "closed", "8:30-20:00", "8:30-22:30", "9:00-20:00", "10:00-17:00" ]

  def convertColorToTime(value):
    num = colors.index(value)
    return times[num]

  schedule = list(map(convertColorToTime, array))
  return schedule