#include <iostream>
#include <cmath>

int main(){

    //double x = 3.4;
    //double y = 4;
    //double z;

    //z = std::max(x, y); //the highest number of the two defined
    //z = std::min(x, y); // the lowest number of the two defined
    //z = pow(2, 3); // power to
    //z = sqrt(9); // square root
    //z = abs(-3); // absolute num
    //z = round (x); // round number
    //z = ceil(x); // number above
    //z = floor(x); // number below

    //Hypotenuse Calculator:

    double hyp;
    double x;
    double y;

    std::cout << "Value of x: "; 
    std::cin >> x;
    std::cout << "Value of y: ";
    std::cin >> y;
    hyp = sqrt(pow(x, 2) + pow(y, 2));
    std::cout << "The longest side of the triangle is: " << hyp;

    








    


   




    return 0;
}