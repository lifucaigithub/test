package g7.cucumber.test;

import io.appium.java_client.android.AndroidElement;
import cucumber.api.java.zh_cn.当;

public class G7TruckManagerDateRelevantStepDefs extends CucumberRunner{
	
	@当("^我点击日期选择器$")
	public void click_date_chose() throws Throwable {
		String currentDate = getCurrentDate();
		String path ="//android.view.View[@content-desc='"+currentDate+"']";
		driver.findElementByXPath(path).click();
	}
	
	@当("^我点击\"([^\"]*)\"选择开始时间$")
	public void click_begin_date(String name) throws Throwable {
		AndroidElement begin  = driver.findElementByAccessibilityId(name);
		begin.click();
	}
	
	@当("^我点击选择结束时间$")
	public void click_begin_date() throws Throwable {
		AndroidElement end  = driver.findElementById("com.chinaway.android.truck.manager:id/end_time");
		end.click();
	}
	@当("^坐标(\\d+)坐标(\\d+)下滑到坐标(\\d+)坐标(\\d+)选择年\"([^\"]*)\"$")
	public void choose_year(int startx,int starty,int endx,int endy,String time) throws Throwable {
		 String currentDate = getCurrentDate();
		 int year = Integer.parseInt(currentDate.substring(0, 4));
		 int paramYear = Integer.parseInt(time);
		 int count = year - paramYear;
		 for(int i=1;i<=count;i++){
			 driver.swipe(startx, starty, endx, endy, 1000); 
		 }
    }
	
	@当("^坐标(\\d+)坐标(\\d+)下滑到坐标(\\d+)坐标(\\d+)选择月\"([^\"]*)\"$")
	public void choose_month(int startx,int starty,int endx,int endy,String time) throws Throwable {
		 String currentDate = getCurrentDate();		 
		 int month = Integer.parseInt(currentDate.substring(5,7));
		 int paramMonth = Integer.parseInt(time);
		 int count = month - paramMonth;
		 if(count>0){
			 for(int i=1;i<=count;i++){
				 driver.swipe(startx, starty, endx, endy, 1000); 
			 }
		 }else{
			 for(int i=1;i<=Math.abs(count);i++){
				 driver.swipe(startx, endy, endx, starty, 1000); 
			 }
		 }
		
    }
	
	@当("^坐标(\\d+)坐标(\\d+)下滑到坐标(\\d+)坐标(\\d+)选择日\"([^\"]*)\"$")
	public void choose_day(int startx,int starty,int endx,int endy,String time) throws Throwable {
		 String currentDate = getCurrentDate();
		 int day = Integer.parseInt(currentDate.substring(8, 10));
		 int paramDay = Integer.parseInt(time);
		 int count = day - paramDay;
		 if(count>0){
			 for(int i=1;i<=count;i++){
				 driver.swipe(startx, starty, endx, endy, 1000); 
			 }
		 }else{
			 for(int i=1;i<=Math.abs(count);i++){
				 driver.swipe(startx, endy, endx, starty, 1000); 
			 }
		 }
    }
}
