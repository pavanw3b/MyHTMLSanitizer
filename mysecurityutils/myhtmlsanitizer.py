from bs4 import BeautifulSoup


class MyHTMLSanitizer:
    def __init__(self):
        self.bad_tags = ['script', 'form', 'input']
        self.bad_attributes = ['onmouseover', 'onkeydown', 'onerror']

    @staticmethod
    def sanitize(text):
        #  Add Sanitize Rules here

        return text
