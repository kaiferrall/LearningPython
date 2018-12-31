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
                hrefs.append((html[i+12:j], i+7))
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


class Other_Stuff():
    def String_Filter(self, strings, baseWord, limit):
        ratios = []
        for i in range(len(strings)):
            ratio = fuzz.ratio(strings[i][0], baseWord)
            if ratio > limit:
                ratios.append((ratio, strings[i]))
        return ratios

    def replace_spaces(self, string):
        for i in range(len(string)-1):
            if string[i] == " ":
                string = string[:i] + "_" + string[i+1:]
        return string

    def sorting_links(self, array):
        largest = array[len(array)-1][0]
        for j in range(len(array)-1, 0, -1):
            for i in range(0, j):
                if array[i][0] > largest:
                    largest = array[i][0]
                    placeholder = array[j]
                    array[j] = array[i]
                    array[i] = placeholder
            largest = array[j-1][0]
        return array


html = req.get(
    "https://www.nytimes.com/").text

Parser = HTMLparser()
Utils = Other_Stuff()

body = Parser.get_body(html)
h1s = Parser.find_h1(body)
atags = Parser.find_local_hrefs(body)
print(h1s)
print(atags)