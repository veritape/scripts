import codecs
import os
import unittest

from bs4 import BeautifulSoup

from verita_scripts import pull_data_from_redam_pages


class TestREDAM(unittest.TestCase):
    def test_vinculos(self):
        filename = os.path.join('redam_html_files', '1755.html')
        print(filename)
        html = codecs.open(filename, "r", "latin1").read()
        soup = BeautifulSoup(html)
        expected = [
            {'nombre_completo': 'CORONADO PARRA HERMINIA', 'vinculo': 'DEMANDANTE'},
            {'nombre_completo': 'DURAND CORONADO JAIRO', 'vinculo': 'DEMANDANTE'},
        ]
        result = pull_data_from_redam_pages.get_vinculo(soup)
        self.assertEqual(expected, result)
