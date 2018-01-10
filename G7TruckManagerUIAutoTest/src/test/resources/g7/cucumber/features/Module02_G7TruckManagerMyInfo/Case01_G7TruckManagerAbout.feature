#language:zh-CN
功能:关于页面
        场景大纲:完成登录
                假设 我在"<page>"页,直到"<keyword>"出现
                当  页面出现输入框,我输入"<account>"和"<password>"          
                并且    我点击"<button>"
                那么 我应该看到"<title>"出现
                 例子:
          | page   | keyword | account   | password|button |title|
          | 登录         | 登录            |lifucai| Qq123123  |登录         |手机管车|
     
     场景大纲:进入我的          
                          
                 当    我点击"<button>"
                那么 我应该看到"<title>"出现
                 例子:
         |button |title|
         |我的         |我的手机管车|
          
           场景大纲:滑动到页面直到关于出现
                假设 我在"<page>"页,直到"<keyword>"出现
                当  向上滑动<n>次,直到"<title>"出现         
                 例子:
          | page       | keyword| n|title| 
          | 我的手机管车     | 我的手机管车   |1 |关于|   
          
      场景大纲:进入关于页面
                假设 我在"<page>"页,直到"<keyword>"出现          
                当     我点击"<button>"
                那么 我应该看到"<title>"出现
                例子:
          | page      |keyword    |button     |title|
          | 我的手机管车  |我的手机管车     |关于                   |关于G7|
          | 关于G7     |关于G7      |联系我们            |帮助|
          | 帮助                |帮助                   |取消                   |关于G7|
          | 关于G7     |关于G7      |联系我们            |帮助|
          | 帮助    |帮助     |联系客服            |400 611 5656|
          
 

          
     场景大纲:从关于返回我的页面
                假设 我在"<page>"页,直到"<keyword>"出现          
                当    我点击back键
                那么 我应该看到"<title>"出现
                例子:
          | page    |keyword      |title|
          | 拨号页面     |400 611 5656 |关于G7|
          | 关于G7   |关于G7        |我的手机管车|
          
          
         
   
          
          