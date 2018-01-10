#language: zh-CN
功能:修改密码
        场景大纲:点击修改密码
                假设 我在"<page>"页,直到"<keyword>"出现     
                当   我点击"<button>"    
                那么 我应该看到"<title>"出现
                 例子:
          | page |keyword|button|title|
          | 我的信息    |我的信息|修改密码 |原始密码|
		  

		  

        场景大纲:修改密码
                假设 我在"<page>"页,直到"<keyword>"出现 
                当  我在第<n>个输入框输入"<keywords1>"
               并且 我在第<n1>个输入框输入"<keywords2>"
                并且 我在第<n2>个输入框输入"<keywords3>"
                并且 我点击"<button>"
               那么  我应该看到"<title>"出现

 
                 例子:
          | page |keyword|n|n1|n2|keywords1|keywords2|keywords3|button|title|
          | 修改密码    |修改密码|1|2|3|Qq123123|Qq123456|Qq123456|确定|原始密码|
		  
		  
		  
		场景大纲:修改密码页返回
                假设 我在"<page>"页,直到"<keyword>"出现
               当 我点击回退
                 那么 我应该看到"<title>"出现  
                 
                 
                 例子:
          | page |keyword|title|
          | 修改密码   |修改密码 |我的信息| 
		  
        场景大纲:退出登录
                假设 我在"<page>"页,直到"<keyword>"出现
                当   我点击"<button1>"
                并且  我点击"<button2>"   
                那么 我应该看到"<title>"出现   
                                              
            
                 例子:
          | page | keyword |button1|button2|title|
          | 我的信息   | 退出登录     |退出登录          |确认退出|登录|

        场景大纲:手机管车登录
                假设 我在"<page>"页,直到"<keyword>"出现
                当  页面出现输入框,我输入"<account>"和"<password>"          
                并且    我点击"<button>"
                那么 我应该看到"<title>"出现
                 例子:
          | page | keyword | account | password |button|title|
          | 登录         | 登录                   |  lifucai| Qq123456 |登录     |手机管车|



        场景大纲:到达我的手机管车页面
                假设 我在"<page>"页,直到"<keyword>"出现
                当   我点击"<button>"                   
                那么 我应该看到"<title>"出现
                 例子:
          | page | keyword |button|title|
          | 管车首页   | 手机管车      |我的            |我的手机管车|		

        场景大纲:到达我的信息页面
                假设 我在"<page>"页,直到"<keyword>"出现
                当   我点击"<button>"                   
                那么 我应该看到"<title>"出现
                 例子:
          | page | keyword |button|title|
          | 我的手机管车  | 我的手机管车      |我的信息      |我的信息  |

		  场景大纲:点击修改密码
                假设 我在"<page>"页,直到"<keyword>"出现     
                当   我点击"<button>"    
                那么 我应该看到"<title>"出现
                 例子:
          | page |keyword|button|title|
          | 我的信息    |修改密码 |修改密码 |原始密码|	

        场景大纲:修改密码
                假设 我在"<page>"页,直到"<keyword>"出现 
                当  我在第<n>个输入框输入"<keywords1>"
               并且 我在第<n1>个输入框输入"<keywords2>"
                并且 我在第<n2>个输入框输入"<keywords3>"
                并且 我点击"<button>"
               那么  我应该看到"<title>"出现

 
                 例子:
          | page |keyword|n|n1|n2|keywords1|keywords2|keywords3|button|title|
          | 修改密码    |修改密码|1|2|3|Qq123456|Qq123123|Qq123123|确定|原始密码|

        场景大纲:返回至我的信息页面
                假设 我在"<page>"页,直到"<keyword>"出现
               当 我点击回退
                 那么 我应该看到"<title>"出现  
                 
                 
                 例子:
          | page |keyword|title|
          | 修改密码   |修改密码 |我的信息| 
          		  