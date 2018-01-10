package g7.cucumber.test;

import g7.cucumber.utils.ClearEditAndBackUtil;
import g7.cucumber.utils.SwipeScreenUtil;
import io.appium.java_client.android.AndroidElement;

import java.util.List;

import org.openqa.selenium.By;

import cucumber.api.java.zh_cn.当;

public class G7TruckManagerAddDriverRelevantStepDefs extends CucumberRunner{

	@当("^我删除司机\"([^\"]*)\"$")
	public void delete_driver(String driverName) throws Throwable {
		SwipeScreenUtil.swipeElementLeft(driver,1000,driverName);
		driver.findElement(By.id("com.chinaway.android.truck.manager:id/btn_delete")).click();
		waitUntilElementDisplayedById("com.chinaway.android.truck.manager:id/btn_positive");
		driver.findElement(By.id("com.chinaway.android.truck.manager:id/btn_positive")).click();
	}
	@当("^司机页面输入\"([^\"]*)\"和\"([^\"]*)\"$")
	public void add_driver(String driverName, String phone) throws Throwable {
		List<AndroidElement> textFieldsList = driver.findElements(By.className("android.widget.EditText"));
		
		textFieldsList.get(1).sendKeys(driverName);
		ClearEditAndBackUtil.clickAndroidBack(driver);

		textFieldsList.get(2).sendKeys(phone);
		ClearEditAndBackUtil.clickAndroidBack(driver);
	}
}
