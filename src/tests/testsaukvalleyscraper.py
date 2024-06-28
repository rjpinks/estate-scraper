import sys
import os

import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

from scrapers.saukvalleyscraper import SaukValleyScraper

class TestSaukValleyScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = SaukValleyScraper()

    def test_url_collection(self):
        url_list = self.scraper.scrape_listings_url()

        first_three = url_list[:3]
        last_three = url_list[-3:]
        
        expected_head = [
            "https://realty.saukvalleyproperties.com/idx/details/listing/c019/12067406/5465-W-Penn-Corner-Road",
            "https://realty.saukvalleyproperties.com/idx/details/listing/c019/12087290/307-Knollwood-Drive",
            "https://realty.saukvalleyproperties.com/idx/details/listing/c019/12051796/905-Monongahela-Drive"
        ]
        expected_tail = [
            "https://realty.saukvalleyproperties.com/idx/details/listing/c019/11980447/212-Minnesota-Drive",
            "https://realty.saukvalleyproperties.com/idx/details/listing/c019/11484296/117-S-Hennepin-Avenue",
            "https://realty.saukvalleyproperties.com/idx/details/listing/c019/11868879/319-W-Everett-Street"
        ]

        self.assertEqual(first_three, expected_head)
        self.assertEqual(last_three, expected_tail)
    

    def run_all_tests(self):
        self.test_url_collection()
    

tests = TestSaukValleyScraper()
tests.setUp()
tests.test_url_collection()

if __name__ == '__main__':
    unittest.main()
