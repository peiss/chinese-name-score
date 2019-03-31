# chinese-name-score

### 大家好，新增加Python3的简化版本，地址在：本代码的chinese-name-score/chinese-name-score/python3/
链接为：https://github.com/peiss/chinese-name-score/tree/master/chinese-name-score/python3
本代码的视频讲解（我的一套付费爬虫视频课程的其中一节）：https://www.iqiyi.com/v_19rsj1yvy8.html


### 以下为python2的默认版本的说明
中文自动起名打分程序。

## 运行方式：
*注意，由于目标网站的编码是GB18030，所以本项目的代码也是GB18030，在导入到pychar时默认是UTF8编码，需要先修改一下*


1. 在/chinese-name-score/main/user_config.py进行运行配置
2. 执行脚本：/chinese-name-score/main/get_name_score.py


## 代码依赖的Python模块：
1. BeautifulSoup4 https://www.crummy.com/software/BeautifulSoup/bs4/doc/#
2. 自带的urllib2、urllib2等模块


按八字和五格做名字测试，不一定真的就是准，不过它也是中国几千年的文化传承，宁可信其有不可信其无，只要测试出来分数不太低就行了。
本代码的博客文章地址：http://www.crazyant.net/2076.html
