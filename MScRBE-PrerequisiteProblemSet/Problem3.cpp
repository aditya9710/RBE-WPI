#include <iostream>
#include <stack>

using namespace std;

bool isValid(string s) {
    stack <char> expression;
    bool validity = false;
    if (s.length() < 2) return validity;
    
    for (int i = 0; i< s.length(); i++) {
        if (s[i] == ')' || s[i] == '}' || s[i] == ']') {
            if (expression.size() == 0) return validity;
            switch(s[i]){
                case ')':
                    if (expression.top() != '(') return validity;
                    expression.pop();
                    break;
                case '}':
                    if (expression.top() != '{') return validity;
                    expression.pop();
                    break;
                case ']':
                    if (expression.top() != '[') return validity;
                    expression.pop();
                    break;
                default:
                    return validity;
            }
        }
        else
            expression.push(s[i]);
    }
    if (!expression.size()) 
        validity = true;
    return validity;
}

int main() {
    cout<<"Enter an expression within double quotes (\"\"): ";
    string s;
    getline(cin, s);
    cout<<isValid(s);
    return 0;
}