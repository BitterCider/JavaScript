#include <iostream>

int main(){

char note;

std::cout << "Whats your favorite note?: ";
std::cin >> note;

switch(note){
  case 'E':
   std::cout << "Metallica!";
   break;
  
  case 'B':
   std::cout << "Cool";
   break;
  
  case 'D':
   std::cout << "Happy!";
   break;

  case 'C':
   std::cout << "Common!";
   break;

  case 'G':
   std::cout << "Anyway here's Wonderwall..";
   break;

  case 'A':
   std::cout << "Versatile";
   break;
 default:
  std::cout << "That's not a musical note!";


   }
return 0;

 }



  
