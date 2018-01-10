package g7.cucumber.utils;

import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;

public class ImageUtil {
	public static boolean sameAs(BufferedImage myImage,BufferedImage otherImage, double percent) {

		if (otherImage.getWidth() != myImage.getWidth()) {
			return false;
		}
		if (otherImage.getHeight() != myImage.getHeight()) {
			return false;
		}
		int width = myImage.getWidth();
		int height = myImage.getHeight();
		int numDiffPixels = 0;
		
		for (int y = 0; y < height; y++) {
			for (int x = 0; x < width; x++) {
				if (myImage.getRGB(x, y) != otherImage.getRGB(x, y)) {
					
					numDiffPixels++;
				}
			}
		}
		double numberPixels = height * width;
		double diffPercent = numDiffPixels / numberPixels;
		//System.out.println("numberPixels"+numberPixels);
		//System.out.println("diffPercent"+diffPercent);
		return percent <= 1.0D - diffPercent;
		//return diffPercent >= percent;
	}

	public static BufferedImage getSubImage(BufferedImage image, int x, int y,
			int w, int h) {
		return image.getSubimage(x, y, w, h);
	}

	public static BufferedImage getImageFromFile(File f) {

		BufferedImage img = null;

		try {
			img = ImageIO.read(f);

		} catch (IOException e) {
			e.printStackTrace();
			//System.exit(1);
		}
		return img;
	}
	public static void main(String[] args) {
		String path = System.getProperty("user.dir");
		String currentPath = path+"\\"+"image"+"\\"+"1"+".png";
		String currentPath1 = path+"\\"+"image"+"\\"+"2"+".png";
		File expect = new File(currentPath);
		File ac = new File(currentPath1);
		BufferedImage img1 = getImageFromFile(expect);
		BufferedImage img2 = getImageFromFile(ac);
		BufferedImage subImg1 = ImageUtil.getSubImage(img1, 45, 250, 1015, 870);
		BufferedImage subImg2 = ImageUtil.getSubImage(img2, 45, 250, 1015, 870);
		sameAs(subImg1,subImg2,1);
	}
}
