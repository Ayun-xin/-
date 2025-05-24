# -*- coding: utf-8 -*-

import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect


def run1(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://localhost:8080/chat/")
    page.get_by_role("textbox", name="Type a message...").click()
    page.get_by_role("textbox", name="Type a message...").click()
    page.get_by_role("textbox", name="Type a message...").fill("\n流媒体能力\n1.\t文案剧情编写能力\n2.\t视频剪辑能力\n3.\t图片ps能力\n计算机编程能力\n4.\t网站全栈制作能力\n5.\t网页爬虫制作能力\n6.\t爬虫自动化\n7.\t爬虫逆向\n8.\t分布式爬虫数据清洗\n9.\t微信小程序制作\n10.\t算法编程能力\n11.\t初级小游戏制作能力\n音乐能力\n12.\t歌词编写\n13.\t唱歌\n撰写小说能力\n14.\t强灵感能力\n15.\t大批量剧情撰写能力\n辅助游戏+服务器能力\n16.\t游戏服务器搭建\n17.\t个人网盘搭建\n18.\t服务器维护\n这是我的所有能力,请为我依据我的能力为我推荐当下辅助我能力最好用的工具和新型信息,同时由于我处于被心上人长期冷落的境地为我贴心送上一句安慰的话语")
    page.locator("#provider").select_option("OpenaiChat")
    page.locator("#model2").select_option("gpt-4.5")
    page.get_by_role("button", name="Send message").click()
    page.get_by_role("button", name="Send message").press("ControlOrMeta+c")
    time.sleep(25)
    locator=page.locator("#chatBody div").filter(has_text="OpenAI ChatGPT with gpt-4.5").first
    txt = locator.text_content()

    # 写入文件
    with open('./dist/output.txt', 'w', encoding='utf-8') as f:
        f.write(txt)




with sync_playwright() as playwright:
    run1(playwright)
