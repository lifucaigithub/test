#language: zh-CN
功能:进入单车通知详情
        场景大纲:完成登录
                假设 我在"<page>"页,直到"<keyword>"出现
                当  页面出现输入框,我输入"<account>"和"<password>"          
                并且    我点击"<button>"
                那么 我应该看到"<title>"出现
                例子:
          | page | keyword | account | password |button|title|
          | 登录   | 登录        |  mobileapitest  | Qq123456 |登录    |手机管车|
          
        场景大纲:到达通知中心
                假设 我在"<page>"页,直到"<keyword>"出现
                当   我点击"<button>"                   
                那么 我应该看到"<title>"出现
                例子:
          | page | keyword |button|title|
          |管车   | 手机管车  |通知     |行车事件 |
          
           场景大纲:到达单车通知列表
                假设 我在"<page>"页,直到"<keyword>"出现
                当 我等待<time>秒
                当   我点击"<button>"                   
                那么 我应该看到"<title>"出现
                例子:
          | page | keyword |time|button|title|
          |通知   | 行车事件 |10000|川G987WU|川G987WU|