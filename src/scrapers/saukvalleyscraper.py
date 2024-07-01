import urllib3
from bs4 import BeautifulSoup
from typing import List, Dict

class SaukValleyScraper():
    def scrape_listings_url(self) -> List:
        http = urllib3.PoolManager()
        res = urllib3.request("GET", "https://realty.saukvalleyproperties.com/idx/featured?start=1&per=100")
        if res.status != 200:
            raise Exception(f"Response Status: {res.status}")
        
        soup = BeautifulSoup(res.data, 'html.parser')
        address_anchors = soup.find_all(class_="IDX-resultsAddressLink")
        url_list = []
        for link in address_anchors:
            url_list.append(link.get("href"))

        return url_list
    

    def scrape_listing_data(self, url: str) -> Dict:
        http = urllib3.PoolManager()
        res = urllib3.request("GET", url)
        if res.status != 200:
            raise Exception(f"Response Status: {res.status}")
        
        soup = BeautifulSoup(res.data, 'html.parser')
        scraped_data = {"url": url}

        photos_url = soup.find(id="IDX-photoGalleryLink")
        scraped_data["photos"] = photos_url.get("href")

        address_el = soup.find(class_="IDX-detailsAddressInfo")
        address_data = []
        for el in address_el.children:
            address_data.append(el.text.trim())

        address_el_two = soup.find(class_="IDX-detailsAddressLocationInfo")
        for el in address_el_two.children:
            address_data.append(el.text.trim())

        scraped_data["address"] = " ".join(address_data)

        price = soup.find(id="IDX-detailsPrice")
        scraped_data["price"] = price.text

        field_data = soup.find(id="IDX-detailsHeadFields")
        for data in field_data.children:
            kids = data.children
            scraped_data[kids[1].text.trim()] = kids[0].text.trim()

        year = soup.find(id="IDX-fieldData")
        scraped_data["year_built"] = year.text.trim()
        