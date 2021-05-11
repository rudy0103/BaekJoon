//https://www.acmicpc.net/problem/1541
//잃어버린 괄호

#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<stack>

#define INF 2147000000

using namespace std;


int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    // freopen("input.txt","rt",stdin);
    string str; cin>>str;
    stack<int> S;
    bool flag=true;//마이너스가 안나오면 flag는 계속 true 마이너스가 나온후로는 false 모든 수를 빼면됨
    int res=0;
    string s_num="";
    for(int i = 0 ; i<(int)str.length(); i++){
        if(str[i]!='+' && str[i]!='-'){
            s_num+=str[i];
        }else if(str[i]=='+'){
            int num = stoi(s_num);
            if(flag==true){
                res+=num;
            }else{
                res-=num;
            }
            s_num="";
        }else if(str[i]=='-'){
            int num = stoi(s_num);
            if(flag==true){
                res+=num;
            }else{
                res-=num;
            }
            flag=false;
            s_num="";
        }
    }
    if(flag==true){
         int num = stoi(s_num);
        res+=num;
    }else{
        int num = stoi(s_num);
        res-=num;
    }
 


    cout<<res;

    return 0;
}