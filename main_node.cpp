#include <iostream> 
#include <sstream> 
#include "ros/ros.h"
#include "std_msgs/String.h"

using namespace std; 

void chatterCallback(const std_msgs::String::ConstPtr& msg); 
void y_callbacl(const std_msgs::String::ConstPtr& msg);
void ang_callbacl(const std_msgs::String::ConstPtr& msg);


void x_callbacl(const std_msgs::String::ConstPtr& msg)
{
  ROS_INFO("I heard: [%s]", msg->data.c_str());
}

void y_callbacl(const std_msgs::String::ConstPtr& msg)
{
  ROS_INFO("I heard: [%s]", msg->data.c_str());
}

void ang_callbacl(const std_msgs::String::ConstPtr& msg)
{
  ROS_INFO("I heard: [%s]", msg->data.c_str());
}



int main(int argc, char **argv)
{
    ros::init(argc, argv, "Main Node"); 
    ros::NodeHandle n;
    ros::Subscriber x_sub = n.subscribe("position_x", 100, x_callbacl);
    ros::Subscriber y_sub = n.subscribe("position_y", 100, y_callbacl);
    ros::Subscriber ang_sub = n.subscribe("angle_cam", 100, ang_callbacl);
    ROS_INFO("Hello"); 
    return 0;
}
