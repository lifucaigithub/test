package g7.cucumber.utils;

import io.appium.java_client.android.AndroidDriver;
import io.appium.java_client.android.AndroidElement;

import java.util.List;

import org.openqa.selenium.By;

public class SwipeScreenUtil  {	

	/** 
	 * 左滑某个元素
	 *  
	 * @param driver
	 * @param during 
	 * @param num 
	 */  
	public static void swipeElementLeft(AndroidDriver<AndroidElement> driver,int during,String name) {  
		AndroidElement element =  driver.findElement(By.name(name));
		//获取控件起始X 坐标
		int xStartPoint = element.getLocation().getX();
		// 获取控件最大宽度
		int xAxisEndPoint = xStartPoint + element.getSize().getWidth();
		//获取控件的高度
		int yAxis = element.getLocation().getY();
				
		driver.swipe(xAxisEndPoint+400,yAxis, xStartPoint,yAxis, during); 
	    
	}  
	
	/** 
	 * 上滑 
	 *  
	 * @param driver
	 * @param during 
	 * @param num 
	 */  
	public static void swipeToUp(AndroidDriver<AndroidElement> driver,int during, int num) {  
	    int width = driver.manage().window().getSize().width;  
	    int height = driver.manage().window().getSize().height;  
	    for (int i = 1; i <=num; i++) { 
	    	
	    	driver.swipe(width /2, height *7/10, width / 2, height / 8, during);  
	         
	    }  
	}  
	  
	/** 
	 * 下拉 
	 *  
	 * @param driver 
	 * @param during 
	 * @param num 
	 */  
	public static void swipeToDown(AndroidDriver<AndroidElement> driver,int during, int num) {  
	    int width = driver.manage().window().getSize().width;  
	    int height = driver.manage().window().getSize().height;  
	    for (int i = 1; i<=num; i++) {  
	    	driver.swipe(width / 2, height / 5, width / 2, height *3/4, during); 
	       
	    }  
	}  
	  
	/** 
	 * 向左滑动 
	 *   
	 * @param driver 
	 * @param during 
	 * @param num 
	 */  
	public  static void swipeToLeft(AndroidDriver<AndroidElement> driver,int during, int num) {  
	    int width = driver.manage().window().getSize().width;  
	    int height = driver.manage().window().getSize().height;  
	    for (int i = 1; i <=num; i++) {  
	    	driver.swipe(width * 7 / 8, height / 2, width / 108, height / 2, during); 
	       
	    }  
	}  
	
	
	  
	/** 
	 * 向右滑动 
	 *  
	 * @param driver 
	 * @param during 
	 * @param num 
	 */  
	public  static void swipeToRight(AndroidDriver<AndroidElement> driver,int during, int num) {  
	    int width = driver.manage().window().getSize().width;  
	    int height = driver.manage().window().getSize().height;  
	    for (int i = 1; i <=num; i++) {  
	    	driver.swipe(width/108, height / 2, width*7 / 8, height / 2, during); 
	       
	    }  
	}
	/** 
	 * 向左滑动num次 并点击按钮
	 *   
	 * @param driver 
	 * @param during 
	 * @param num 
	 */  
	public static void swipeToLeftNumberAndClickButton(AndroidDriver<AndroidElement> driver,int during, int num,String path) {  
	    int width = driver.manage().window().getSize().width;  
	    int height = driver.manage().window().getSize().height; 
	    List<AndroidElement> page  = driver.findElementsByXPath("//android.webkit.WebView[@content-desc='我的车队']/android.view.View[10]");
	    if(page.size()>0){
		    for (int i = 1; i <=num; i++) {
		    	 if(i==num){
				    	driver.swipe(width*7/8, height / 2, width / 108, height / 2, during); 
				    	NativeAndWebViewChangeUtil.nativeChangeToWebView(driver);
				    	driver.findElementByXPath(path).click();
				    	//driver.findElementByXPath("//*[@id=\"vux_view_box_body\"]/div/div[4]/div[1]/div/div[1]/div[5]/div/div[2]").click();
				    	    	    
				    }else{
				    	
				    	driver.swipe(width*7/8, height / 2, width / 108, height / 2, during); 
				    }	    	  
				       
				  }    
	    }
	}   
	
	
	/** 
	 * 向左滑动num次 并点击class 属性按钮
	 *   
	 * @param driver 
	 * @param during 
	 * @param num 
	 */  
	public static void truckDetailSwipeToLeftNumberAndClickButton(AndroidDriver<AndroidElement> driver,int during, int num,String path) {  
	    int width = driver.manage().window().getSize().width;  
	    int height = driver.manage().window().getSize().height; 
	    NativeAndWebViewChangeUtil.nativeChangeToWebView(driver);
	    String path1 ="//*[contains(@class, 'guide--alias__cont')]";
	    List<AndroidElement> page  = driver.findElementsByXPath(path1);
	   if(page.size()>0){
		    for (int i = 1; i <=num; i++) {
			    if(i==num){
			    	   NativeAndWebViewChangeUtil.webViewChangeToNative(driver);
					   driver.swipe(width/2, height / 2, width / 108, height / 2, during); 
					   NativeAndWebViewChangeUtil.nativeChangeToWebView(driver);
					   driver.findElementByXPath(path).click();
					    	//driver.findElementByXPath("//*[@id=\"vux_view_box_body\"]/div/div[4]/div[1]/div/div[1]/div[5]/div/div[2]").click();
					    	    	    
				}else{
					    	
					    driver.swipe(width/2, height / 2, width / 108, height / 2, during); 
					   }	    	  
					       
				 }    
	    }
	}   
	
	/** 
	 * 向右滑动num次 并点击按钮
	 *   
	 * @param driver 
	 * @param during 
	 * @param num 
	 */  
	public static void swipeToRightNumberAndClickButton(AndroidDriver<AndroidElement> driver,int during, int num,String path) {  
	    int width = driver.manage().window().getSize().width;  
	    int height = driver.manage().window().getSize().height; 
	    for (int i = 1; i <num; i++) {
			    if(i==num){
			    	driver.swipe( width / 108, height / 2,  width*7/8, height / 2,during); 
			    	NativeAndWebViewChangeUtil.nativeChangeToWebView(driver);
			    	driver.findElementByXPath(path).click();
			    	//driver.findElementByXPath("//*[@id=\"vux_view_box_body\"]/div/div[4]/div[1]/div/div[1]/div[5]/div/div[2]").click();
			    	    	    
			    }else{
			    	
			    	driver.swipe(width / 108, height / 2,  width*7/8, height / 2,during); 
			    }	    	  
			       
			  }     
	}    
	
	/** 
	 * 向上滑动num次 并点击按钮
	 *   
	 * @param driver 
	 * @param during 
	 * @param num 
	 */  
	public static void swipeToUpNumberAndClickButton(AndroidDriver<AndroidElement> driver,int during, int num,String path) {  
	    int width = driver.manage().window().getSize().width;  
	    int height = driver.manage().window().getSize().height; 
	    for (int i = 1; i <num; i++) {
	    	 if(i==num){
			    	driver.swipe( width / 2, height *7/8,  width/2, height /192,during); 
			    	NativeAndWebViewChangeUtil.nativeChangeToWebView(driver);
			    	driver.findElementByXPath(path).click();
			    	//driver.findElementByXPath("//*[@id=\"vux_view_box_body\"]/div/div[4]/div[1]/div/div[1]/div[5]/div/div[2]").click();
			    	    	    
			    }else{
			    	
			    	driver.swipe(width / 2, height *7/8,  width/2, height /192,during); 
			    }	    	  
			       
			  }     
	}    
	
	/** 
	 * 向下滑动num次 并点击按钮
	 *   
	 * @param driver 
	 * @param during 
	 * @param num 
	 */  
	public static void swipeToDownNumberAndClickButton(AndroidDriver<AndroidElement> driver,int during, int num,String path) {  
	    int width = driver.manage().window().getSize().width;  
	    int height = driver.manage().window().getSize().height; 
	    for (int i = 1; i <num; i++) {
	    	 if(i==num){
			    	driver.swipe(width / 2, height /192,  width/2, height *7/8,during); 
			    	NativeAndWebViewChangeUtil.nativeChangeToWebView(driver);
			    	driver.findElementByXPath(path).click();
			    	//driver.findElementByXPath("//*[@id=\"vux_view_box_body\"]/div/div[4]/div[1]/div/div[1]/div[5]/div/div[2]").click();
			    	    	    
			    }else{
			    	
			    	driver.swipe(width / 2, height /192,  width/2, height *7/8,during); 
			    }	    	  
			       
			  }     
	}    
}
