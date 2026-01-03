import os
import requests

ip = os.getenv("VDS_IP")

url_input = input("Enter URL to shorten: ")

response = requests.get(
    f"http://{ip}:8000/shorturl",
    params={"url": url_input}
)

if response.status_code == 200:
    data = response.json()
    print("Kısa URL:", data["short_url"])
else:
    print("Hata:", response.status_code)