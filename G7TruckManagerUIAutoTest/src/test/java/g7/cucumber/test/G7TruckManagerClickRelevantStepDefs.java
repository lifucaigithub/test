package g7.cucumber.test;

import g7.cucumber.utils.ClearEditAndBackUtil;
import io.appium.java_client.android.AndroidElement;

import org.openqa.selenium.By;

import cucumber.api.java.zh_cn.当;

public class G7TruckManagerClickRelevantStepDefs extends CucumberRunner {
	
	@当("^我点击\"([^\"]*)\"$")
	public void i_click(String button) throws Throwable {
		driver.findElement(By.name(button)).click();

	}

	@当("^我点击WebView\"([^\"]*)\"$")
	public void i_click_webviwe(String button) throws Throwable {
		String path = "//*[contains(text(), '" + button + "')]";
		AndroidElement btn = driver.findElementByXPath(path);
		btn.click();
	}

	@当("^我点击事件\"([^\"]*)\"$")
	public void i_click_flueEvent(String name) throws Throwable {
		AndroidElement oilEvent = driver.findElementByAccessibilityId(name);
		oilEvent.click();
	}
	@当("^我点击事件加油$")
	public void i_click_addFlueEvent() throws Throwable {
		driver.tap(1, 500, 500, 1);
	}
	@当("^我点击事件异常少油$")
	public void i_click_addFewFlueEvent() throws Throwable {
		driver.tap(1, 500, 650, 1);
	}
	
	@当("^我点击车辆\"([^\"]*)\"$")
	public void click_car_name(String carName) throws Throwable {
		AndroidElement carlist =  driver.findElementByAccessibilityId(carName);
		carlist.click();
	}
	
	@当("^通过AccessibilityId点击列表\"([^\"]*)\"$")
	public void click_ele_byAccessibilityId(String name) throws Throwable {
		AndroidElement ele = driver.findElementByAccessibilityId(name);
		ele.click();
	}

	@当("^我点击WebView链接\"([^\"]*)\"$")
	public void i_click_webviwelink(String link) throws Throwable {
		String path = "//a[contains(@href, '" + link + "')]";
		driver.findElementByXPath(path).click();

	}

	@当("^我点击商城分类\"([^\"]*)\"$")
	public void i_click_mallcategory(String name) throws Throwable {
		String path = "//img[contains(@alt, '" + name + "')]";
		driver.findElementByXPath(path).click();

	}
	@当("^我点击记住密码$")
	public void click_remember_pwd() throws Throwable {
		
		driver.findElement(By.id("com.chinaway.android.truck.manager:id/checkbox_remember_password")).click();
	}
	@当("^我点击回退$")
	public void click_leftMenu() throws Throwable {
		AndroidElement backMenu =  driver.findElement(By.id("com.chinaway.android.truck.manager:id/title_left"));
		backMenu.click();
		
	}
	
	@当("^我点击back键$")
	public void click_backMenu() throws Throwable {
		ClearEditAndBackUtil.clickAndroidBack(driver);
	}
	
	@当("^我点击back键2次$")
	public void double_click_backMenu() throws Throwable {
		ClearEditAndBackUtil.doubleClickAndroidBack(driver);
	}
}
