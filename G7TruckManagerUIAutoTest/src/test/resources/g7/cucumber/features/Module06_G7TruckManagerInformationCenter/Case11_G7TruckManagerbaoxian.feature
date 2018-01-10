#language: zh-CN
功能:保险信息
        场景大纲:到达保险信息页面
                假设 我在"<page>"页,直到"<keyword>"出现
                当 我等待<time>秒  
                当  向上滑动<n>次,直到"<title>"出现
                当   我点击"<button>"                   
                那么 我应该看到"<title1>"出现
                 例子:
          | page    | keyword|time |n|title|button |  title1 |
          | 消息中心  | 消息中心|5000|1|保险信息|保险信息 |保险信息  |
		  
        场景大纲:返回消息中心
                假设 我在"<page>"页,直到"<keyword>"出现
                当 我等待<time>秒  
                当   我点击回退                 
                那么 我应该看到"<title>"出现
                 例子:
          | page    |keyword |time |  title |
          | 保险信息  |保险信息   |5000|消息中心| 