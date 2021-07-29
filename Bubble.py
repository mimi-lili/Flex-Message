# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 18:47:09 2020

@author: LIN
"""
#一個BUBBLE的字典
#用來製作Flex Message
Bubble_Type_1 =     {
  "type": "bubble",
  "hero": {
    "type": "box",
    "layout": "vertical",
    "contents": []
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "課程名稱",
        "weight": "bold",
        "size": "xl",
        "margin": "md",
        "align": "start"
      },
      {
        "type": "text",
        "text": "授課老師",
        "align": "start"
      },
      {
        "type": "text",
        "text": "上課時間地點",
        "align": "start"
      }
    ],
    "backgroundColor": "#e6f2ff"
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "button",
        "action": {
          "type": "postback",
          "label": "加入我的課表",
          "data": "加入我的課表"
        }
      }
    ]
  }
}

Bubble_Type_2 =     {
  "type": "bubble",
  "hero": {
    "type": "box",
    "layout": "vertical",
    "contents": []
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "課程名稱",
        "weight": "bold",
        "size": "xl",
        "margin": "md",
        "align": "start"
      },
      {
        "type": "text",
        "text": "授課老師",
        "align": "start"
      },
      {
        "type": "text",
        "text": "上課時間地點1",
        "align": "start"
      },
      {
        "type": "text",
        "text": "上課時間地點2"
      }
    ],
    "backgroundColor": "#e6f2ff"
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "button",
        "action": {
          "type": "postback",
          "label": "加入我的課表",
          "data": "加入我的課表"
        }
      }
    ]
  }
}

Bubble_Type_3 =     {
  "type": "bubble",
  "hero": {
    "type": "box",
    "layout": "vertical",
    "contents": []
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "課程名稱",
        "weight": "bold",
        "size": "xl",
        "margin": "md",
        "align": "start"
      },
      {
        "type": "text",
        "text": "授課老師",
        "align": "start"
      },
      {
        "type": "text",
        "text": "上課時間地點1",
        "align": "start"
      },
      {
        "type": "text",
        "text": "上課時間地點2"
      },
      {
        "type": "text",
        "text": "上課時間地點3"
      }
    ],
    "backgroundColor": "#e6f2ff"
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "button",
        "action": {
          "type": "postback",
          "label": "加入我的課表",
          "data": "加入我的課表"
        }
      }
    ]
  }
}
