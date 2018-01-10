#language: zh-CN
功能:进入事件定位页面
           场景大纲:进入事件定位
                假设 我在"<page>"页,直到"<keyword>"出现
                当 我等待<time>秒
                当   我点击"<button>"                   
                那么 我应该看到"<title>"出现
                 例子:
          | page | keyword|time |button|title|
          |川G987WU   | 离开test |5000 |离开test   |事件定位 |
          
         场景大纲:返回通知中心页面
                假设 我在"<page>"页,直到"<keyword>"出现
                当 我等待<time>秒
                当   我点击回退          
                并且    我点击回退
                那么 我应该看到"<title>"出现
                 例子:
          | page | keyword |time|title|
          |事件定位   |事件定位 |5000|行车事件 |