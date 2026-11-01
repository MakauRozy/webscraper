import requests

URL = "https://quotes.toscrape.com/"
header= {"User-Agent": "Rozie practice cot. contact: rozie@gmail.com"}
response= requests.get(URL, headers=header, timeout=10)
print(response.status_code)