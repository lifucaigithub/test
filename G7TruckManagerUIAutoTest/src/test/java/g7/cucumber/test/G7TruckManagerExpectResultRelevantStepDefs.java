package g7.cucumber.test;

import io.appium.java_client.android.AndroidElement;

import java.util.List;

import org.junit.Assert;
import org.openqa.selenium.By;

import cucumber.api.java.zh_cn.那么;

public class G7TruckManagerExpectResultRelevantStepDefs extends CucumberRunner{

	@那么("^我应该看到\"([^\"]*)\"出现$")
	public void i_will_see(String title) throws Throwable {
		waitUntilElementDisplayedByName(title);
	}
	
	
	@那么("^我应该看到WebView\"([^\"]*)\"出现$")
	public void i_will_see_webview(String title) throws Throwable {
		String path ="//*[contains(text(), '" + title + "')]";
		waitUntilElementDisplayedByXpath(path);
		
	}
	
	
	
	@那么("^我应该看到弹出层出现$")
	public void i_will_see_popup() throws Throwable {
		List<AndroidElement> popup = driver.findElements(By.className("android.widget.ExpandableListView"));
		Assert.assertNotNull(popup.size());
		
	}
	@那么("^我不应该看到\"([^\"]*)\"出现$")
	public void delete_driver_success(String driverName) throws Throwable {
		List<AndroidElement> deleteDriverName = driver.findElements(By.name(driverName));
		 Assert.assertEquals(deleteDriverName.size(), 0);
		
	}
}
