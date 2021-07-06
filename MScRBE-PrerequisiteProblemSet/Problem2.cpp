#include <iostream>
using namespace std;

string String;

string searchX(string s){
    for (int i = 0; i < s.length(); i++) {
        if (s[i] == 'x')
            return "yes";
    }
    return "no";
}

int main() {
    cout<<"Enter a string here to search for 'x': "<<endl;
    getline (cin, String);
    cout<<searchX(String);
}