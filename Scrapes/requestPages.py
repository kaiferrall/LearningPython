import requests as req


class HTMLparser():

    def get_body(self, html):
        tags = []
        openFound = False
        for i in range(len(html)):
            if html[i: i+5] == "<body" and openFound is False:
                tags.append(i)
                openFound = True
            elif html[i: i+7] == "</body>" and openFound is True:
                tags.append(i)
                break
        print(tags)
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
print(html)
myParser = HTMLparser()

body = myParser.get_body(html)

print(myParser.find_hrefs(body))
