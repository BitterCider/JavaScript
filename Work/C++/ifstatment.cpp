#include <iostream>

int main(){

    //example of if statment:

    int age;

    std::cout << "What's your age: ";
    std::cin >> age;

    if(age >= 18){

        std::cout << "Welcome to the site!";
    }
    else if(age < 0){
        std::cout << "WTF?!";
    }
    
    else {
        std::cout << "Away with you!";
    }
}