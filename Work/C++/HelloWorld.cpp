#include <iostream> 

int main(){
    
    //integer (whole number)
    int x; //decleration
    x = 5;
    int age = 28;
    int year = 2023;
    
    //double (number with decimal)
    double price = 21.99;
    double temp = 25.2;
   

    //char (single text)
    char grade = 'A';
    char intial = 'T';
    
    
    // boolean (true or false)
    bool student = false;
    bool power = true;
    bool forsale = true;
    
    //string (a sequence of text)
    std::string name = "Tal";
    std::string day = "Friday";

    

    //const - const keyowrd specifies that variable's value is constant
    //it tells the compuler to prevent anything from modifying it
    //so its effectivley (read only), example:

    const double PI = 3.14159;
    PI = 420.69;
    double radius = 20;
    double circumference = 2* PI * radius;
    std::cout << circumference << "cm";



    //Namespace = provides a soluton for preventing name conflicts in large projects
    //a namespace allos for identcally named entities as long as 
    //the namespaces are different.
    //example:

    int x = 0;
    int x = 1;









    return 0;
}
