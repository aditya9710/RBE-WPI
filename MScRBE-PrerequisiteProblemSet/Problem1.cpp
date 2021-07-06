#include <iostream>
using namespace std;

int Factorial(int num){
    int fact = 1;
    while(num > 1) {
        fact = fact * num;
        num--;
    }
    return fact;
}

int main(int argc, char *args[]) {
    std::cout<<"Enter a positive number: "<<endl;
    int number = 0;
    std::cin>>number;
    cout<<"The factorial is: "<<Factorial(number);
    return 0;
}