# coding:GB18030

"""
对http://life.main.com/xingming.asp地址的姓名测试表单进行自动提交参数，获取结果页面中的分数结果

Created on 2016年10月23日

@author: crazyant.net
""" 

import urllib 
import urllib2 
from bs4 import BeautifulSoup 
import re
import sys 
import threading
import time 
import threadpool

from main import user_config
from main import sys_config

reload(sys) 
sys.setdefaultencoding("GB18030")

curr_idx = 0
all_count = 0
fout = None

def get_name_postfixs():
    """根据是否使用单字和用户配置的性别参数，获取所有的名字列表
    """
    target_name_postfixs = set()
    
    # 是否有单字限制
    has_limit_word = False
    limit_word = user_config.setting["limit_world"]
    if limit_word is not None and len(limit_word) > 0:
        has_limit_word = True
        
    if has_limit_word:
        if user_config.setting["sex"] == "男":
            fpath_input = sys_config.FPATH_DICTFILE_BOYS_SINGLE
        elif user_config.setting["sex"] == "女":
            fpath_input = sys_config.FPATH_DICTFILE_GIRLS_SINGLE
        
        print "has limit word, fpath=%s" % fpath_input
        
        for line in open(fpath_input):
                iter_name = str(line).strip()
                target_name_postfixs.add("%s%s" % (limit_word, iter_name))
    else:
        if user_config.setting["sex"] == "男":
            fpath_input = sys_config.FPATH_DICTFILE_BOYS_DOUBLE
        elif user_config.setting["sex"] == "女":
            fpath_input = sys_config.FPATH_DICTFILE_GIRLS_DOUBLE

        for line in open(fpath_input):
                iter_name = str(line).strip()
                target_name_postfixs.add(iter_name)
    
    return target_name_postfixs


def compute_name_score(name_postfix):
    """调用接口，执行计算，返回结果
    """
    result_data = {}
    params = {}
    
    # 日期类型，0表示公历，1表示农历
    params['data_type'] = "0"
    params['year'] = "%s" % str(user_config.setting["year"])
    params['month'] = "%s" % str(user_config.setting["month"])
    params['day'] = "%s" % str(user_config.setting["day"])
    params['hour'] = "%s" % str(user_config.setting["hour"])
    params['minute'] = "%s" % str(user_config.setting["minute"])
    params['pid'] = "%s" % str(user_config.setting["area_province"])
    params['cid'] = "%s" % str(user_config.setting["area_region"])
    # 喜用五行，0表示自动分析，1表示自定喜用神
    params['wxxy'] = "0"
    params['xing'] = "%s" % (user_config.setting["name_prefix"])
    params['ming'] = name_postfix
    # 表示女，1表示男
    if user_config.setting["sex"] == "男":
        params['sex'] = "1"
    else:
        params['sex'] = "0"
        
    params['act'] = "submit"
    params['isbz'] = "1"
    
    # for k, v in params.items():
    #    print k, v
    
    post_data = urllib.urlencode(params)
    req = urllib2.urlopen(sys_config.REQUEST_URL, post_data)
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
    
    result_data['total_score'] = float(result_data['wuge_score']) + float(result_data['bazi_score'])
    result_data['full_name'] = full_name
    return result_data
    

def compute_and_writefile(name_postfix):
    try:
        global fout
        name_data = compute_name_score(name_postfix)
        write_to_file(fout, name_data)
    except Exception as e:
        print 'error, ', e, name_postfix

def get_full_name(name_postfix):
    return "%s%s" % ((user_config.setting["name_prefix"]), name_postfix)


lock = threading.Lock()
def write_to_file(fout, name_data):
    lock.acquire()
    global curr_idx, all_count
    curr_idx += 1
    print "%d/%d" % (curr_idx, all_count),
    print "\t".join((name_data['full_name'],
                     "姓名八字评分=" + str(name_data['bazi_score']),
                     "姓名五格评分=" + str(name_data['wuge_score']),
                     "总分=" + str(name_data['total_score'])
                     ))
    fout.write(name_data['full_name'] + "\t" 
               + str(name_data['bazi_score']) + "\t" 
               + str(name_data['wuge_score']) + "\t" 
               + str(name_data['total_score']) + "\n")
    lock.release()

def process(output_fpath):
    """计算并且将结果输出到文件
    """
    global fout
    # 输出文件路径
    fout = open(output_fpath, "w")
    # 获得所有可用的名字列表
    all_name_postfixs = get_name_postfixs()
    
    global all_count
    all_count = len(all_name_postfixs)
     
    pool = threadpool.ThreadPool(50) 
    requests = threadpool.makeRequests(compute_and_writefile, all_name_postfixs) 
    [pool.putRequest(req) for req in requests] 
    pool.wait()  

    fout.flush()
    fout.close()


if __name__ == "__main__":
    print "begin................................"
    output_fpath = "./outputs/%s" % user_config.setting["output_fname"]
    process(output_fpath)
    print "over................................"

