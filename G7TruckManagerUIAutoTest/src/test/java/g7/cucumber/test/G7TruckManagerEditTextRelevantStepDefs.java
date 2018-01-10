package g7.cucumber.test;

import g7.cucumber.utils.ClearEditAndBackUtil;
import io.appium.java_client.android.AndroidElement;

import java.util.List;

import org.openqa.selenium.By;

import cucumber.api.java.zh_cn.当;

public class G7TruckManagerEditTextRelevantStepDefs extends CucumberRunner  {
	
	@当("^页面出现输入框,我输入\"([^\"]*)\"和\"([^\"]*)\"$")
	public void find_textFields(String account, String password) throws Throwable {
		List<AndroidElement> textFieldsList = driver.findElements(By.className("android.widget.EditText"));
		AndroidElement name = textFieldsList.get(0);
		AndroidElement pwd = textFieldsList.get(1);
		String text = name.getText();
		if(text.equals("请输入账号")){
			name.sendKeys(account);
			ClearEditAndBackUtil.clickAndroidBack(driver);
		}else{
			name.clear();
			name.sendKeys(account);
			ClearEditAndBackUtil.clickAndroidBack(driver);
		}	
		pwd.clear();
		pwd.sendKeys(password);
		ClearEditAndBackUtil.clickAndroidBack(driver);
	}
	
	 @当("^我在第(\\d+)个输入框输入\"([^\"]*)\"$")
	  public void enter_oneTextFields(int n,String param) throws Throwable {
	    List<AndroidElement> textFieldsList = driver.findElements(By.className("android.widget.EditText"));
	    textFieldsList.get(n-1).sendKeys(param);
	    
	 }
	 
	
}
