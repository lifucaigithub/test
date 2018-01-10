#language: zh-CN
功能:登录体验模式
        场景大纲:完成登录
                假设	我在"<page>"页,直到"<keyword>"出现
                当		我点击"<button>"     
                那么	我应该看到"<title>"出现
                并且		我点击"<button1>"
                那么	我应该看到"<title1>"出现
                
                 例子:
          |page|keyword |button|title	|button1|title1|
          |体验|体验		|体验	|我要体验|稍后再填写|手机管车|
          
          

        场景大纲:退出登录
                当	我点击"<button>"
                那么 我应该看到"<title>"出现           
                 例子:
           |button|title|
           |我的	|我的手机管车|
           |我的信息|我的信息|
           |退出登录|确认退出|
           |确认退出|登录|
          
         
          