#include <iostream>

int main(){

// && = and, check if 2 conditions are true
// || = check IF AT LEAST 1 of 2 conditions are true
// ! = reverses the logical state of its operand, if its true, then false.

int temperature;
bool sunny = true;

std::cout << "Enter Temp: ";
std::cin >> temperature;

if(temperature > 20 && temperature < 30){
    std::cout << "It's nice outside!\n";
}
else{
    std::cout << "GET IN THE BUNKER!\n";
}

if(!sunny){
    std::cout << "It is cloudy outside";

}
else {
    std::cout << "It is sunny outside";
}
return 0;

    
}
