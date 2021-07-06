#include <iostream>
using namespace std;

int Factorial(int num) {
    int fact = 1;
    while (num > 1) {
        fact = fact * num;
        num--;
    }
    return fact;
}

int main() {
    cout<<"Enter an integer number: ";
    int number;
    cin>>number;
    cout<<"Factorial of the number is: "<<Factorial(number);
}