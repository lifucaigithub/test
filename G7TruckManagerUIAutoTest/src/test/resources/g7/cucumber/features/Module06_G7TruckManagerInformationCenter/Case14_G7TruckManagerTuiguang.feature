#language: zh-CN
功能:其他信息
        场景大纲:到达其他信息页面
                假设 我在"<page>"页,直到"<keyword>"出现
                当 我等待<time>秒  
                当   我点击"<button>"                   
                那么 我应该看到"<title>"出现
                 例子:
          | page    | keyword|time |button     |  title |
          | 消息中心  | 消息中心 |5000|外部链接测试|其他信息  |
		  
        场景大纲:返回消息中心
                假设 我在"<page>"页,直到"<keyword>"出现
                当 我等待<time>秒  
                当   我点击回退                 
                那么 我应该看到"<title>"出现
                 例子:
          | page    |keyword |time |  title |
          | 其他信息 |其他信息   |5000|消息中心   | 
       
         场景大纲:返回手机管车
                假设 我在"<page>"页,直到"<keyword>"出现
                当 我等待<time>秒  
                当   我点击回退                 
                那么 我应该看到"<title>"出现
                 例子:
          | page    |keyword |time |  title |
          | 消息中心 |消息中心    |5000|手机管车  | 
          
    场景大纲:退出登录     
             当 我等待<time>秒  
                当    我点击"<button>"
                那么 我应该看到"<title>"出现
                例子:
      |time  |button   |title|
      |2000  |我的 |我的手机管车|
      |2000  |我的信息 |我的信息|
      |2000 |退出登录|确认退出|
      |2000  |确认退出|登录|