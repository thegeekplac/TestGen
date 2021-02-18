from requests import get
from bs4 import BeautifulSoup
from constants import ScraperConsts as constants
from Question import *
import yaml


def GetSiteContent(link):
    r = get(link)
    r = BeautifulSoup(r.text, "html.parser")
    return r


def GetQuestionsLinks(SiteContent):
    links = SiteContent.find_all(constants.SearchType, {"class": constants.Class})
    for i in range(len(links)):
        item = links[i]
        links[i] = item.get("href")
    return links


def Questions():
    content = GetSiteContent(constants.link)
    LinksArr = GetQuestionsLinks(content)
    LinksArr = list(LinksArr)
    DumpArr = []
    for i in range(len(LinksArr)):
        LinksArr[i] = Question(LinksArr[i])
        DumpArr.append(LinksArr[i].GetDictOfQuestion())
        print(i)
    with open("Questions.yaml", "w+") as f:
        yaml.dump(DumpArr, f, allow_unicode=True)


Questions()
