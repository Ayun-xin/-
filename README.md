# 这是一个可以为你显示当下符合你能力的工具和对于你能力有利新闻的个人情报机构项目,立志于像情报机构一样为你时刻提供最新最好对你最有利的新闻和工具,让我们每天都可以跟着时代一起进步
# This is a personal intelligence project that can display tools and news that are currently suitable for your abilities and beneficial to you. It aims to provide you with the latest and best news and tools, just like an intelligence agency, so that we can all advance with the times every day.
首先你需要把文件夹像图片里一样放好,我们的项目里需要的仅有AI.PY,AI数据.PY,RUN.PY,新闻界面.py,界面.py这五个文件,而图片中其他的文件我们不需要理会![image](https://github.com/user-attachments/assets/05d39e40-d21f-4842-a5e8-e1af52c89a7e)
注意,在AI.PY和AI数据.PY文件内的messages=[{'role': 'user', 'content':''}处![image](https://github.com/user-attachments/assets/fd7fc6de-2f68-433c-bfe5-be462c0952e8)
也就是红框content后面填写你的能力这样它才能关于有你的能力,如果你也和我一样遭遇了被冷落的待遇别忘了在AI.PY中的conntent最后附上你的情感状况,让AI结合你的能力好好安慰一些你
接下来你需要用python中的打包文件为exe的功能,将RUN.PY,新闻界面.py,界面.py这三个文件全部打包为exe文件,然后就出现了build和dist文件夹,在dist文件夹中你需要创建两个空的txt文件,如图片所示![image](https://github.com/user-attachments/assets/3b2d7196-e5fb-47a3-a7f4-8059fe086fad)last_run.txt文件会自动生成无需理会,然后将这三个exe程序的快捷方式全都拖放到我们的开机启动文件夹内![image](https://github.com/user-attachments/assets/dcd1889f-5218-4ce2-b001-0f305be3b9df)就像这样
然后我们的项目就完成了!run文件在开机后检查是不是离上次运行过了24小时,如果是它将自动运行AI.py为我们抓取最新的与我们能力相关的对我们有利的新闻消息,如果是过了七天它则会为我们更新与我们能力相关的最新工具的消息
最后的成果就是这样![image](https://github.com/user-attachments/assets/130c14f4-ae1b-403d-abcb-590ab146c369)
再接下来我也会不断的完善它,让他可以有更多和更加自动化的ai情报服务
