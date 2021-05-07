//https://www.acmicpc.net/problem/2504
//괄호의 값

#include<iostream>
#include<stack>
#include<string>


using namespace std;

bool isNumber(const string& str)
{
    for (char const &c : str) {
        if (isdigit(c) == 0) return false;
    }
    return true;
}

bool is_correct(char a[]){

    stack<char> S;
    for(int i = 0; a[i]!='\0';i++){
        if(a[i]=='['||a[i]=='('){
            S.push(a[i]);
        }
        else if(a[i]==']'){
            if(S.empty()) return false;
            if(S.top()=='['){
                S.pop();
            }
            else return false;
        }else if(a[i]==')'){
            if(S.empty()) return false;
            if(S.top()=='('){
                S.pop();
            }
            else return false;
        }

    }
    if(S.empty()) return true;
    else return false;


}

int main(){
    // freopen("input.txt","rt",stdin);
    char str[40];
    cin>>str;
    stack<string> S;

    if(is_correct(str)){
        for(int i = 0 ;str[i]!='\0';i++){
            if(str[i]=='('){
                S.push("(");
            }
            else if(str[i]=='['){
                S.push("[");
            }
            else if(str[i]==')' && S.top()=="("){
                S.pop();
                S.push("2");
            }else if(str[i]==']' && S.top()=="["){
                S.pop();
                S.push("3");
            }
            else if(str[i]==')' && isNumber(S.top())==true){
                int sum = 0;
                while(S.top()!="("){
                    int n = stoi(S.top());
                    S.pop();
                    sum+=n;
                }
                S.pop();
                sum=sum*2;
                string num= to_string(sum);
                S.push(num);
            }
            else if(str[i]==']' && isNumber(S.top())==true){
                int sum = 0;
                while(S.top()!="["){
                    int n = stoi(S.top());
                    S.pop();
                    sum+=n;
                }
                S.pop();
                sum=sum*3;
                string num= to_string(sum);
                S.push(num);
            }
        }
        int sum =0;
        while(!S.empty()){
            int n = stoi(S.top());
            S.pop();
            sum+=n;
        }
    cout<<sum<<'\n';
    }
    else cout<<0<<endl;

    return 0;
}