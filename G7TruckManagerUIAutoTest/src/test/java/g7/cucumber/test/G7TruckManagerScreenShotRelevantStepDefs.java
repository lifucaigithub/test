package g7.cucumber.test;

import g7.cucumber.utils.ImageUtil;

import java.awt.image.BufferedImage;
import java.io.File;

//import javax.imageio.ImageIO;

import org.junit.Assert;
import org.openqa.selenium.OutputType;

import cucumber.api.java.zh_cn.那么;

public class G7TruckManagerScreenShotRelevantStepDefs extends CucumberRunner{


	
	@那么("^截取图片名\"([^\"]*)\"的坐标(\\d+)坐标(\\d+)截取宽度(\\d+)高度(\\d+)子图\"([^\"]*)\"一致$")
	public void getSubImage(String name,int startx,int starty,int weight,int hight,String perc) throws Throwable {
		double percent = Double.parseDouble(perc);
		String path = System.getProperty("user.dir");
		String currentPath = path+"\\"+"image"+"\\"+name+".png";
		File expect = new File(currentPath);
		BufferedImage img1 = ImageUtil.getImageFromFile(expect);
		File actual = driver.getScreenshotAs(OutputType.FILE);
		//FileUtils.copyFile(actual, new File(path+"\\"+"image"+"\\"+ getCurrentTimeSnap() + ".png"));
		BufferedImage img2 = ImageUtil.getImageFromFile(actual);		
		BufferedImage subImg1 = ImageUtil.getSubImage(img1, startx, starty, weight, hight);
		BufferedImage subImg2 = ImageUtil.getSubImage(img2, startx, starty, weight, hight);
		/*
		File f3 = new File(path+"\\"+"image"+"\\" + "sub-1.png");
		ImageIO.write(subImg1, "PNG", f3);
		File f4 = new File(path+"\\"+"image"+"\\" + "sub-2.png");
		ImageIO.write(subImg2, "PNG", f4);
		*/
		Boolean sameSub = ImageUtil.sameAs(subImg1, subImg2, percent);
		Assert.assertTrue(sameSub);
		
    }
	
}
