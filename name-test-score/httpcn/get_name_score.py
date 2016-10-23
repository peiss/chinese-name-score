# coding:GB18030

'''
对http://life.httpcn.com/xingming.asp地址的姓名测试表单进行自动提交参数，获取结果页面中的分数结果

Created on 2016年10月23日

@author: crazyant.net
'''
import urllib
import urllib2
from bs4 import BeautifulSoup
import re
import sys 


reload(sys) 
sys.setdefaultencoding("GB18030")

# 请求的表单地址
REQUEST_URL = "http://life.httpcn.com/xingming.asp"

def get_name_score(name):
    result_data = {}
    
    params = {}
    
    params['data_type'] = "0"
    params['year'] = "2016"
    params['month'] = "10"
    params['day'] = "18"
    params['hour'] = "8"
    params['minute'] = "38"
    params['pid'] = "北京"
    params['cid'] = "海淀"
    params['wxxy'] = "0"
    params['xishen'] = "水"
    params['yongshen'] = "水"
    params['xing'] = name[:2]  # "裴"
    params['ming'] = name[2:]  # "云林"
    params['sex'] = "1"
    params['act'] = "submit"
    params['isbz'] = "1"
    
    post_data = urllib.urlencode(params)
    
    req = urllib2.urlopen(REQUEST_URL, post_data)
    
    content = req.read()
    
    soup = BeautifulSoup(content, 'html.parser', from_encoding="GB18030")
    
    # print soup.find(string=re.compile(u"姓名五格评分"))
    for node in soup.find_all("div", class_="chaxun_b"):
        node_cont = node.get_text()
        if u'姓名五格评分' in node_cont:
            name_wuge = node.find(string=re.compile(u"姓名五格评分"))
            result_data['wuge_score'] = name_wuge.next_sibling.b.get_text()
        
        if u'姓名八字评分' in node_cont:
            name_wuge = node.find(string=re.compile(u"姓名八字评分"))
            result_data['bazi_score'] = name_wuge.next_sibling.b.get_text()
        
    result_data['name'] = name
    return result_data


if __name__=="__main__":
    fout = open("output_result.txt", "w")
    for line in open("input_names.txt"):
        name = line[:-1]
        if len(name) == 4:
            print "不需要处理：" + name
            continue
        print "处理中：" + name
        name_data = get_name_score(name)
        print "\t姓名八字评分=" + name_data['bazi_score'] + "\t姓名五格评分=" + name_data['wuge_score']
        fout.write(name_data['name'] + "\t" + name_data['bazi_score'] + "\t" + name_data['wuge_score'] + "\n")
    fout.flush()
    fout.close()
