#include "opencv2/imgproc.hpp"
#include "opencv2/imgcodecs.hpp"
#include "opencv2/highgui.hpp"

using namespace cv;
using namespace std;

int main(int argc, char const *argv[])
{
    Mat inputImage = imread("../Data/lennaNoisy.png", IMREAD_GRAYSCALE);
    
    imshow("Input Image", inputImage);

    Mat boxOutput, gaussianOutput, medianOutput, kernel;

    Point anchor(-1,-1);
    double delta = 0;
    int ddepth = -1, kernel_size = 3, sigmaX = 5, sigmaY = 5;

    kernel = Mat::ones(kernel_size, kernel_size, CV_32F )/ (float)(kernel_size*kernel_size);

    filter2D(inputImage, boxOutput, ddepth , kernel, anchor, delta, BORDER_DEFAULT );

    GaussianBlur(inputImage, gaussianOutput, Size(0,0), sigmaX, sigmaY);

    kernel_size = 5;

    medianBlur(inputImage, medianOutput, kernel_size);

    imshow("Box Filter", boxOutput);
    imshow("Gaussian Filter", gaussianOutput);
    imshow("Median Filter", medianOutput);
    waitKey(0);
    
    return 0;
}
