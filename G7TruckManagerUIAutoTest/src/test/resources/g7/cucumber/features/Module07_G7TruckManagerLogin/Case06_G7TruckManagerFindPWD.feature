#language: zh-CN
功能:找回密码
        场景大纲:点击无法登录
                假设 我在"<page>"页,直到"<keyword>"出现
                当		我点击"<button>"
                那么	我应该看到"<title>"出现
               
                 例子:
				|page|keyword |button|title|
				|登录|登录		|无法登录？|找回密码|
				
	场景大纲:点击找回密码          
                当		我点击"<button>"
                那么	我应该看到"<title>"出现
               
                 例子:
		|button	|title|
		|找回密码|找回密码|
          
        场景大纲:找回密码-未绑定手机号
                假设 我在"<page>"页,直到"<keyword>"出现
                当		我在第<n>个输入框输入"<param>"
                并且		我点击"<button>"
                那么	我应该看到"<title>"出现
                当		我点击"<button1>"
                那么	我应该看到"<title1>"出现
                 例子:
          |page		|keyword |n|param|button|title|button1|title1|
          |找回密码|找回密码|1|tang123	|获取验证码	|提醒|取消| 找回密码|  
           
          
       场景大纲:找回密码-信息有误
                假设 我在"<page>"页,直到"<keyword>"出现
                当		我在第<n>个输入框输入"<param>"
                并且	我点击"<button>"
                那么	我应该看到"<title>"出现
                当		我点击"<button1>"
                那么	我应该看到"<title1>"出现
                 例子:
          |page		|keyword |n|param|button|title|button1|title1|
          |找回密码|找回密码|1|123	|获取验证码	|提醒|我知道了| 找回密码|   
          
	   场景大纲:找回密码-回到登录
	       假设 我在"<page>"页,直到"<keyword>"出现      
	                当	我点击回退  
	                那么 我应该看到"<title>"出现
	        例子:
	      |page		|keyword |title|
	      |找回密码|获取验证码|登录|
	       
	      
	   场景大纲:找回密码-回到选择登录	           
	                当		我点击back键             
	                那么	我应该看到"<title>"出现
	        例子:
	      |title|
	      |现在去购买|   

          