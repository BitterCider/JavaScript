#include <iostream>

main (){

    //type conversion = converting a value of one data type to another
    // implicit = automatic
    // explicit = precede value with new data type (int):

    //implicit example:

    //int x = 3.14;

    //std::cout << x;

    //explicit example:

    //double x = (int) 3.14;

    //std::cout << x;

    // implicit example:
    //char x = 100;
    //std::cout << x; // this will print the char the number 100 represents - "d"

    //explicit example:
    int correct = 8;
    int questions = 10;
    double score = correct/(double)questions * 100;

    //the "(double)" has to be there since a division of 8 by 10 would yield a 0 (int)

    std::cout << score;

    return 0;

    


}