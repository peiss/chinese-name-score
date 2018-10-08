# chinese-name-score

中文自动起名打分程序。

### 如果大家对程序不感兴趣，只想得到宝宝名称列表，可以QQ联系我693609645，收费60元（如果觉得贵就算了，我没时间搞这个^_^）

## 运行方式：
*注意，由于目标网站的编码是GB18030，所以本项目的代码也是GB18030，在导入到pychar时默认是UTF8编码，需要先修改一下*


1. 在/chinese-name-score/main/user_config.py进行运行配置
2. 执行脚本：/chinese-name-score/main/get_name_score.py


## 代码依赖的Python模块：
1. BeautifulSoup4 https://www.crummy.com/software/BeautifulSoup/bs4/doc/#
2. 自带的urllib2、urllib2等模块


按八字和五格做名字测试，不一定真的就是准，不过它也是中国几千年的文化传承，宁可信其有不可信其无，只要测试出来分数不太低就行了。
本代码的博客文章地址：http://www.crazyant.net/2076.html
