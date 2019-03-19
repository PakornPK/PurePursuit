#include <ros/ros.h> 
#include <cv_bridge/cv_bridge.h>
#include <opencv2/highgui/highgui.hpp>
#include <iostream>
#include <sstream>
#include <math.h>

using namespace std; 
using namespace cv; 

class cam{
    public: 
        double norm(Point2f A,Point2f B);
        Point midpoint(const Point& a, const Point& b);
        void drawAllTriangles(Mat& img, const vector< vector<Point> >& contours);
        cam(){
            VideoCapture cap(CV_CAP_ANY);
                
                if (!cap.isOpened()){
                    cout << "Cannot open the video cam" << endl;  
                }

                double dWidth = cap.get(CV_CAP_PROP_FRAME_WIDTH);
                double dHeight = cap.get(CV_CAP_PROP_FRAME_HEIGHT); 

                cout << "Frame size : " << dWidth << "x" << dHeight << endl;
                
                Mat img,gray,bw,new_img,canny_output;
                vector< vector<Point> > contours;
                vector<Vec4i> hierarchy;
                int thr (160); 
                int CV_THRESH_BINARY (0); 
                
                 
                while(1){
                    bool bSuccess = cap.read(img); 

                    if(!bSuccess){
                        cout << "Cannot read img frome video stream" << endl; 
                        break; 
                    }
                    new_img = img/5; 
                    cvtColor(img,gray, CV_BGR2GRAY); 
                    threshold(gray, bw, thr, 255, CV_THRESH_BINARY);
                    Canny( bw, canny_output, 100, 200, 3 );
                    findContours(canny_output,contours, CV_RETR_EXTERNAL, CV_CHAIN_APPROX_SIMPLE);
                    
                    int biggestContourIdx = -1;
                    float biggestContourArea = 0;
                    Mat drawing = Mat::zeros( bw.size(), CV_8UC3 );
                    for( int i = 0; i< contours.size(); i++ )
                    {
                        Scalar color = Scalar(0, 100, 0);
                        drawContours( drawing, contours, i, color, 1, 8, hierarchy, 0, Point() );

                        float ctArea= contourArea(contours[i]);
                        if(ctArea > biggestContourArea)
                        {
                            biggestContourArea = ctArea;
                            biggestContourIdx = i;
                        }
                    }

                    if(biggestContourIdx < 0)
                    {
                        cout << "no contour found" << endl;
                        //return 0;
                    }

                    drawAllTriangles(drawing,contours);

                    Rect r = Rect(50,50,540,380);
                    rectangle(img,r,Scalar(0,255,0),2,8,0);

                    imshow("Black and Write" ,bw); 
                    imshow("Candy image" ,canny_output); 
                    imshow("Normal image" ,img);
                    imshow("Triangles",drawing);

                    if (waitKey(30) == 27) {
                        cout << "esc key is pressed by user" << endl;
                        break;
                    }
                }
                
        }

        ~cam(){
            cvDestroyWindow("Camera_Output"); 
        }

};

double cam::norm(Point2f A,Point2f B){
    double X,Y,l; 
    Y = A.x - B.x; 
    X = A.y - B.y;
    l = sqrt(pow(X,2)+pow(Y,2)); 
    return l; 
}

Point cam::midpoint(const Point& a, const Point& b) {
    Point ret;
    ret.x = (a.x + b.x) / 2;
    ret.y = (a.y + b.y) / 2;
    return ret;
}
vector<float> pak_data; 

void cam::drawAllTriangles(Mat& img, const vector< vector<Point> >& contours){
    vector<Point> approxTriangle;
    for(size_t i = 0; i < contours.size(); i++){
        approxPolyDP(contours[i], approxTriangle, arcLength(Mat(contours[i]), true)*0.05, true);
        if(approxTriangle.size() == 3){
            drawContours(img, contours, i, Scalar(0, 255, 255), CV_FILLED); // fill GREEN
            vector<Point>::iterator vertex;
            for(vertex = approxTriangle.begin(); vertex != approxTriangle.end(); ++vertex){
                circle(img, *vertex, 3, Scalar(0, 0, 255), 1);
                vertex -> pak_data ; 
                cout << pak_data << endl;
            }
        }
    }
}


int main(int argc, char **argv)
{
    system("clear");
    ros::init(argc, argv, "internal_cam_test");
    cam cam_object; 

    ROS_INFO("Cam_Tested!"); 
    return 0;
}
