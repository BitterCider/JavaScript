#include <iostream>

int main(){

    double temp;
    char unit;

    std::cout << "What unit would you like to convert to?: ";
    std::cin >> unit;

switch(unit){
    case 'C':
    std::cout << "Enter temperature in F: \n";
    std::cin >> temp;
    temp = ((temp - 32) * 0.555);
    std::cout << "The temperatrue in Celsius is: " << temp << "C";
    break;

    case 'F':
    std::cout << "Enter temperature in C: \n";
    std::cin >> temp;
    temp = (temp * 9/5) + 32;
    std::cout << "The temperatrue in Farenheit is: " << temp << "F";
    break;

    
}

return 0;
}