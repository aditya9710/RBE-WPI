#include <iostream>

using namespace std;

double evaluate(string s) {

    string compactExpression = "";

    for (int i = 0; i < s.length(); i++) {
        if (s[i] != ' '){
            compactExpression = compactExpression + s[i];
        }
    }

    string semiStatement = ""; // Do parantheses first
    for (int i = 0; i < compactExpression.length(); i++)
    {
        if (compactExpression[i] == '(')
        {
            int paranthesis = 1;
            string subExpression;
            i++;
            while (true)
            {
                if (compactExpression[i] == '(') {
                    paranthesis++;
                }

                else if (compactExpression[i] == ')') {
                    paranthesis--;
                    if (paranthesis == 0)
                    {
                        i++;
                        break;
                    }
                }
                subExpression += compactExpression[i];
                i++;
            }
            semiStatement += to_string(evaluate(subExpression));
        }
        semiStatement += compactExpression[i];
    }

    for (int i = 0; i < semiStatement.length(); i++)
    {
        if (semiStatement[i] == '*') {
            return evaluate(semiStatement.substr(0, i)) * evaluate(semiStatement.substr(i+1, semiStatement.length()-i-1));
        } 
        
        else if (semiStatement[i] == '/') {
            return evaluate(semiStatement.substr(0, i)) / evaluate(semiStatement.substr(i+1, semiStatement.length()-i-1));
        }

        else if (semiStatement[i] == '+')
        {
            return evaluate(semiStatement.substr(0, i)) + evaluate(semiStatement.substr(i+1, semiStatement.length()-i-1));
        } 
        
        else if (semiStatement[i] == '-') {
            return evaluate(semiStatement.substr(0, i)) - evaluate(semiStatement.substr(i+1, semiStatement.length()-i-1));
        }
    }

    return stod(semiStatement.c_str());
}

int main() {

    cout<<"Enter an expression within double quotes (\"\"): ";
    string s;
    getline(cin, s);
    if(s[0] == '\"' && s[s.length() - 1] == '\"') {
        s = s.substr(1, s.length() -2);
        cout<<evaluate(s);
    }
    else
        cout<<"Expression must inculude quotes";
    return 0;
}