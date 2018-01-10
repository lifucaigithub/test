package g7.cucumber.utils;



import io.appium.java_client.android.AndroidDriver;
import io.appium.java_client.android.AndroidElement;

public class NativeAndWebViewChangeUtil {

	public static void nativeChangeToWebView(AndroidDriver<AndroidElement> driver) {
		
		driver.context("WEBVIEW_com.chinaway.android.truck.manager");

	}
	public static void webViewChangeToNative(AndroidDriver<AndroidElement> driver) {

		driver.context("NATIVE_APP");

	}
}
