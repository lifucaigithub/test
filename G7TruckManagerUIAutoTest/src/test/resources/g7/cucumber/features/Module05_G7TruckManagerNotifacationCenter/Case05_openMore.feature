#language: zh-CN
功能:展开更多
	场景大纲:返回通知中心页面	
	    当 我等待<time>秒              
	                当   我点击back键  	
	                并且    我点击back键                     
	                
	                当 我切换到Native
	                那么 我应该看到"<title>"出现
	                 例子:
	        |time |title|
	        |20000|更多 |
           场景大纲:展开更多按钮
                假设 我在"<page>"页,直到"<keyword>"出现
                当   我点击"<button>"                              
                那么 我应该看到弹出层出现
                例子:
          | page | keyword |button|
          |车辆列表   | 更多 |更多 |
          
      场景大纲:回到通知中心
             
                当   我点击back键                            
                那么 我应该看到"<title>"出现
                例子:
          |title|
         |离开test|
         |通知中心 |
         
   场景大纲:退出登录     
                当    我点击"<button>"
                那么 我应该看到"<title>"出现
                例子:
        |button   |title|
        |我的 |我的手机管车|
        |我的信息 |我的信息|
        |退出登录|确认退出|
        |确认退出|登录|   
          
     