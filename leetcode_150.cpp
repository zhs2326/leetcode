/*
This is a good question to test your understanding of stack.
The logic is pretty simple. There are two cases: (1) It's an operator. (2) It's a number.
For the first case, we should pop two numbers from the stack and calculate the result with the operator.
For the second case, we should push the number into the stack and wait for future operator.
Finally, there must be only one number in the stack, which is the result. (Since the given expression is always valid)
*/

class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> s;
        unordered_set<string> op;
        op.insert("+");
        op.insert("-");
        op.insert("*");
        op.insert("/");
        
        for(auto token: tokens){
            if(op.find(token) == op.end())
                s.push(atoi(token.c_str()));
            else{
                int n1 = int(s.top());
                s.pop();
                int n2 = int(s.top());
                s.pop();
                int n3;
                if(token == "+")
                    n3 = n1+n2;
                else if(token == "-")
                    n3 = n2-n1;
                else if(token == "*")
                    n3 = n1*n2;
                else if(token == "/")
                    n3 = n2/n1;
                s.push(n3);
            }
        }
        
        int res = s.top();
        s.pop();
        
        return res;
        
    }
};
