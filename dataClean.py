import pandas as pd

df = pd.read_excel('测试题目/maoyan.xlsx',sheet_name = '猫眼电影数据')

# 定义一个函数来清理时间字符串
def clean_time_string(time_str):
    if isinstance(time_str, str): # 确保是字符串类型
        # 优先处理中文括号，因为英文括号可能在中文括号内部
        if '（' in time_str:
            time_str = time_str.split('（')[0]
        # 再处理英文括号
        if '(' in time_str:
            time_str = time_str.split('(')[0]
        if ' 00:' in time_str:
            time_str = time_str.split(' 00:')[0]
    return time_str

if 'Unnamed: 0' in df.columns:
    df = df.drop(columns=['Unnamed: 0'])
# 对 '上映时间' 列应用清理函数
# 假设 df.columns[2] 对应的是 '上映时间' 列
df['上映时间'] = df.loc[:, '上映时间'].apply(clean_time_string)

# 将清理后的列转换为日期时间类型
# 使用 format='mixed' 自动推断多种日期格式，errors='coerce' 将无法解析的转换为 NaT
df['上映时间'] = df['上映时间'].astype(str)

df.to_excel('测试题目/maoyan.xlsx',sheet_name = '猫眼电影数据',index = False)