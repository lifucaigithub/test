#language: zh-CN
功能:进入车辆追踪
	
           场景大纲:进入车辆追踪
                假设 我在"<page>"页,直到"<keyword>"出现
                当   我点击"<button>"  
                当 我等待<time>秒
                并且    我点击"<button1>"
                当         我切换到WebView 
                当         我等待<time1>秒   
                  当   我点击WebView"<button2>"   
                   当 我等待<time2>秒                   
                那么 我应该看到WebView"<title>"出现
                 例子:
          | page | keyword |button|time|button1|time1|button2|time2|title|
          |通知中心   | 行车事件   |川G987WU|5000 |离开test |10000|车辆追踪 |20000|川G987WU |