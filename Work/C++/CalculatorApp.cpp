#include <iostream>

int main() {

   char op;
   double num1;
   double num2;
   double result;

   std::cout << "**** CALCULATOR ****\n";

   std::cout << "What operation would you like to perform (+, -, *, /)?: ";
   std::cin >> op;

   std::cout << "Enter num1: ";
   std::cin >> num1;

   std::cout << "Enter num2: ";
   std::cin >> num2;

   switch(op){
    case '+':
    result = num1 + num2;
    std::cout << "The result is: " << result;
    break;
    case '-':
    result = num1 - num2;
    std::cout << "The result is: " << result;
    break;
    case '*':
    result = num1 * num2;
    std::cout << "The result is: " << result;
    break;
    case '/':
    result = num1 / num2;
    std::cout << "The result is :" << result;
    break;

    default:
    std::cout << "That's illegal!";
       


   }

return 0; 
}