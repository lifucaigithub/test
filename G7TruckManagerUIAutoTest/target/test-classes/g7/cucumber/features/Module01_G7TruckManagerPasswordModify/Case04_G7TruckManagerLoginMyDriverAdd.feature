#language: zh-CN
功能:添加司机
          
	   场景大纲:进入添加司机信息页面
	                假设 我在"<page>"页,直到"<keyword>"出现
	                当   我点击"<button>"  
	                那么 我应该看到"<title>"出现
	                 例子:
	          | page | keyword |button|title|
	          | 我的司机   | 我的司机        |添加|司机信息  |
	 
	 场景大纲:添加司机
	                假设 我在"<page>"页,直到"<keyword>"出现
	                当    司机页面输入"<driverName>"和"<phone>" 
	                当   我点击"<button>" 
	             当 我等待<time>秒                             
	                那么 我应该看到"<driverName>"出现
	                 例子:
	          | page | keyword |driverName|phone  |  button |time|driverName|
	          | 司机信息  | 司机信息       |Alih   |13730645598  |保存  |8000   |Alih|