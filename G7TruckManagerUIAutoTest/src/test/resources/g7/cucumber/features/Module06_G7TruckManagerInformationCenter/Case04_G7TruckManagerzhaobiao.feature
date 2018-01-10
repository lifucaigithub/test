#language: zh-CN
功能:招标信息
        场景大纲:到达招标信息页面
                假设 我在"<page>"页,直到"<keyword>"出现
                当 我等待<time>秒  
                当   我点击"<button>"                   
                那么 我应该看到"<title>"出现
                 例子:
          | page    | keyword |time|button |  title |
          | 消息中心  | 消息中心|5000|招标信息 |招标信息  |

        场景大纲:返回消息中心
                假设 我在"<page>"页,直到"<keyword>"出现
                当 我等待<time>秒  
                当   我点击回退               
                那么 我应该看到"<title>"出现
                 例子:
          | page    |keyword  |time|  title |
          | 招标信息  |招标信息   |5000|消息中心| 