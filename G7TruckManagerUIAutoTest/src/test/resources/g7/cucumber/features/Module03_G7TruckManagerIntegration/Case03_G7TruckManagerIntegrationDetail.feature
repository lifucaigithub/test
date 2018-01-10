#language: zh-CN
功能:获取明细
        场景大纲:获取明细       
              当         我切换到WebView 
              当 我等待<time>秒               
                并且  我点击WebView链接"<link>"   
                当 我等待<time1>秒                           
                那么 我应该看到WebView"<title>"出现
                当    我点击back键            
                那么 我应该看到WebView"<webviewtitle>"出现          
                 例子:
          |time| link |time1|title |webviewtitle|
          |8000|detail |8000|温馨提示   |获取明细|
          
          
  
          
           
        