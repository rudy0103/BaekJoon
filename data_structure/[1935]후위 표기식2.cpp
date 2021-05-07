//https://www.acmicpc.net/problem/1935
//후위 표기식2

#include<iostream>
#include<vector>
#include<string>
#include<stack>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    // freopen("input.txt","rt",stdin);
    int arr[27]={0};
    char ch[27]={'\0'};
    string op;
    stack<double> S;
    int n; cin>>n; // 1<=N<=26 A~Z;
    cin>>op;
    for(int i =0 ; i<n; i++){
        cin>>arr[i];
    }


    for(int i = 0; i<(int)op.length();i++){
        if(op[i]>='A' && op[i]<='Z'){
            int k=op[i]-'A';
            if(ch[k]=='\0'){
                ch[k]=op[i];
            }
        }
    }

    for(int i = 0; i<(int)op.length();i++){
        if(op[i]>='A' && op[i]<='Z'){
            S.push((double)arr[op[i]-'A']);
        }else{
            double a = S.top();
            S.pop();
            double b= S.top();
            S.pop();
            if(op[i]=='+'){
                double x= b+a;
                S.push(x);
            }
            else if(op[i]=='-'){
                double x = b-a;
                S.push(x);
            }
            else if(op[i]=='*'){
                double x = b*a;
                S.push(x);
            }
            else if(op[i]=='/'){
                double x = b/a;
                S.push(x);
            }

        }
    }


    cout << fixed;
    cout.precision(2);
    cout<<S.top();





    return 0;
}