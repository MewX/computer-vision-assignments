package org.mewx.cv.assignment1;


import org.bytedeco.javacpp.opencv_core.Mat;
import org.bytedeco.javacpp.opencv_core.MatVector;
import org.bytedeco.javacpp.opencv_imgcodecs;
import org.bytedeco.javacpp.opencv_stitching.Stitcher;

import java.io.File;
import java.net.URISyntaxException;

/**
 * This is main class for assignment 1.
 * Created by mewx on 10/04/17.
 */
public class Main {

    public static void main(String[] args) throws URISyntaxException {
        // usage: java -jar xxx.jar folderName
        String basePath = Main.class.getProtectionDomain().getCodeSource().getLocation().toURI().getPath();
        basePath = basePath.substring(0, basePath.lastIndexOf(File.separator) + 1);
        System.out.println(basePath);

//        String[] fileList = (String[]) Arrays.stream(getFileNameList(basePath)).filter(a -> a.startsWith(args[0])).toArray();
        String[] fileList = getFileNameList(basePath + "rc" + File.separator + args[0]);
        if (fileList.length == 0) {
            System.out.println("No file found.");
            return;
        } else {
            System.out.println("Found files:");
        }
        for (String temp : fileList) System.out.println(temp);

        // todo: try different file name orders

        // stitching
        new Main().run(basePath + "rc" + File.separator + args[0] + File.separator,
                fileList, args[0] + "_result.png");

    }

    private static String[] getFileNameList(String dir) {
        File[] files = new File(dir).listFiles();
        if (files == null) return new String[0];
        String[] strings = new String[files.length];
        for (int i = 0; i < strings.length; i ++) {
            strings[i] = files[i].getName();
        }
        return strings;
    }

    public void run(String basePath, String[] fileNames, String targetName) {
        MatVector imgs = new MatVector();
        for (String name : fileNames) {
            System.out.println("Reading: " + basePath + name);
            Mat img = opencv_imgcodecs.imread(basePath + name);
            imgs.resize(imgs.size() + 1);
            imgs.put(imgs.size() - 1, img);
        }

        Mat pano = new Mat();
        Stitcher stitcher = Stitcher.createDefault(false);
        int status = stitcher.stitch(imgs, pano);

        if (status != Stitcher.OK) {
            System.out.println("Can't stitch images, error code = " + status);
            return;
        }

        opencv_imgcodecs.imwrite(basePath + targetName, pano);
        System.out.println("Images stitched together to make " + basePath + targetName);
    }
}
