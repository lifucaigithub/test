package g7.cucumber.test;

import g7.cucumber.utils.SwipeScreenUtil;
import cucumber.api.java.zh_cn.当;

public class G7TruckManagerSwipeRelevantStepDefs extends CucumberRunner{

	@当("^向上滑动(\\d+)次,直到\"([^\"]*)\"出现$")
	public void swipeToUp(int num,String keyword) throws Throwable {
	    SwipeScreenUtil.swipeToUp(driver, 1000, num);
	    waitUntilElementDisplayedByName(keyword);
	}
	
	@当("^向下滑动(\\d+)次,直到\"([^\"]*)\"出现$")
	public void swipeToDown(int num,String keyword) throws Throwable {
	    SwipeScreenUtil.swipeToDown(driver, 1000, num);
	    waitUntilElementDisplayedByName(keyword);
	}
	
	@当("^向左滑动(\\d+)次,直到\"([^\"]*)\"出现$")
	public void swipeToLeft(int num,String keyword) throws Throwable {
	    SwipeScreenUtil.swipeToLeft(driver, 1000, num);
	    waitUntilElementDisplayedByName(keyword);
	}
	
	@当("^向右滑动(\\d+)次,直到\"([^\"]*)\"出现$")
	public void swipeToRight(int num,String keyword) throws Throwable {
	    SwipeScreenUtil.swipeToRight(driver, 1000, num);
	    waitUntilElementDisplayedByName(keyword);
	}
	
	@当("^划屏(\\d+)次,并点击\"([^\"]*)\"$")
	public void swipeScreenLeftCountAndClick(int num,String name) throws Throwable {
		String path ="//*[contains(text(), '" + name + "')]";
	    SwipeScreenUtil.swipeToLeftNumberAndClickButton(driver, 1000, num,path);
	    
	}
	
	@当("^车辆详情划屏(\\d+)次,并点击\"([^\"]*)\"$")
	public void truckDetailSwipeScreenLeftCountAndClick(int num,String name) throws Throwable {
		String path ="//*[contains(@class, '" + name + "')]";
	    SwipeScreenUtil.truckDetailSwipeToLeftNumberAndClickButton(driver, 1000, num,path);
	    
	}
}
