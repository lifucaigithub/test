#language:zh-CN
功能:我要购买
        
      场景大纲:切换到我的页面并进入G7商城页面
                假设 我在"<page>"页,直到"<keyword>"出现          
                当     我点击"<button>"
                并且     我等待<time>秒
                那么 我应该看到"<title>"出现
                例子:
          | page      |keyword    |button|time|title|
          | 我的手机管车  |我的手机管车     |我要购买    | 10000  |G7商城|

          
     场景大纲:从商城返回我的页面
                假设 我在"<page>"页,直到"<keyword>"出现          
                当    我点击back键
                那么 我应该看到"<title>"出现
                例子:
          | page    |keyword      |title|
          | G7商城       |G7商城                   |我的手机管车|
    
          
          
         
   
          
          