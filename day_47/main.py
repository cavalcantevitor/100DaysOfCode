from bs4 import BeautifulSoup
import requests
import smtplib

URL = "https://www.invictus.com.br/calca-maverick-preta.html"
EMAIL = "email"
PASSWORD = "password"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(response.content, "html.parser")

price = soup.find(name="span", class_="price").get_text()
price = float(price[2:].replace(",", "."))

print(f"{price:.2f}")

target_price = 349

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=EMAIL, password=PASSWORD)
    connection.sendmail(
        from_addr=EMAIL,
        msg=f"Subject:Desconto INVICTUS\n\nSe liga! Descontao na Invictus! Calca Maverick por apenas R${price:.2f}!",
        to_addrs=f"email"
    )