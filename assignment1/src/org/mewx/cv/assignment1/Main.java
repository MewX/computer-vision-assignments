package org.mewx.cv.assignment1;


import org.bytedeco.javacpp.opencv_stitching.Stitcher;

import java.io.File;
import java.net.URISyntaxException;

/**
 * This is main class for assignment 1.
 * Created by mewx on 10/04/17.
 */
public class Main {
    private static String basePath;

    public static void main(String[] args) throws URISyntaxException {
        // usage: java -jar xxx.jar folderName
        basePath = Main.class.getProtectionDomain().getCodeSource().getLocation().toURI().getPath();
        basePath = basePath.substring(0, basePath.lastIndexOf(File.separator) + 1) + "rc" + File.separator;
        System.out.println(basePath);

//        String[] fileList = (String[]) Arrays.stream(getFileNameList(basePath)).filter(a -> a.startsWith(args[0])).toArray();
        String[] fileList = getFileNameList(basePath + args[0]);
        if (fileList.length == 0) {
            System.out.println("No file found.");
            return;
        } else {
            System.out.println("Found files:");
        }
        for (String temp : fileList) System.out.println(temp);

        // next

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

    public void run() {
        Stitcher s;
    }
}
