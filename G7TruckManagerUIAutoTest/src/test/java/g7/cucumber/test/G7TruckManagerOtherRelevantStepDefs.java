package g7.cucumber.test;

import io.appium.java_client.android.AndroidElement;

import org.junit.Assert;
import org.openqa.selenium.By;

import cucumber.api.java.zh_cn.当;
import cucumber.api.java.zh_cn.那么;

public class G7TruckManagerOtherRelevantStepDefs extends CucumberRunner {

	@当("^我等待(\\d+)秒$")
	  public void waitTime(int time) throws Throwable {		
		Thread.sleep(time);	    
	 }
	
	@那么("^元素\"([^\"]*)\"已勾选$")
	  public void check_box_have_checked(String name) throws Throwable {	
	    AndroidElement rempwd = driver.findElement(By.name(name));
	    String attr = rempwd.getAttribute("checked");
	    Assert.assertEquals(attr, "true");
	   
	 }
}
