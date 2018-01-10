#language: zh-CN
功能:查看加油事件列表
         场景大纲:加油事件列表         
                当 我点击事件加油
                当       我等待<time>秒 
                那么 我应该看到"<title>"出现
                 例子:
        | time | title  |
         | 20000  | 加油 |
         
     场景大纲:进入事件定位页面     
                当 通过AccessibilityId点击列表"<name>"
                当       我等待<time>秒 
                那么 我应该看到"<title>"出现
                 例子:
         |name | time | title  |
         |江西省宜春市高安市祥符镇兰东| 10000  | 事件定位 |
         
         场景大纲:返回车辆详情页
                当	我等待<time>秒 
                当   我点击back键               
                  那么   我应该看到"<title>"出现
                 例子:
          |time|title|
          |10000|加油|
          |10000|油箱事件|

              
          