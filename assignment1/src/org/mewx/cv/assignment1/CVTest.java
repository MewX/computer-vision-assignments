package org.mewx.cv.assignment1;

import org.bytedeco.javacpp.indexer.UByteRawIndexer;
import org.bytedeco.javacpp.opencv_core;
import org.bytedeco.javacpp.opencv_core.*;
import org.bytedeco.javacpp.opencv_imgcodecs;
import org.bytedeco.javacpp.opencv_imgproc;
import org.bytedeco.javacpp.opencv_objdetect.CascadeClassifier;

import java.io.File;
import java.net.URISyntaxException;

/**
 * Created by mewx on 6/04/17.
 * The test file for OpenCV java binding.
 */
public class CVTest {
    public static String BASE_RESOURCE_DIR = "/rc";

    public static void main(String[] args) throws URISyntaxException {
        System.out.println("Welcome to OpenCV");
        Mat m = new Mat(5, 10, opencv_core.CV_8UC1, new Scalar(0));
        UByteRawIndexer indexer = m.createIndexer();
        System.out.println("OpenCV Mat: " + m);
        for (int c = 0; c < m.cols(); c ++)
            indexer.put(1, c, 1);
        for (int r = 0; r < m.rows(); r ++)
            indexer.put(r, 5, 5);
        System.out.println("OpenCV Mat data:\n");

        for (int i = 0; i < m.rows(); i ++) {
            for (int j = 0; j < m.cols(); j ++) {
                System.out.print(" " + indexer.get(i, j));
            }
            System.out.println();
        }

        // image test
        new CVTest().run();
    }

    public void run() throws URISyntaxException {
        System.out.println("\nRunning DetectFaceDemo");
        String basePath = this.getClass().getProtectionDomain().getCodeSource().getLocation().toURI().getPath();
        basePath = basePath.substring(0, basePath.lastIndexOf(File.separator) + 1);
        System.out.println(basePath);

        // Create a face detector from the cascade file in the resources directory.
        CascadeClassifier faceDetector = new CascadeClassifier(basePath
                + BASE_RESOURCE_DIR + "/lbpcascade_frontalface.xml");
//        System.out.println(getClass().getResource(BASE_RESOURCE_DIR + "/lena.png").getPath());
        Mat image = opencv_imgcodecs.imread(basePath + BASE_RESOURCE_DIR + "/lena.png");
        System.out.format("height: %d, width: %d\n", image.arrayHeight(), image.arrayWidth());

        // Detect faces in the image.
        // MatOfRect is a special container class for Rect.
        RectVector faceDetections = new RectVector();
        faceDetector.detectMultiScale(image, faceDetections);
        System.out.println(String.format("Detected %s faces", faceDetections.size()));
        // Draw a bounding box around each face.
        for (int i = 0; i < faceDetections.size(); i ++) {
            Rect rect = faceDetections.get(i);
            opencv_imgproc.rectangle(image, new Point(rect.x(), rect.y()),
                    new Point(rect.x() + rect.width(), rect.y() + rect.height()), new Scalar(0, 255));
        }
        // Save the visualized detection.
        String filename = basePath + "/faceDetection.png";
        System.out.println(String.format("Writing %s", filename));
        opencv_imgcodecs.imwrite(filename, image);
    }
}
