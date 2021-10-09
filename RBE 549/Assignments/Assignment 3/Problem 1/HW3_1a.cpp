#include "opencv2/core/core.hpp"
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include "iostream"

using namespace cv;
using namespace std;

int main(int argc, char const *argv[])
{
    Mat src;
    src = imread("../Data/lenna.png", IMREAD_COLOR);
    namedWindow( "Original Image", WINDOW_AUTOSIZE);
    imshow( "Original Image", src);

    Mat grey;
    cvtColor(src, grey, COLOR_BGR2GRAY);

    Mat sobelx;
    Sobel(grey, sobelx, CV_32F, 1, 0);

    double minVal, maxVal;
    minMaxLoc(sobelx, &minVal, &maxVal);    //find minimum and maximum intensities
    cout << "minVal : " << minVal << endl << "maxVal : " << maxVal << endl;

    Mat draw;
    sobelx.convertTo(draw, CV_8U, 255.0/(maxVal - minVal), -minVal * 255.0/(maxVal - minVal));

    namedWindow("Sobel Image", WINDOW_AUTOSIZE);
    imshow("Sobel Image", draw);

    waitKey(0);                                        
    return 0;
}
