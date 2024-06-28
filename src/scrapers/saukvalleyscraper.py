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

        pass

