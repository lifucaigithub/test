package g7.cucumber.test;

import java.net.URL;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;

import g7.cucumber.config.Settings;
import g7.cucumber.utils.AndroidDriverWait;
import io.appium.java_client.android.AndroidDriver;
import io.appium.java_client.android.AndroidElement;

import org.junit.AfterClass;
import org.junit.BeforeClass;
import org.junit.runner.RunWith;
import org.openqa.selenium.By;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.support.ui.ExpectedConditions;

import cucumber.api.CucumberOptions;
import cucumber.api.junit.Cucumber;

@RunWith(Cucumber.class)
@CucumberOptions(plugin = { "pretty", "html:target/cucumber-html-report", "json:target/cucumber-json-report/cucumber.json" },
				 features = ("src/test/resources/g7/cucumber/features"),
				 glue = "g7.cucumber.test")
public class CucumberRunner {
	public  static  AndroidDriver<AndroidElement> driver;

	@BeforeClass
	public  static void setUp() throws Exception {
		if (Settings.device.toUpperCase().equals("ANDROID")) {
			DesiredCapabilities capabilities = new DesiredCapabilities();
			capabilities.setCapability("deviceName", "7b4fcc72");
			capabilities.setCapability("platformName", "Android");
			capabilities.setCapability("platformVersion", "6.0.1");
			capabilities.setCapability("noReset", true);
			capabilities.setCapability("noSign", true);
			capabilities.setCapability("unicodeKeyboard", "True");
			capabilities.setCapability("resetKeyboard", "True");
			capabilities.setCapability("app", Settings.g7TruckManagerAppPath);
			capabilities.setCapability("appPackage","com.chinaway.android.truck.manager");
			capabilities.setCapability("appActivity","com.chinaway.android.truck.manager.ui.SplashScreenActivity");
			
			// Create an instance of RemoteWebDriver and connect to the Appium server
			
			driver = new AndroidDriver<>(new URL("http://127.0.0.1:4723/wd/hub"), capabilities);

		}
	}

	@AfterClass
	public  static void tearDown() {
		driver.quit();

	}

	public  void waitUntilElementDisplayedByName(String name) {
		AndroidDriverWait wait = new AndroidDriverWait(driver, 20);
		wait.until(ExpectedConditions.presenceOfElementLocated(By.name(name)));
	}

	public  void waitUntilElementDisplayedById(String id) {
		AndroidDriverWait wait = new AndroidDriverWait(driver, 20);
		wait.until(ExpectedConditions.presenceOfElementLocated(By.id(id)));
	}
	
	public  void waitUntilElementDisplayedByXpath(String path) {
		AndroidDriverWait wait = new AndroidDriverWait(driver, 20);
		wait.until(ExpectedConditions.presenceOfElementLocated(By.xpath(path)));
	}
	public  void waitUntilElementClickableByXpath(String path) {
		AndroidDriverWait wait = new AndroidDriverWait(driver, 20);
		wait.until(ExpectedConditions.elementToBeClickable(By.xpath(path)));
	}


	public  void waitAuto(int time) throws InterruptedException {
		Thread.sleep(time);
	}
	public  String getCurrentDate() throws InterruptedException {
		Date currentTime = new Date();
		DateFormat formatter = new SimpleDateFormat("yyyy年MM月dd日");
		String dateString = formatter.format(currentTime);
		return dateString;
		 
		
	}
	public  String getCurrentTimeSnap() throws InterruptedException {
		SimpleDateFormat df = new SimpleDateFormat("yyyyMMddHHmmss");//设置日期格式
		String date = df.format(new Date());
		return date;
		
	}
	
	
	
}