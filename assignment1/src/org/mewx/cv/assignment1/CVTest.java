package org.mewx.cv.assignment1;

import org.opencv.core.*;
import org.opencv.imgcodecs.Imgcodecs;
import org.opencv.imgproc.Imgproc;
import org.opencv.objdetect.CascadeClassifier;

import java.io.File;
import java.net.URISyntaxException;

/**
 * Created by mewx on 6/04/17.
 * The test file for OpenCV java binding.
 */
public class CVTest {
    public static String BASE_RESOURCE_DIR = "/rc";
    static{ System.loadLibrary(Core.NATIVE_LIBRARY_NAME); }

    public static void main(String[] args) throws URISyntaxException {
        System.out.println("Welcome to OpenCV " + Core.VERSION);
        Mat m = new Mat(5, 10, CvType.CV_8UC1, new Scalar(0));
        System.out.println("OpenCV Mat: " + m);
        Mat mr1 = m.row(1);
        mr1.setTo(new Scalar(1));
        Mat mc5 = m.col(5);
        mc5.setTo(new Scalar(5));
        System.out.println("OpenCV Mat data:\n" + m.dump());

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
        System.out.println(getClass().getResource(BASE_RESOURCE_DIR + "/lena.png").getPath());
        Mat image = Imgcodecs.imread(basePath + BASE_RESOURCE_DIR + "/lena.png");
        System.out.format("height: %d, width: %d\n", image.height(), image.width());

        // Detect faces in the image.
        // MatOfRect is a special container class for Rect.
        MatOfRect faceDetections = new MatOfRect();
        faceDetector.detectMultiScale(image, faceDetections);
        System.out.println(String.format("Detected %s faces", faceDetections.toArray().length));
        // Draw a bounding box around each face.
        for (Rect rect : faceDetections.toArray()) {
            Imgproc.rectangle(image, new Point(rect.x, rect.y), new Point(rect.x + rect.width, rect.y + rect.height), new Scalar(0, 255, 0));
        }
        // Save the visualized detection.
        String filename = basePath + "/faceDetection.png";
        System.out.println(String.format("Writing %s", filename));
        Imgcodecs.imwrite(filename, image);
    }
}
