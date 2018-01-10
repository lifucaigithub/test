package g7.cucumber.utils;

import static org.junit.Assert.assertTrue;

import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;
import io.appium.java_client.android.AndroidDriver;
import io.appium.java_client.android.AndroidElement;
import org.apache.commons.io.FileUtils;
import org.openqa.selenium.OutputType;


public class CompareScreenShots{

	public static void compareScreenAndSubScreen(AndroidDriver<AndroidElement> driver) throws InterruptedException,
			IOException {

	
		String currentPath = System.getProperty("user.dir");

		File f1 = driver.getScreenshotAs(OutputType.FILE);
		FileUtils.copyFile(f1, new File(currentPath + "\\" + "1" + ".png"));
		BufferedImage img1 = ImageUtil.getImageFromFile(f1);

		File f2 = driver.getScreenshotAs(OutputType.FILE);
		FileUtils.copyFile(f1, new File(currentPath + "\\" + "2" + ".png"));
		BufferedImage img2 = ImageUtil.getImageFromFile(f2);

		Boolean same = ImageUtil.sameAs(img1, img2, 0.9);
		assertTrue(same);

		BufferedImage subImg1 = ImageUtil.getSubImage(img1, 90, 387, 900, 132);
		BufferedImage subImg2 = ImageUtil.getSubImage(img2, 90, 387, 900, 132);
		Boolean sameSub = ImageUtil.sameAs(subImg1, subImg2, 1);
		assertTrue(sameSub);

		File f3 = new File(currentPath + "\\" + "sub-1.png");
		ImageIO.write(subImg1, "PNG", f3);

		File f4 = new File(currentPath + "\\" + "sub-2.png");
		ImageIO.write(subImg2, "PNG", f4);

	}

}
