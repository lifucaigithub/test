#language: zh-CN
功能:进入油量曲线
        场景大纲:进入我的车队页面
                假设 我在"<page>"页,直到"<keyword>"出现
                当   我点击"<button>"                   
                那么 我应该看到"<title>"出现
                 例子:
          | page | keyword |button|title|
          | 管车首页   | 我的车队 |我的车队  |我的车队|
 场景大纲:关闭车辆列表引导页
              当	我等待<time>秒
                当   划屏<n>次,并点击"<name>"          
                那么 我应该看到WebView"<title>"出现
                 例子:
           |time| n | name | title |
          |10000|4|我知道了| 在线车辆 |
          
        场景大纲:我的车队页面，选择车辆
           
              当	我切换到Native  
               当	我等待<time>秒          
                并且   我点击"<carno>"
                那么 我应该看到"<title>"出现
                 例子:
          |time| carno | title |
          |10000| 赣HK3394   | 赣HK3394 |
          
    场景大纲:关闭车辆详情引导页
              
               当	我等待<time>秒 
                当   车辆详情划屏<n>次,并点击"<name>"           
                那么 我应该看到WebView"<title>"出现
                 例子:
           |time| n | name | title |
          |20000|1|guide--alias__btn| 行车电脑数据 |
          
        场景大纲:进入油量曲线
             当	我切换到Native  
              当	我等待<time>秒     
                当   向上滑动<d>次,直到"<name>"出现    
                当	我切换到WebView 
                 当	我等待<time1>秒                
                并且   我点击WebView"<button>" 
                当	我切换到Native                 
                那么   我应该看到"<title>"出现
                 例子:
          |time|   d   |  name |time1| button | title |
          |10000| 1     |油量曲线  |10000|油量曲线  |油量曲线|
    
          
         
          