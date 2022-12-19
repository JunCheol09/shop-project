import requests
from bs4 import BeautifulSoup
import certifi
ca = certifi.where();

from pymongo import MongoClient
client = MongoClient('mongodb+srv://JucCheol:wnscjf909@cluster0.505uedx.mongodb.net/Cluster0?retryWrites=true&w=majority',tlsCAFile=ca)
db = client.dbsparta

url = 'https://www.gsshop.com/shop/search/main.gs?lseq=392814&tq=%EB%82%98%EC%9D%B4%ED%82%A4%EC%8B%A0%EB%B0%9C&initSrchYn=Y&ab=df&gsid=gnb-AU392814-AU392814-1'

header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
}

res = requests.get(url, headers=header)

soup = BeautifulSoup(res.text, 'html.parser')


new_product_list = soup.select('#searchPrdList > section> ul> li')

for product in new_product_list:
    product_img=product.select_one('a > div> img')['src'].strip()
    product_name = product.select_one('a > dl > dt').text.strip()
    
    product_price = product.select_one('a > dl > dd.price-info > span.price > span').text.strip()
    doc={
        'product_img':product_img,
        'product_name':product_name,
        'product_price':product_price
    }
    db.shop.insert_one(doc)

