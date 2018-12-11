import requests as req
from fuzzywuzzy import fuzz


class HTMLparser():

    def get_body(self, html):
        tags = []
        openFound = False
        for i in range(len(html)):
            if openFound is False and html[i: i+5] == "<body":
                tags.append(i)
                openFound = True
            elif openFound is True and html[i: i+7] == "</body>":
                tags.append(i)
                break
        return html[tags[0]:tags[1]]

    def find_h1(self, html):
        heading = []
        for i in range(len(html)):
            if html[i: i+3] == "<h1":
                j = i + 3
                while html[j] != ">":
                    j += 1
                q = j
                while html[q] != "<":
                    q += 1
                heading = html[j+1:q]
                break
        return heading

    def find_local_hrefs(self, html):
        hrefs = []
        for i in range(len(html)):
            if html[i: i+7] == 'href="/':
                j = i+7
                while html[j] != '"':
                    j += 1
                hrefs.append(html[i+12:j])
        return hrefs

    def find_hrefs(self, html):
        hrefs = []
        for i in range(len(html)):
            if html[i: i+5] == "href=":
                j = i+6
                while html[j] != '"':
                    j += 1
                hrefs.append(html[i+6:j])
        return hrefs

    def String_Filter(self, strings, baseWord):
        ratios = []
        for i in range(len(strings)):
            ratio = fuzz.ratio(strings[i], baseWord)
            if ratio > 40:
                ratios.append((ratio, strings[i]))
        return ratios


html = req.get(
    "https://en.wikipedia.org/wiki/Python_(programming_language)").text

Parser = HTMLparser()


def beta1(startHeader, endHeader, clicks):
    wikipedia = "https://en.wikipedia.org/wiki/"
    html = req.get(wikipedia + startHeader).text

    body = Parser.get_body(html)
    currentHeader = Parser.find_h1(body)
    print(currentHeader)

    if currentHeader == endHeader:
        return "Found! In " + str(clicks) + " click." if clicks == 1 else "Found! In " + str(clicks) + " clicks"

    else:
        hrefs = Parser.find_local_hrefs(body)
        ratios = Parser.String_Filter(hrefs, endHeader)
        bestMatch = ratios[0]
        for i in range(len(ratios)):
            if ratios[i][0] == 100:
                clicks += 1
                return beta1(ratios[i][1], endHeader, clicks)
            elif ratios[i][0] > bestMatch[0]:
                bestMatch = ratios[i]
        return (bestMatch, "test")


test = beta1("Operating_system",
             "CPython", 0)
print(test)
# body = myParser.get_body(html)

# h1s = myParser.find_local_hrefs(body)
# print(String_Filter(h1s))
# print(myParser.find_h1(body))
# print(myParser.find_local_hrefs(body))
