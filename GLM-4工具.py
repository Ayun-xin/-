# -*- coding: utf-8 -*-
all_news=['爬虫工具','网页前端后端工具','视频剪辑工具','音乐创作工具']
for t in all_news:
    from zhipuai import ZhipuAI

    client = ZhipuAI(api_key='')  # 填写您自己的APIKey

    response = client.web_search.web_search(
        search_engine="search-pro",
        search_query="最新的"+t
    )

    content = ''
    for i in range(10):
        content += response.search_result[i].content + '\n'
    with open('{}.txt'.format(t), 'w', encoding='utf-8') as f:
        f.write(content)

