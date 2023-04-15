from urllib import request
from bs4 import BeautifulSoup
import json

def get_session_list(link):
    response = request.urlopen(link)
    soup = BeautifulSoup(response, "html.parser")
    response.close()

    response = request.urlopen(link)
    soup = BeautifulSoup(response, "html.parser")
    response.close()

    data = soup.find("article")
    data = str(data).split("<hr/>")

    session_title_list = []
    for i in range(len(data)):
        session_title = data[i][data[i].find("<em>") + len("<em>"):data[i].find("</em>")]
        if data[i].find("<em>") != -1:
            session_title_list.append(session_title)

    return session_title_list

def get_sessions_article_dict(link):
    response = request.urlopen(link)
    soup = BeautifulSoup(response, "html.parser")
    response.close()

    data = soup.find("article")
    data = str(data).split("<hr/>")

    session_title_list = []
    for i in range(len(data)):
        session_title = data[i][data[i].find("<em>") + len("<em>"):data[i].find("</em>")]
        if data[i].find("<em>") != -1:
            session_title_list.append(session_title)

    paper_name_dict = {}
    idx = 0
    for i in range(1, len(data)):
        session_data = BeautifulSoup(data[i], "html.parser").find_all("p")
        article_title_list = []
        for j in range(1, len(session_data)):
            idx += 1
            article_title = str(session_data[j])[str(session_data[j]).find("<strong>") + len("<strong>"):str(session_data[j]).find("</strong>")]
            article_title_list.append("{}_".format(str(idx).zfill(3)) + article_title)
        paper_name_dict[session_title_list[i - 1]] = article_title_list

    return paper_name_dict