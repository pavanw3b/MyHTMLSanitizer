from bs4 import BeautifulSoup


class MyHTMLSanitizer:
    def __init__(self):
        self.bad_tags = ['script', 'form', 'input']
        self.bad_attributes = ['onmouseover', 'onkeydown', 'onerror']

    def sanitize(self, text):
        #  Add Sanitize Rules here
        for bad_tag in self.bad_tags:
            soup = BeautifulSoup(text, "html.parser")
            [x.extract() for x in soup.find_all(bad_tag)]
            text = str(soup)

        #  Remove only bad attributes
        soup = BeautifulSoup(text, "html.parser")
        for tag in soup.find_all():
            for key, value in tag.attrs.items():
                if key in self.bad_attributes:
                    tag[key] = None  # Set to None for now since we del in dict iteration

            #  Now delete the None attrs in list iteration
            for attr in list(tag.attrs):
                if tag[attr] is None:
                    del tag[attr]
        text = str(soup)
        #  Sanitization ends here

        return text
