from bs4 import BeautifulSoup


class MyHTMLSanitizer:

    @staticmethod
    def sanitize(text):
        #  Add Sanitize Rules here
        soup = BeautifulSoup(text, "html.parser")
        [x.extract() for x in soup.findAll('script')]
        text = str(soup)
        #  Sanitizing ends

        return text
