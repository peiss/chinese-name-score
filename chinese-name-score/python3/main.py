from urllib.parse import urlencode

import requests
from bs4 import BeautifulSoup


def get_name_score(name):
    url = "http://life.httpcn.com/xingming.asp"

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {
        "data_type": 0,
        "year": 1980,
        "month": 2,
        "day": 25,
        "hour": 16,
        "minute": 10,
        "pid": "北京".encode("gb2312"),
        "cid": "北京".encode("gb2312"),
        "wxxy": 0,
        "xishen": "金".encode("gb2312"),
        "yongshen": "金".encode("gb2312"),
        "xing": "裴".encode("gb2312"),
        "ming": name.encode("gb2312"),
        "sex": 1,
        "act": "submit",
        "isbz": 1
    }

    params_data = urlencode(data)
    # print(params_data)
    r = requests.post(url, data=params_data, headers=headers)
    r.encoding = 'gb2312'

    if r.status_code != 200:
        raise Exception()
    # print(r.text)
    soup = BeautifulSoup(r.text, "html.parser")
    for node in soup.find_all("div", class_="chaxun_b"):
        # print(node)
        if "姓名五格评分" not in node.get_text():
            continue
        score_fonts = node.find_all("font")
        wuge_score = score_fonts[0].get_text()
        bazi_score = score_fonts[1].get_text()
        return wuge_score.replace("分", "").strip(), bazi_score.replace("分", "").strip()


with open("input.txt") as fin, open("output.txt", "w") as fout:
    for line in fin:
        line = line.strip()
        if not line or len(line) == 0:
            continue
        wuge, bazi = get_name_score(line)
        fout.write(
            "\t".join([
                "裴%s" % line,
                wuge,
                bazi
            ]) + "\n"
        )
