package g7.cucumber.test;

import g7.cucumber.utils.NativeAndWebViewChangeUtil;
import cucumber.api.java.zh_cn.当;

public class G7TruckManagerWebViewNativeRelevantStepDefs  extends CucumberRunner{


	@当("^我切换到WebView$")
	public void change_webview() throws Throwable {
		waitAuto(5);
		NativeAndWebViewChangeUtil.nativeChangeToWebView(driver);
	}
	
	@当("^我切换到Native$")
	public void change_native() throws Throwable {
		waitAuto(5);
		NativeAndWebViewChangeUtil.webViewChangeToNative(driver);	
		
	}
}
