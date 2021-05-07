//https://www.acmicpc.net/problem/9012
//괄호

#include<iostream>
#include<string>
#include<stack>

using namespace std;

int is_VPS(string str){
    stack<char> S;
    int len = (int)str.length();


    for(int i=0;i<len;i++){
        if(str[i]=='(') S.push(str[i]);
        else{
            if(S.empty()) return 0;
            else{
                S.pop();
            }

        }
    }

    if(S.empty()) return 1;
    else return 0;
}

int main(void){

    // freopen("input.txt","rt",stdin);
    int n;    
    int res;
    cin>>n;

    for(int i=0; i<n; i++){
        string ps;
        cin>>ps;
        res=is_VPS(ps);

        if(res==1) cout<<"YES"<<endl;
        else cout<<"NO"<<endl;
    }

    return 0;

}