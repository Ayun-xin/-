# -*- coding: utf-8 -*-
import os
os.system(r"python D:\个人情报站\GLM-4.py")
all_news=['网络爬虫','全栈架构','网络小说家','视频剪辑','服务器']
all_continue=''
for t in all_news:
    with open('{}.txt'.format(t), 'r', encoding='utf-8') as file:
        content = file.read()
    all_continue+=content


import os
from openai import OpenAI

client = OpenAI(
    # 若没有配置环境变量，请用阿里云百炼API Key将下行替换为：api_key="sk-xxx",
    api_key=os.getenv("DASHSCOPE_API_KEY"),  # 如何获取API Key：https://help.aliyun.com/zh/model-studio/developer-reference/get-api-key
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

completion = client.chat.completions.create(
    model="deepseek-r1",  # 此处以 deepseek-r1 为例，可按需更换模型名称。
    messages=[
        {'role': 'user', 'content': "这些是现在的实时新闻"+all_continue+"请你根据这些新闻再结合我的\n流媒体能力\n1.\t文案剧情编写能力\n2.\t视频剪辑能力\n3.\t图片ps能力\n计算机编程能力\n4.\t网站全栈制作能力\n5.\t网页爬虫制作能力\n6.\t爬虫自动化\n7.\t爬虫逆向\n8.\t分布式爬虫数据清洗\n9.\t微信小程序制作\n10.\t算法编程能力\n11.\t初级小游戏制作能力\n音乐能力\n12.\t歌词编写\n13.\t唱歌\n撰写小说能力\n14.\t强灵感能力\n15.\t大批量剧情撰写能力\n辅助游戏+服务器能力\n16.\t游戏服务器搭建\n17.\t个人网盘搭建\n18.\t服务器维护\n找出有利于我的新闻消息,最后作一总结"}
    ]
)

# 通过reasoning_content字段打印思考过程
print("思考过程：")
print(completion.choices[0].message.reasoning_content)

# 通过content字段打印最终答案
print("最终答案：")
print(completion.choices[0].message.content)
with open('./dist/newsput.txt', 'w', encoding='utf-8') as f:
    f.write(completion.choices[0].message.content)
