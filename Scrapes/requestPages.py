import requests as req


class HTMLparser():

    def get_body(self, html):
        tags = []
        openFound = False
        for i in range(len(html)):
            if html[i: i+5] == "<body" and openFound is False:
                tags.append(i)
                openFound = True
            elif openFound is True and html[i: i+7] == "</body>":
                tags.append(i)
                break
        return html[tags[0]:tags[1]]

    def find_hrefs(self, html):
        hrefs = []
        for i in range(len(html)):
            if html[i: i+5] == "href=":
                j = i+6
                while html[j] != '"':
                    j = j + 1
                hrefs.append(html[i+6:j])
        return hrefs


html = req.get(
    "https://en.wikipedia.org/wiki/Main_Page").text

myParser = HTMLparser()

body = myParser.get_body(html)

print(myParser.find_hrefs(body))
