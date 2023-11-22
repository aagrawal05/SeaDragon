#include <opencv2/opencv.hpp>

int main()
{
    // Create a VideoCapture object to capture video from the default camera
    cv::VideoCapture cap(0);

    // Check if the camera opened successfully
    if (!cap.isOpened())
    {
        std::cerr << "Error: Camera could not be opened" << std::endl;
        return -1;
    }

    // Create a window to display the stream
    cv::namedWindow("Camera Stream", cv::WINDOW_AUTOSIZE);

    // Frame to hold each captured image
    cv::Mat frame;

    while (true)
    {
        // Capture a new frame from the camera
        cap >> frame;

        // If the frame is empty, break immediately
        if (frame.empty())
        {
            break;
        }

        // Display the resulting frame in the created window
        cv::imshow("Camera Stream", frame);

        // Wait for 1 ms and break the loop if 'Esc' key is pressed
        if (cv::waitKey(1) == 27)
        {
            break;
        }
    }

    // Release the VideoCapture object
    cap.release();
    // Destroy all windows
    cv::destroyAllWindows();

    return 0;
}
