# -*- coding: utf-8 -*-

import random
import os
import sys
import asyncio
import copy
import subprocess
from typing import List

import requests
from bs4 import BeautifulSoup

class Link():
    """
    - Link.url
    - Link.ID
    - Link.artists
    - Link.download(path=None)
    - Link.delete()
    """
    def __init__(self,url:str,ID:str,artists:str) -> None:
        self.url = url
        self.ID = ID
        self.artists = artists.split(",")
        self._path = f"/tmp/{ID}.mp3"

    def __str__(self) -> str:
        s = "{"
        s += f"'url': {self.url}"
        s += f", 'ID': {self.ID}"
        s += f", 'artists': {self.artists}"
        s += "}"
        return s

    def download(self, path="") -> str:
        if path:
            if path.endswith(".mp3"):
                self._path = path
            else:
                self._path = f"{path}.mp3"

        cmd = f"youtube-dl -o {self._path.replace('mp3','%(ext)s')} -x -f bestaudio --audio-format mp3 --audio-quality 0 {self.url}"
        subprocess.check_call(cmd.split())

        return self._path

    def delete(self) -> None:
        if os.path.exists(self._path):
            os.remove(self._path)

class Composition():
    """
    - Composition.title
    - Composition.Opus
    - Composition.No
    - Composition.links -> [Link]
    - Composition.wikiLink
    """
    def __init__(self,title:str,Op:str,No:str,wikiLink:str):
        self.title = title
        self.Opus = None if Op == "ㅤ" else Op
        self.No = None if No == "ㅤ" else No
        self.links: List[Link] = []
        self.wikiLink = wikiLink

    def __str__(self):
        s = f"{self.title} "
        if self.Opus:
            s += f"Op.{self.Opus} "
        if self.No:
            s += f"No.{self.No}"
        return s

    def _appendLink(self,url:str,ID:str,artists:str) -> None:
        link = Link(url,ID,artists)
        self.links.append(link)

class chopin():
    def __init__(self, parallel=False, semaphore=5, output=True) -> None:
        self.compositionList: List[Composition] = []
        while not self.compositionList:
            init = Init(output)
            if parallel:
                self.compositionList = init.mainPara(semaphore)
            else:
                self.compositionList = init.mainNotPara()
        self.genreList = [
            "Ballade",
            "Bolero",
            "Etude",
            "Fantasie",
            "Impromptu",
            "Mazurka",
            "Nocturne",
            "Concerto",
            "Sonata",
            "Scherzo",
            "Polonaise",
            "Prelude",
            "Rondo",
            "Variations",
            "Waltz",
        ]

    def __str__(self) -> str:
        return self.__repr__()

    def _list_in_list(self,l1:list,l2:list) -> bool:
        for elm in l1:
            if not elm in l2:
                return False
        return True

    def genre(self, gen=""):# -> List[Composition]:
        if not gen in self.genreList:
            gen = "Others"

        outputList = []

        if gen != "Others":
            for compo in self.compositionList:
                if gen in compo.title:
                    outputList.append(copy.deepcopy(compo))
            return outputList
        else:
            for compo in self.compositionList:
                if not self._list_in_list(self.genreList, compo.title):
                    outputList.append(copy.deepcopy(compo))
            return outputList

    def get(self):# -> Composition:
        outputCompo = None
        while not outputCompo:
            compo = random.choice(self.compositionList)
            if compo.links != []:
                outputCompo = copy.deepcopy(compo)
                outputCompo.links = [random.choice(compo.links)]

        return outputCompo

    def gets(self):# -> Composition:
        outputCompo = None
        while not outputCompo:
            compo = random.choice(self.compositionList)
            if compo.links != []:
                outputCompo = copy.deepcopy(compo)

        return outputCompo

class Init():
    def __init__(self, output=True) -> None:
        self._wiki = Wiki(output)

    def mainNotPara(self) -> List[Composition]:
        self._wiki.mainNotPara()
        return self._wiki.compoList

    def mainPara(self,semaphore) -> List[Composition]:
        self._wiki.mainPara(semaphore)
        return self._wiki.compoList

class Wiki():
    def __init__(self,output=True) -> None:
        url = "https://github.com/ster-phys/chopin/wiki"
        self.compoList :List[Composition] = []
        soup = BeautifulSoup(requests.get(url).text, "lxml")
        trList = soup.find_all("div", class_="markdown-body")[0].find_all("tr")[1:]
        for tr in trList:
            tdList = tr.find_all("td")
            link = tdList[0].find('a').get("href")
            title = str(tdList[1].string)
            Opus = str(tdList[2].string)
            No = str(tdList[3].string)
            compo = Composition(title=title,Op=Opus,No=No,wikiLink=link)
            self.compoList.append(compo)
        self.output :bool = output

    def req(self,i:int) -> None:
        if self.output:
            print("{:>3}/{} Connect to {}".format(i+1,len(self.compoList),self.compoList[i].wikiLink))

        soup = BeautifulSoup(requests.get(self.compoList[i].wikiLink).text, "lxml")
        try:
            trList = soup.find_all("div", class_="markdown-body")[0].find_all("tr")[1:]
        except IndexError as e:
            return

        if self.output:
            print("Found {} IDs".format(len(trList)))

        for tr in trList:
            tdList = tr.find_all("td")
            url = tdList[0].find('a').get("href")
            ID = str(tdList[1].string)
            artists = str(tdList[2].string)
            self.compoList[i]._appendLink(url=url,ID=ID,artists=artists)

    def mainNotPara(self) -> None:
        for i in range(len(self.compoList)):
            self.req(i)

    async def paraRun(self,loop:asyncio.unix_events._UnixSelectorEventLoop,semaphore:int):
        sem = asyncio.Semaphore(semaphore)

        async def runReq(i):
            async with sem:
                return await loop.run_in_executor(None, self.req, i)

        tasks = [runReq(i) for i in range(len(self.compoList))]
        return await asyncio.gather(*tasks)

    def mainPara(self,semaphore:int) -> None:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.paraRun(loop,semaphore))
