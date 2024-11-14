#include <iostream>

//cin >> (extraction operator)

int main(){
    std::string name;
    std::string age;

    std::cout << "What's your full name?: ";
    std::getline(std::cin >> std::ws, name); //if you want to use spaces and not just single words
   
    // "std::ws" is used to eliminate any spaces from being recieved as input.

    std::cout << "Hello! " << name << '\n';
    std::cout << "How old are you? " << name << '\n';
    std::cin >> age;

    std::cout << age << "? Wow!";


    return 0;
}