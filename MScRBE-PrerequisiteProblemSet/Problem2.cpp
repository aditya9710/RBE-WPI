#include <iostream>
using namespace std;

string searchX(string s) {
    for(int i = 0; i < s.length(); i++) {
        if (s[i] == 'x') 
            return "yes";
    }
    return "no";
}

int main() {
    cout<<"Enter a string: ";
    string s;
    getline(cin, s);
    cout<<searchX(s);
}