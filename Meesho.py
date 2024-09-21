import requests,openpyxl
from bs4 import BeautifulSoup


excel=openpyxl.Workbook()
sheet=excel.active
sheet.title="meesho product list"
sheet.append(["Prod_name","Prod_Price","prod_Ratings"])

try:
    req=requests.get("https://www.meesho.com/mobile-cases-covers/pl/3q3")
    soup=BeautifulSoup(req.text,"html.parser")
    all_div=soup.find("div",class_="sc-gswNZR sc-hLBbgP JoMRc etQEgJ products")
    for x in all_div:
        name=x.find("p").text
        price=x.find("h5").text
        ratings=x.find("div",class_="NewProductCardstyled__RatingSection-sc-6y2tys-9 fyvrGC").span.text
        print(name,price,ratings)
        sheet.append([name,price,ratings])
except Exception as x:
    print(x)
excel.save("meesho product list.xlsx")