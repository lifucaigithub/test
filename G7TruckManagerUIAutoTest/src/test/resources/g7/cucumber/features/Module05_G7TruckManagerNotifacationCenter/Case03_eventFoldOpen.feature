#language: zh-CN
功能:事件折叠和展开
           场景大纲:查看事件折叠
                假设 我在"<page>"页,直到"<keyword>"出现
                当 我等待<time>秒
                当   我点击"<button>"                   
                那么 我应该看到"<title>"出现
                 例子:
          | page | keyword |time|button|title|
          |行车事件   | 成O12345 |5000 |成O12345   |展开 |
          
         场景大纲:展开事件
                假设 我在"<page>"页,直到"<keyword>"出现
                当 我等待<time>秒
                当   我点击"<button>"   
                当 我等待<time1>秒                
                那么 我应该看到"<title>"出现
                 例子:
          | page | keyword |time|button|time1|title|
          |成O12345   |展开 |5000|展开 |5000|收起|
          
          场景大纲:返回通知中心页面
                假设 我在"<page>"页,直到"<keyword>"出现
                当   我点击回退          
                那么 我应该看到"<title>"出现
                 例子:
          | page | keyword |title|
          |成O12345    |收起  |行车事件 |