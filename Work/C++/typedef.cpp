#include <iostream>
#include <vector>
//typedef = reserved keyword used to create 
    //an additional name (alias) for anyohter data type
    //new identifier for an existing type
    //helps with readabillity and reduces typos, example:
    //type has been replaced with 'using' (works better w/ tmeplates)

//typedef std::string text_t;
//typedef int number_t;
using text_t = std::string;
using number_t = int;

int main(){

    text_t firstName = "Tal";
    number_t age = 28;

    std::cout << firstName << '\n';
    std::cout << "You are "<< age << '\n'; 


    
    return 0;

}