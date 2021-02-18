import bs4
import requests
from constants import QuestionConsts
import yaml


class Question:
    def __init__(self, link: str):
        self.link = link
        self.FullContent = self.GetFullContent()
        self.Header = self.GetHeader()
        self.QuestionContent = self.GetQuestionContent()
        self.tags = self.QuestionsTags()
        self.QuestionDict = {"link": self.link, "Header": self.Header, "QuestionContent": self.QuestionContent,
                             "tags": self.tags}

    def __str__(self):
        return yaml.dump(self.QuestionDict, allow_unicode=True)

    def GetFullContent(self):
        r = requests.get(self.link)
        r = bs4.BeautifulSoup(r.text, "html.parser")
        return r

    def GetHeader(self):
        header = self.FullContent.find(QuestionConsts.SearchType, {"class": QuestionConsts.Class})
        header = str(header.text)
        return header

    def GetQuestionContent(self):
        content = self.FullContent.find(QuestionConsts.ContentType, {"class", QuestionConsts.ContentClass})
        content = str(content.text)
        return content

    def QuestionsTags(self):
        Tags = ""
        try:
            TagsDiv = self.FullContent.find("div", {"class", QuestionConsts.TagDivClass})
            Tags = TagsDiv.find_all(QuestionConsts.TagType)
            for i in range(len(Tags)):
                Tags[i] = str(Tags[i].text)
            Tags = list(Tags)
        except:
            pass
        return Tags

    def GetDictOfQuestion(self):
        return self.QuestionDict

