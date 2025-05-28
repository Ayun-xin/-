# 这是独属于你的中情局,用他们每天从世界上收集对你最有用的信息吧!让今天的自己都比昨天的自己更好,我通过GLM-4提供的接口来实现网络搜索实时新闻,然后通过deepseek-R1接口来综合总结对你最有用的消息,最后在每天你打开电脑时就会弹出两个窗口,里面都是最即时最对你有用大事件哦

# This is your very own CIA, using their daily collection of information from around the world to bring you the most useful insights! Make today’s you better than yesterday’s you. I will leverage the GLM-4 interface to conduct real-time web searches for news, and then utilize the DeepSeek-R1 interface to synthesize and summarize the most valuable information for you. Every morning when you turn on your computer, two windows will pop up, filled with the most up-to-the-minute and relevant major events.
可以直接观看我发布的视频来了解这个项目:https://www.bilibili.com/video/BV1cCj2ztEy2/?spm_id_from=333.1387.favlist.content.click&vd_source=e77e017189e0b6249e9f3fb9193a6c89


一.配置前的准备工作:

一.Preparation

1.首先你得获得阿里云百炼模型和GLM-4的APIKAY,这是阿里云接口的网址:https://help.aliyun.com/zh/model-studio/developer-reference/get-api-key,这是GLM-4接口的网址:https://bailian.console.aliyun.com/?tab=model#/api-key

1.you need to obtain the API KEY for the Aliyun Bailian Model and GLM-4. Here is the link to the Aliyun interface: https://help.aliyun.com/zh/model-studio/developer-reference/get-api-key, and here is the link to the GLM-4 interface: https://bailian.console.aliyun.com/?tab=model#/api-key

2.你得确保在这四个文件中被我标注为红框的地方都是你的能力

2.You need to ensure that the areas marked with red boxes in these four documents all reflect your capabilities.
![image](https://github.com/user-attachments/assets/e455de5a-b8b8-4059-970c-19ab0ab67f33)
![image](https://github.com/user-attachments/assets/5771f5a8-67a4-4a46-b653-6cc85e31a458)
![image](https://github.com/user-attachments/assets/1822f904-092a-46bb-826b-c3a07bd2e51d)
![image](https://github.com/user-attachments/assets/8f35f591-71e7-4e52-8798-b570077ba2c1)
请确保你在第3,4个文件上方的红框处填写的和1,2个文件中红框处填写的一致

Please ensure that the information you fill in the red boxes above the 3rd and 4th documents is consistent with what you filled in the red boxes in the 1st and 2nd documents.

二.正式部署开始:

二.real start:

将所有文件都先放在一起

Put all the files together first

![image](https://github.com/user-attachments/assets/878da9a0-2016-4e2d-b219-773e3c951b7f)

请你将run.py,新闻界面.py,界面.py,三个文件用pyinstaller打包为exe程序,newsput.txt,output.txt都得新建后放在dist文件夹内

Please package the run.py, news_interface.py, and interface.py files into exe programs using pyinstaller, and create newsput.txt and output.txt files and place them in the dist folder.

![image](https://github.com/user-attachments/assets/3b2d7196-e5fb-47a3-a7f4-8059fe086fad)

注意:run.exe得和几个AI文件靠在一起

Note: run.exe should be placed close to the AI files.

![image](https://github.com/user-attachments/assets/9d3fc367-d846-4f94-9b33-ab9204db5965)

last_run.txt文件会自动生成无需理会,然后生成这三个exe程序的快捷方式,将他们全都拖放到我们的开机启动文件夹内

The last_run.txt file will be generated automatically, so you don't need to worry about it. Then, drag the shortcuts of all three exe programs into our startup folder.
![image](https://github.com/user-attachments/assets/dcd1889f-5218-4ce2-b001-0f305be3b9df)
就像这样
然后我们的项目就完成了!run文件在开机后检查是不是离上次运行过了24小时,如果是它将自动运行AI.py为我们抓取最新的与我们能力相关的对我们有利的新闻消息,如果是过了七天它则会为我们更新与我们能力相关的最新工具的消息
最后的成果就是这样

Here’s how it looks:
And that’s it, our project is complete! The RUN file checks after startup if it has been more than 24 hours since the last run. If so, it will automatically run AI.py to fetch the latest news that is relevant to our capabilities and beneficial to us. If it has been seven days, it will update us with the latest information about tools related to our capabilities.
This is the final result.
![image](https://github.com/user-attachments/assets/130c14f4-ae1b-403d-abcb-590ab146c369)
接下来我也会不断的完善它,让他可以有更多和更加自动化的情报服务,我的最终目标是实现更加完善的情报服务,我一定可以的!

Next, I will continuously improve it, enabling it to provide more and increasingly automated AI intelligence services.
