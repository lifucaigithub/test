#language: zh-CN
功能:积分说明         
场景大纲:积分说明        
           当 我等待<time>秒               
                当   我点击WebView链接"<link>" 
                当 我等待<time1>秒           
                并且 我切换到Native                  
                那么 我应该看到"<title>"出现           
                 例子:
         |time | link |time1|title |
          |8000|intro |8000|积分说明   |      
   
场景大纲:返回积分中心           
                当   我点击back键                   
                那么 我应该看到"<title>"出现
                
                 例子:
          | title |
          |积分中心     |