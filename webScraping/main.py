import requests
import urllib3
from bs4 import BeautifulSoup
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
datas = []
BASE_URL = "https://www.vatanbilgisayar.com"
API_BASE_URL = "YOUR_API_BASE_URL"
CATEGORY_URLs = [
    "tuketici-elektronigi",
    "bilgisayar",
    "televizyon",
    "bilgisayar-bilesenleri",
    "mutfak-urunleri",
    "elektrikli-ev-aletleri",
    "kisisel-bakim-urunleri",
    "hafiza-karti",
    "fotograf-makinesi-aksesuarlari",
    "fotograf-makinesi",
    "yazici",
    "hesap-makinesi",
    "yazilim",
    "tuketim-malzemeleri",
    "oto-ses-sistemleri",
    "aksesuar-urunleri",
    "drone",
    "oyun-konsollari",
    "elektrikli-tasitlar"
]

def get_category_id(category):
    response = (requests.get(API_BASE_URL + f"/Categories/GetCategory/{category}", verify=False))
    return response.json().get("id")

def create_category(name, parent_category_id=None):
    params = {"name": name}
    if parent_category_id is not None:
        params["parentCategoryId"] = parent_category_id

    response = requests.post(API_BASE_URL + "/Categories/CreateCategory", json=params, verify=False)
    return response.json().get("id")

def get_or_create_category(category_name, parent_id=None):
    try:
        existing_category_id = get_category_id(category_name)
        if existing_category_id :
            return existing_category_id

        new_category = create_category(category_name, parent_id)
        return new_category.id

    except Exception as e:
        print(f"Kategori işleminde hata oluştu: {e}")
        return None

for curl in CATEGORY_URLs:
    for page in range(1,6):
        try:
            url = f"{BASE_URL}/{curl}/?page={page}"
            R = requests.get(url)
            Soup = BeautifulSoup(R.text, "html5lib")
            List = Soup.find("div", {"class": "wrapper-product wrapper-product--list-page clearfix"}).find_all("div", {
                "class": "product-list"})

            for product in List:
                purl = product.find("a", {"class":"product-list-link"}).get("href")

                if purl.startswith("/"):
                    purl = BASE_URL + purl

                R = requests.get(purl)
                Soup = BeautifulSoup(R.text, "html5lib")
                title = Soup.find("div", {"product-list__content product-detail-big-price"}).h1.text.strip()
                price = Soup.find("span", {"class": "product-list__price"}).text.replace('.', '')
                image = Soup.find("a",{"data-fancybox":"images"}).img.get("data-srcset")
                rating = Soup.find("div", {"class": "rank-star"}).span.get("style").replace("width: ","").replace("%;","")
                rating_count = Soup.find("a", {"class": "comment-count"}).span.text.replace("(", "").replace(")", "")

                property = Soup.find("div", {"class": "wrapper-breadcrumb"}).find_all("a", {"class", "bradcrumb-item"})
                uzunluk = len(property)

                model_no = property[uzunluk - 1].get_text()
                brand = property[uzunluk - 2].get_text()
                category_name = property[uzunluk - 3].get_text()

                categories = [category.get_text() for category in property[:uzunluk - 2]]

                parent_id = None
                category_id = None
                for category_name in categories:
                    category_id = get_or_create_category(category_name, parent_id)
                    if category_id is None:
                        break
                    parent_id = category_id

                data = {
                    "name": title,
                    "brand": brand,
                    "modelNo": model_no,
                    "price": price,
                    "imageUrl": image,
                    "categoryId": category_id,
                    "rating": rating,
                    "ratingCount": rating_count
                }
                datas.append(data)
                print(data)
        except :
            print("error")

request = {
    "products": datas
}

with open('request.json', 'w', encoding='utf-8') as file:
    json.dump(request, file, indent=4, ensure_ascii=False)
