# 这是一个可以为你显示当下符合你能力的工具和对于你能力有利新闻的个人情报机构项目,立志于像情报机构一样为你时刻提供最新最好对你最有利的新闻和工具,让我们每天都可以跟着时代一起进步
# This is a personal intelligence project that can display tools and news that are currently suitable for your abilities and beneficial to you. It aims to provide you with the latest and best news and tools, just like an intelligence agency, so that we can all advance with the times every day.
首先你需要把文件像图片里一样放好,我们的项目里需要的仅有AI.PY,新闻热点AI个性化聚焦.PY,RUN.PY,新闻界面.py,界面.py这五个文件,而图片中其他的文件我们不需要理会

First, you need to arrange the files as shown in the picture. For our project, we only need the following five files: AI.py, News Hotspot AI Personalized Focus.py, RUN.py, News Interface.py, and Interface.py. You can ignore the other files in the picture.
!![image](https://github.com/user-attachments/assets/ba66e379-298c-48f8-9b9b-9ce9430dab66)

注意,在AI.py和新闻热点AI个性化聚焦.PY文件内的messages=[{'role': 'user', 'content':''}处也就是红框content后面填写你的能力这样它才能关于有你的能力,如果你也和我一样遭遇了被冷落的待遇别忘了在AI.PY中的conntent最后附上你的情感状况,让AI结合你的能力好好安慰一下你

Please note that in the file AI.News Hotspot AI.py and Personalized Focus.PY, you need to fill in your abilities in the content field of the messages list, like this: messages=[{'role': 'user', 'content':'Your abilities here'}]. This will allow the AI to understand your capabilities. If you, like me, have experienced being neglected, don't forget to also include your emotional state at the end of the content in the AI.PY file, so that the AI can take your abilities and emotions into account and offer you some comfort.
![image](https://github.com/user-attachments/assets/fd7fc6de-2f68-433c-bfe5-be462c0952e8)
还需注意的是在run.py文件中的红框位置处需要填写正确的文件路径

Also, please note that you need to fill in the correct file path at the red框 position in the run.py file.
![image](https://github.com/user-attachments/assets/b77f221f-5430-4b0a-bee8-342399dd2f03)
接下来你需要用python中的打包文件为exe的功能,将RUN.PY,新闻界面.py,界面.py这三个文件全部打包为exe文件,然后就出现了build和dist文件夹,在dist文件夹中你需要创建两个空的txt文件,如图片所示

Next, you need to use the "package files into exe" feature in Python to convert RUN.PY, News Interface.py, and Interface.py into executable files. This will create build and dist folders. In the dist folder, you need to create two empty txt files as shown in the picture.
![image](https://github.com/user-attachments/assets/3b2d7196-e5fb-47a3-a7f4-8059fe086fad)
last_run.txt文件会自动生成无需理会,然后将这三个exe程序的快捷方式全都拖放到我们的开机启动文件夹内

The last_run.txt file will be generated automatically, so you don't need to worry about it. Then, drag the shortcuts of all three exe programs into our startup folder.
![image](https://github.com/user-attachments/assets/dcd1889f-5218-4ce2-b001-0f305be3b9df)
就像这样
然后我们的项目就完成了!run文件在开机后检查是不是离上次运行过了24小时,如果是它将自动运行AI.py为我们抓取最新的与我们能力相关的对我们有利的新闻消息,如果是过了七天它则会为我们更新与我们能力相关的最新工具的消息
最后的成果就是这样

Here’s how it looks:
And that’s it, our project is complete! The RUN file checks after startup if it has been more than 24 hours since the last run. If so, it will automatically run AI.py to fetch the latest news that is relevant to our capabilities and beneficial to us. If it has been seven days, it will update us with the latest information about tools related to our capabilities.
This is the final result.
![image](https://github.com/user-attachments/assets/130c14f4-ae1b-403d-abcb-590ab146c369)
接下来我也会不断的完善它,让他可以有更多和更加自动化的ai情报服务

Next, I will continuously improve it, enabling it to provide more and increasingly automated AI intelligence services.
