#language: zh-CN
功能:登录未订阅账号
			场景大纲:登录未订阅账号
			假设 我在"<page>"页,直到"<keyword>"出现
			当		页面出现输入框,我输入"<account>"和"<password>"   
			并且		我点击"<button>"             
			那么		我应该看到"<title>"出现
			例子:
          |page|keyword |account |password|button|title|
          |登录|登录		|huoche1|Qq123123|登录     |您是否需要开通车辆通知|
          
 	场景大纲:关闭提示框
			并且		我点击"<button>"
			那么		我应该看到"<title>"出现
			例子:
			|button|title|
			|取消|手机管车|
          
	场景大纲:跳转到我的信息页面退出登录         
                当	我点击"<button>"
                那么 我应该看到"<title>"出现           
                 例子:
           |button|title|
           |我的	|我的手机管车|
           |我的信息|我的信息|
           |退出登录|确认退出|
           |确认退出|登录|	        
          