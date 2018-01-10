#language: zh-CN
功能:删除某个司机
          
	   场景大纲:删除某个司机
	                假设 我在"<page>"页,直到"<keyword>"出现
	                当   我删除司机"<driverName>"  
	                当 我等待<time>秒           
	                那么 我不应该看到"<driverName>"出现
	                 例子:
	          | page | keyword |driverName|time|driverName|
	          | 我的司机   | 我的司机        |Alih|8000|Alih  |