#language: zh-CN
功能:退出登录
        场景大纲:跳转到我的信息页面         
                当	我点击"<button>"
                那么 我应该看到"<title>"出现           
                 例子:
           |button|title|
           |我的	|我的手机管车|
           |我的信息|我的信息|
           |退出登录|确认退出|
           |确认退出|登录|
	  
  场景大纲:再次登录账号检查密码勾选
                假设 我在"<page>"页,直到"<keyword>"出现            
                 那么 元素"<button>"已勾选
                 例子:	
          |page|keyword |button|
          |登录|登录		|记住密码|
          