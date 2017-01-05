# coding:GB18030

'''
对http://life.main.com/xingming.asp地址的姓名测试表单进行自动提交参数，获取结果页面中的分数结果

Created on 2016年10月23日

@author: crazyant.net
'''
import urllib
import urllib2
from bs4 import BeautifulSoup
import re
import sys 

import config

reload(sys) 
sys.setdefaultencoding("GB18030")

# 请求的表单地址
REQUEST_URL = "http://life.main.com/xingming.asp"

def get_name_score(name_postfix):
    """调用接口，执行计算，返回结果
    """
    result_data = {}
    
    params = {}
    
    # 日期类型，0表示公历，1表示农历
    params['data_type'] = "0"
    params['year'] = "%s" % str(config.setting["year"])
    params['month'] = "%s" % str(config.setting["month"])
    params['day'] = "%s" % str(config.setting["day"])
    params['hour'] = "%s" % str(config.setting["hour"])
    params['minute'] = "%s" % str(config.setting["minute"])
    params['pid'] = "%s" % str(config.setting["area_province"])
    params['cid'] = "%s" % str(config.setting["area_region"])
    # 喜用五行，0表示自动分析，1表示自定喜用神
    params['wxxy'] = "0"
    params['xing'] = "%s" % (config.setting["name_prefix"])
    params['ming'] = name_postfix
    # 表示女，1表示男
    if config.setting["sex"] == "男":
        params['sex'] = "1"
    else:
        params['sex'] = "0"
        
    
    params['act'] = "submit"
    params['isbz'] = "1"
    
    post_data = urllib.urlencode(params)
    
    req = urllib2.urlopen(REQUEST_URL, post_data)
    
    content = req.read()
    
    soup = BeautifulSoup(content, 'html.parser', from_encoding="GB18030")
    
    full_name = get_full_name(name_postfix)
    
    # print soup.find(string=re.compile(u"姓名五格评分"))
    for node in soup.find_all("div", class_="chaxun_b"):
        node_cont = node.get_text()
        if u'姓名五格评分' in node_cont:
            name_wuge = node.find(string=re.compile(u"姓名五格评分"))
            result_data['wuge_score'] = name_wuge.next_sibling.b.get_text()
        
        if u'姓名八字评分' in node_cont:
            name_wuge = node.find(string=re.compile(u"姓名八字评分"))
            result_data['bazi_score'] = name_wuge.next_sibling.b.get_text()
        
    result_data['full_name'] = full_name
    return result_data

def get_full_name(name):
    return "%s%s" % ((config.setting["name_prefix"]), name)

def process(input_fpath, output_fpath):
    fout = open(output_fpath, "w")
    
    
    all_name_postfixs = set()
    for line in open(input_fpath):
        name_postfix = str(line).strip()
        
        if name_postfix is None or len(name_postfix) == 0:
            continue
        
        name_postfix_full = "%s%s" % (config.setting["middle_world"], name_postfix)
        
        all_name_postfixs.add(name_postfix_full)
        
    cur_idx = 0
    all_count = len(all_name_postfixs)
    for name_postfix in all_name_postfixs:
        cur_idx += 1
        
        try:
            # 以名字的后缀作为参数进行计算
            name_data = get_name_score(name_postfix)
        except Exception as e:
            print "error:", name_postfix, e
            continue
        
        print "%d/%d" % (cur_idx, all_count),
        print name_data['full_name'] + "\t姓名八字评分=" + name_data['bazi_score'] + "\t姓名五格评分=" + name_data['wuge_score']
        
        fout.write(name_data['full_name'] + "\t" + name_data['bazi_score'] + "\t" + name_data['wuge_score'] + "\n")

    fout.flush()
    fout.close()

if __name__ == "__main__":
    print "begin................................"
    process(config.setting["input_fpath"], config.setting["output_fpath"])
    print "over................................"

