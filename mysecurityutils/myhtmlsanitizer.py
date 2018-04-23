from bs4 import BeautifulSoup


class MyHTMLSanitizer:
    def __init__(self):
        self.bad_tags = ['script', 'form', 'input']
        self.bad_attributes = ['onerror', 'onload', 'onblur', 'onmouseover']

        self.good_tags = ['p', 'div', 'b', 'i', 'img', 'a']
        self.good_attributes = ['src', 'href', 'class']
        self.modifiers = [{"a": {"target": "_blank", "rel": "noreferrer nofofllow"}}]
        self.bad_attr_values = ['javascript:']

    def sanitize(self, text):
        #  Add Sanitize Rules here
        soup = BeautifulSoup(text, "html.parser")
        for tag in soup.find_all():
            if tag.name not in self.good_tags: # tag.name == <p> == p
                tag.extract()

        for tag in soup.find_all():
            for key, value in tag.attrs.items():
                if key not in self.good_attributes:
                    tag[key] = None

            for attr in list(tag.attrs):
                if tag[attr] is None:
                    del tag[attr]

        #  Modify tags
        for element in soup.find_all():
            for modifier in self.modifiers:
                for tags in modifier:
                    for tag in tags:
                        if element.name == tag:
                            for key in modifier[tag].keys():
                                element[key] = modifier[tag][key]

        # remove bad attr values
        for element in soup.find_all():
            for key, value in element.attrs.items():
                for bad_attr_value in self.bad_attr_values:
                    if bad_attr_value in value:
                        element[key] = None

            # Remove the attribute
            for attr in list(element.attrs):
                if element[attr] is None:
                    del element[attr]

        text = str(soup)

        return text
