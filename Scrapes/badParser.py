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
    "https://en.wikipedia.org/wiki/Python_(programming_language)").text

Parser = HTMLparser()
Utils = Other_Stuff()

body = Parser.get_body(html)


def beta_v2(html, end_header, prev_rating, back_index):

    body = Parser.get_body(html)
    header = Parser.find_h1(body)

    print(back_index)
    if back_index > 10:
        return "Failed"
    if header == end_header:
        return "Found!"

    links = Parser.find_local_hrefs(body)

    ratios = Utils.String_Filter(links, end_header, 50)
    sorted_ratios = Utils.sorting_links(ratios)
    
    rating = sorted_ratios[len(sorted_ratios)][1][0]
   
beta_v2(html, "Object-oriented programming", 0, 0)
