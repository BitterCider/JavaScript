    //Namespace = provides a soluton for preventing name conflicts in large projects
    //a namespace allos for identcally named entities as long as 
    //the namespaces are different.
    //example:

#include <iostream>

namespace first{
    int x = 1;
}
namespace second {
    int x = 2;
}
int main(){

    using namespace first;
    std::cout << x;
    //or
    std::cout << first::x;


    return 0;
} 
