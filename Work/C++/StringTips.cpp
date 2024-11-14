#include <iostream>

int main(){

    std::string name;

    std::cout << "Enter your name: ";
    std::getline(std::cin, name); //getline - includes spaces within a string in output

    //".length()" - gives length of a string
    //".empty()" - boolian value
    //".clear()" - clears string
    //".append()" - adds another string immedietly after the string
    // ".at()" - 

 //   if(name.length() > 12){
       // std::cout << "Your name is too long";


    
//else{

  //  std::cout << "Welcome " << name;


    //if(name.empty()){
    //    std::cout << "You didn't enter your name";

//else{
  //  std::cout << "Hello " << name;

//return 0;

name.append("@gmail.com");
std::cout << "you email is: " << name;


return 0;
    
}