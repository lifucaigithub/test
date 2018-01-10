#language:zh-CN
功能:帮助
           
      场景大纲:切换到我的页面并进入帮助页面查看常见问题
                假设 我在"<page>"页,直到"<keyword>"出现          
                当     我点击"<button>"
                那么 我应该看到"<title>"出现
                例子:
          | page      |keyword    |button     |title|
          | 我的手机管车  |我的手机管车     |帮助                   |帮助|
          | 帮助                |常见问题            |常见问题            |常见问题|
          
          
   场景大纲:切换到我的页面并进入帮助页面查看常见问题
                假设 我在"<page>"页,直到"<keyword>"出现  
              当         我切换到WebView
                并且     我点击WebView"<button>"
                那么 我应该看到WebView"<title>"出现
                例子:
          | page      |keyword |button|title|
          | 常见问题         |常见问题      |忘记密码            |忘记密码 |
          
    场景大纲:从常见问题返回帮助页面                       
                当    我点击back键       
                那么 我应该看到WebView"<title>"出现
                例子:
          |title|
          |基础账户设置|
          
  场景大纲:从常见问题返回帮助页面                  
                当    我点击back键
                并且         我切换到Native
                那么 我应该看到"<title>"出现
                例子:
          |title|
          |使用说明|
          
    场景大纲:在使用说明页面滑动查看说明          
                当     我点击"<button>"
                那么 我应该看到"<title>"出现
                例子:
         |button|title|
         |使用说明|使用说明|
         
    场景大纲:从使用返回帮助页面            
                当    我点击back键
                那么 我应该看到"<title>"出现
                例子:
         |title|
         |常见问题|
         |我的手机管车|

   
          
          