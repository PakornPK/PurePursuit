#include <math.h>

using namespace std;

class pathCal{
    public:
    double norm(double pointA[2], double pointB[2]); 
    double radianCal(double L, double shortate);
    double alpha(double ld, double eld); 
    double KFactor(double alpha, double ld);
    double zixma(double k); 
};

