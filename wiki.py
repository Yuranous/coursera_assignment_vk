from bs4 import BeautifulSoup
import unittest

def parse(path_to_file):
    with open(path_to_file, encoding='utf-8') as f:
        wiki_html = f.read()
    soup = BeautifulSoup(wiki_html, 'lxml')
    imgs = len(soup.findAll(lambda tag: tag['width'] >= 200))
    headers = len(soup.findAll(lambda tag: tag.string[0] in ('E', 'T', 'C')))
    return [imgs, headers, linkslen, lists]


class TestParse(unittest.TestCase):
    def test_parse(self):
        test_cases = (
            ('wiki/Stone_Age', [13, 10, 12, 40]),
            ('wiki/Brain', [19, 5, 25, 11]),
            ('wiki/Artificial_intelligence', [8, 19, 13, 198]),
            ('wiki/Python_(programming_language)', [2, 5, 17, 41]),
            ('wiki/Spectrogram', [1, 2, 4, 7]),)

        for path, expected in test_cases:
            with self.subTest(path=path, expected=expected):
                self.assertEqual(parse(path), expected)


if __name__ == '__main__':
    unittest.main()
