#include "opencv2/imgproc.hpp"
#include "opencv2/imgcodecs.hpp"
#include "opencv2/highgui.hpp"
#include <iostream>
#include <vector>

using namespace cv;
using namespace std;

int main(int argc, char const *argv[])
{
    Mat inputImage = imread("../Data/lenna.png", IMREAD_GRAYSCALE);
    Mat binaryOutputImage, adaptiveOutputImage;
    vector<int> oneDImage;
    
    oneDImage = inputImage.reshape(0,1);

    cout<< "1D Image size: "<< oneDImage.size()<<endl;

    sort(oneDImage.begin(), oneDImage.end());

    int median = oneDImage.size()/2;

    cout<<"Median Pixel value: "<<oneDImage[median]<<endl;

    threshold(inputImage, binaryOutputImage, oneDImage[median], 255, THRESH_BINARY);

    imshow("Binarized Image", binaryOutputImage);
    waitKey();

    adaptiveThreshold(inputImage, adaptiveOutputImage, 225, ADAPTIVE_THRESH_MEAN_C, THRESH_BINARY_INV, 5, 2);
    imshow("Adaptive Image", adaptiveOutputImage);
    waitKey();

    return 0;
}
