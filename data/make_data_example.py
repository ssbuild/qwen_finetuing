# -*- coding: utf-8 -*-
# @Time    : 2023/2/24 12:50


import json

x0 = {
    "id": 0, "paragraph": [
        {
            "role": "system",
            "q": "You are a helpful assistant.",
            "a": ""
        },
        {
            "role": "user",
            "q": "现在给我画个五彩斑斓的黑",
            "tools": """ 
[
  {
    "name_for_human": "夸克搜索",
    "name_for_model": "quark_search",
    "description_for_model": "夸克搜索是一个通用搜索引擎，可用于访问互联网、查询百科知识、了解时事新闻等。",
    "parameters": [
      {
        "name": "search_query",
        "description": "搜索关键词或短语",
        "required": true,
        "schema": {
          "type": "string"
        }
      }
    ]
  },
  {
    "name_for_human": "通义万相",
    "name_for_model": "image_gen",
    "description_for_model": "通义万相是一个AI绘画（图像生成）服务，输入文本描述，返回根据文本作画得到的图片的URL",
    "parameters": [
      {
        "name": "query",
        "description": "中文关键词，描述了希望图像具有什么内容",
        "required": true,
        "schema": {
          "type": "string"
        }
      }
    ]
  }
]
""",
            "a": '''
Thought: 我应该使用通义万相API来生成一张五彩斑斓的黑的图片。
Action: image_gen
Action Input: {"query": "五彩斑斓的黑"}
            '''
        },
        {
            "role": 'observation',
            "q": '''
{"status_code": 200, "request_id": "3d894da2-0e26-9b7c-bd90-102e5250ae03", "code": null, "message": "", "output": {"task_id": "2befaa09-a8b3-4740-ada9-4d00c2758b05", "task_status": "SUCCEEDED", "results": [{"url": "https://dashscope-result-sh.oss-cn-shanghai.aliyuncs.com/1e5e2015/20230801/1509/6b26bb83-469e-4c70-bff4-a9edd1e584f3-1.png"}], "task_metrics": {"TOTAL": 1, "SUCCEEDED": 1, "FAILED": 0}}, "usage": {"image_count": 1}}
''',
            "a": '''
Thought: 我已经成功使用通义万相API生成了一张五彩斑斓的黑的图片。
Final Answer: 我已经成功使用通义万相API生成了一张五彩斑斓的黑的图片https://dashscope-result-sh.oss-cn-shanghai.aliyuncs.com/1e5e2015/20230801/1509/6b26bb83-469e-4c70-bff4-a9edd1e584f3-1.png。
            '''
        }
    ]
}

x1 = {
    "id": 0, "paragraph": [
    {
        "role": "system",
        "q": "You are a helpful assistant.",
        "a": ""
    },
    {
        "q": "从南京到上海的路线",
        "a": "\n".join([
            "你好，南京到上海的路线如下：",
            "1. 南京到上海，可以乘坐南京地铁1号线，在南京站乘坐轨道交通1号线。",
            "2. 南京到浦东机场，可以搭乘上海地铁1号，在陆家嘴站乘坐地铁1线，在浦东国际机场站乘坐机场快线，前往上海浦东国际机场。",
            "3. 上海到南京，可以换乘上海地铁2号线，从南京站换乘地铁2线，再从南京南站换乘地铁1路，然后到达上海站"
        ])
    }
    ]
}

x2 = {"id": 0, "paragraph": [
    {
        "role": "system",
        "q": "You are a helpful assistant.",
        "a": ""
    },
    {
        "q": "写一个诗歌，关于冬天",
        "a": "\n".join([
            "冬夜寂静冷，",
             "云在天边飘，", "冰封白雪上， ", "寒冷像一场雪。",
             " ",
             "雪花融化成冰，",
             "像那雪花飘洒，",
             "在寒冷的冬天，",
             "感受春天的喜悦。",
             " 冬日里，",
             "风雪渐消，",
             "一片寂静，",
             "把快乐和温暖带回家。"
        ])
    }
    ]
}

x3 = {"id": 0, "paragraph": [
    {
        "role": "system",
        "q": "You are a helpful assistant.",
        "a": ""
    },
    {
        "q": "晚上睡不着应该怎么办",
        "a": "\n".join([
            "晚上睡不着可能会让你感到焦虑或不舒服,但以下是一些可以帮助你入睡的方法:",
            "",
            "1. 制定规律的睡眠时间表:保持规律的睡眠时间表可以帮助你建立健康的睡眠习惯,使你更容易入睡。尽量在每天的相同时间上床,并在同一时间起床。",
            "2. 创造一个舒适的睡眠环境:确保睡眠环境舒适,安静,黑暗且温度适宜。可以使用舒适的床上用品,并保持房间通风。",
            "3. 放松身心:在睡前做些放松的活动,例如泡个热水澡,听些轻柔的音乐,阅读一些有趣的书籍等,有助于缓解紧张和焦虑,使你更容易入睡。",
            "4. 避免饮用含有咖啡因的饮料:咖啡因是一种刺激性物质,会影响你的睡眠质量。尽量避免在睡前饮用含有咖啡因的饮料,例如咖啡,茶和可乐。",
            "5. 避免在床上做与睡眠无关的事情:在床上做些与睡眠无关的事情,例如看电影,玩游戏或工作等,可能会干扰你的睡眠。",
            "6. 尝试呼吸技巧:深呼吸是一种放松技巧,可以帮助你缓解紧张和焦虑,使你更容易入睡。试着慢慢吸气,保持几秒钟,然后缓慢呼气。",
            "",
            "如果这些方法无法帮助你入睡,你可以考虑咨询医生或睡眠专家,寻求进一步的建议。"
        ])
    }
    ]
}



x = [x0,x1,x2,x3]

with open('./finetune_train_examples.json',mode='w',encoding='utf-8',newline='\n') as f:
    index = 0
    for i in range(100):
        for j in range(len(x)):
            index += 1
            x[j]['id'] = index
            f.write(json.dumps(x[j],ensure_ascii=False) + '\n' )
