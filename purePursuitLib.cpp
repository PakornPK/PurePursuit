#include "purePursuitLib.h"

#define PI 3.14159265359

double pathCal::norm(double *pointA[2], double *pointB[2]){
    double defX,defY,dis; 
    defX = pointA[0]-pointB[0];
    defY = pointA[1]-pointB[1];
    dis = sqrt( pow(defX,2)+ pow(defY,2));
    return dis; 
}

double pathCal::radianCal(double L, double shortate){
    double R; 
    R = pow(L,2)/(2*shortate); 
    return  R; 
}

double pathCal::alpha(double ld, double eld){
    double alpha; 
    alpha = (asin(ld/eld) * 180.0)/PI;
    return alpha; 
}

double pathCal::KFactor(double alpha, double ld){
    double k; 
    k = (2 * sin((alpha*PI)/180.0))/ld; 
    return k ; 
}

double pathCal::zixma(double k){
    return (asin(k*30)*180.0)/PI;
}
