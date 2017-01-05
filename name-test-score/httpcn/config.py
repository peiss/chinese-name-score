# coding:GB18030

"""
在这里写好配置
"""

setting = {}

# 计算TYPE，1表示全字，2表示限定中间的字，3表示限定结尾的字
setting["comp_type"] = [1, 2][1]
setting["middle_world"] = "家"

# 姓
setting["name_prefix"] = "王"
# 性别
setting["sex"] = ["男", "女"][1]
# 省份
setting["area_province"] = "北京"
# 区
setting["area_region"] = "海淀"
# 出生的年份
setting['year'] = "2017"
# 出生的月份
setting['month'] = "1"
# 出生的日子
setting['day'] = "4"
# 出生的小时
setting['hour'] = "5"
# 出生的分钟
setting['minute'] = "52"

# 种子文件输入地址
setting['input_fpath'] = "./dicts/names_girls_single_words_formal.txt"
# 结果产出文件地址
setting['output_fpath'] = "./outputs/names_girls_source_wxy.txt"



