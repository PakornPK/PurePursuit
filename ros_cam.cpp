#include <ros/ros.h> 
#include <cv_bridge/cv_bridge.h>
#include <opencv2/highgui/highgui.hpp>
#include <iostream>
#include <sstream>
#include <math.h>

#define PI 3.14159265

using namespace std; 
using namespace cv; 

class cam{
    public: 
        double norm(Point2f A,Point2f B);
        Point midpoint(const Point& a, const Point& b);

        cam(){
            VideoCapture cap(CV_CAP_ANY);
                
                if (!cap.isOpened()){
                    cout << "Cannot open the video cam" << endl;  
                }

                double dWidth = cap.get(CV_CAP_PROP_FRAME_WIDTH);
                double dHeight = cap.get(CV_CAP_PROP_FRAME_HEIGHT); 

                cout << "Frame size : " << dWidth << "x" << dHeight << endl;
                
                Mat img,gray,bw,new_img,drawing;
                drawing = Mat::zeros( bw.size(), CV_8UC3 );
                vector< vector<Point> > contours;
                vector<Vec4i> hierarchy;
                
                int thr (203); 
                int CV_THRESH_BINARY (0); 
                int biggestContourIdx (-1);
                float biggestContourArea (0);
                double base_car[3],head_car[3]; 
                
                 
                while(1){
                    bool bSuccess = cap.read(img); 

                    if(!bSuccess){
                        cout << "Cannot read img frome video stream" << endl; 
                        break; 
                    }
                    new_img = img/5; 
                    cvtColor(img,gray, CV_BGR2GRAY); 
                    threshold(gray, bw, thr, 255, CV_THRESH_BINARY);
                    findContours(bw,contours, CV_RETR_EXTERNAL, CV_CHAIN_APPROX_SIMPLE);
                    
                    
                    
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
                    }

                    vector<Point> approxTriangle;
                    Point2f pos_car,front_car;      
                    for(size_t i = 0; i < contours.size(); i++){
                        approxPolyDP(contours[i], approxTriangle, arcLength(Mat(contours[i]), true)*0.05, true);
                        if(approxTriangle.size() == 3){

                            line(img,approxTriangle[0],approxTriangle[1],Scalar(0,255,255),3,8,0);
                            line(img,approxTriangle[1],approxTriangle[2],Scalar(0,255,255),3,8,0);
                            line(img,approxTriangle[2],approxTriangle[0],Scalar(0,255,255),3,8,0);

                            base_car[0] = norm(approxTriangle[0],approxTriangle[1]);
                            base_car[1] = norm(approxTriangle[1],approxTriangle[2]);
                            base_car[2] = norm(approxTriangle[2],approxTriangle[0]);

                            if(base_car[0] < base_car[1] && base_car[0] < base_car[2]){
                                pos_car = midpoint(approxTriangle[0],approxTriangle[1]);
                            }
                            else if (base_car[1] < base_car[0] && base_car[1] < base_car[2])
                            {
                                pos_car = midpoint(approxTriangle[1],approxTriangle[2]);
                            }else
                            {
                                pos_car = midpoint(approxTriangle[2],approxTriangle[0]);
                            }
                            
                            head_car[0] = norm(pos_car,approxTriangle[0]);
                            head_car[1] = norm(pos_car,approxTriangle[1]);
                            head_car[2] = norm(pos_car,approxTriangle[2]);

                            if (head_car[0] > head_car[1] && head_car[0] > head_car[2]) {
                                front_car = approxTriangle[0];
                            }else if (head_car[1] > head_car[0] && head_car[1] > head_car[2])
                            {
                                front_car = approxTriangle[1];
                            }else
                            {
                                front_car = approxTriangle[2];
                            }
                            
                            circle(img,front_car,3,Scalar(0,0,255),3,8,0);
                            circle(img,pos_car,3,Scalar(0,0,255),3,8,0);
                            line(img,pos_car,front_car,Scalar(0,0,255),1,8,0);

                            
                            double x_ref,y_ref,body_car,x_base,pX,pY,l_base,angle_car;
                            body_car = norm(pos_car,front_car);

                            x_ref = front_car.x;
                            y_ref = pos_car.y;  
             
                            pX = pos_car.x - x_ref; 
                            pY = pos_car.y - y_ref;
                            l_base = sqrt(pow(pX,2)+pow(pY,2)); 

                            angle_car = acos(l_base/body_car) * 180.0 / PI; 

                            cout << angle_car << endl;  

                            line(img,pos_car,Point(x_ref,y_ref),Scalar(255,0,0),1,8,0);
                            line(img,front_car,Point(x_ref,y_ref),Scalar(255,0,0),1,8,0);
                            
                        }
                    }

                    Rect r = Rect(50,50,540,380);
                    rectangle(img,r,Scalar(0,255,0),2,8,0);
                        
                    imshow("Normal image" ,img);

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

double cam::norm(Point2f A, Point2f B){
    double X,Y,l; 
    X = A.x - B.x; 
    Y = A.y - B.y;
    l = sqrt(pow(X,2)+pow(Y,2)); 
    return l; 
}

Point cam::midpoint(const Point& a, const Point& b) {
    Point ret;
    ret.x = (a.x + b.x) / 2;
    ret.y = (a.y + b.y) / 2;
    return ret;
} 

int main(int argc, char **argv)
{
    system("clear");
    ros::init(argc, argv, "internal_cam_test");
    cam cam_object; 

    ROS_INFO("Cam_Tested!"); 
    return 0;
}
