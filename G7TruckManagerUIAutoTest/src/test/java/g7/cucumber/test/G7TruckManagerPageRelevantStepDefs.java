package g7.cucumber.test;

import io.appium.java_client.android.AndroidElement;
import java.util.List;
import org.openqa.selenium.By;
import cucumber.api.java.zh_cn.*;

public class G7TruckManagerPageRelevantStepDefs extends CucumberRunner {

	@假设("^我在\"([^\"]*)\"页,直到\"([^\"]*)\"出现$")
	public void which_page_on(String page, String keyword) throws Throwable {
		waitAuto(5);
		List<AndroidElement> upgrade_btn = driver.findElements(By.id("com.chinaway.android.truck.manager:id/upgrade_close"));
		if (upgrade_btn.size() > 0) {
			upgrade_btn.get(0).click();
		}
		if (page.equals("登录")) {
			waitUntilElementDisplayedById("com.chinaway.android.truck.manager:id/btn_goto_login");
			driver.findElement(
					By.id("com.chinaway.android.truck.manager:id/btn_goto_login"))
					.click();
			waitUntilElementDisplayedByName(keyword);
		} else {
			waitUntilElementDisplayedByName(keyword);
		}
	}

}
