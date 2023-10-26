#include <opencv2/opencv.hpp>
#include <iostream>

using namespace cv;

VideoCapture videoCapture(0);
//VideoCapture videoCapture("/dev/video0", CAP_V4L2);

void exit_node(bool hasFaulted = false) {
    videoCapture.release();
    destroyAllWindows();
    exit(hasFaulted);
}

void crit_error(const std::string &errMsg) {
    std::cerr << errMsg << std::endl;
    exit_node(true);
}

void set_cap_properties(int width = 1280, int height = 720, int fps = 120) {
    //videoCapture.set(CAP_PROP_FOURCC ,('M', 'J', 'P', 'G') );
    videoCapture.set(CAP_PROP_FRAME_WIDTH, width);
    videoCapture.set(CAP_PROP_FRAME_HEIGHT, height);
    videoCapture.set(CAP_PROP_FPS, fps);
}

int main() {
    set_cap_properties(1920, 1080, 25);
    if (!videoCapture.isOpened()) crit_error("Error opening video stream or file");

    // Read the frames to the last frame
    while (videoCapture.isOpened()) {
        Mat frame;
        if (!videoCapture.read(frame)) crit_error("No frames in buffer, camera may have disconnected");
        Mat rsizd_frame;
        resize(frame, rsizd_frame, Size(480, 360), INTER_LINEAR);
        Mat bwFrame;
        cvtColor(rsizd_frame, bwFrame, COLOR_BGR2GRAY);
        imshow("Frame", frame);

        if (waitKey(1) == 'q') {
            exit_node();
        }
    }
    crit_error("camera connection closed unexpectedly");
}