//https://www.acmicpc.net/problem/1343
//폴리오미노

#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<queue>

#define INF 2147000000

using namespace std;

vector<string> res;
queue<int> Q;

int main(){
    int cnt=0;
    // freopen("input.txt","rt",stdin);
    string str;
    bool impossible= false;
    cin>>str;


    int k = 0;
    for(int i =0; i<(int)str.length(); i++){
        if(str[i]=='X'){
            cnt++;
        }
        else{
            Q.push(cnt);
            Q.push(-1);
            cnt=0;
        }
    }
    Q.push(cnt);

    string res="";
    while (!Q.empty())
    {
        int tmp=Q.front();
        Q.pop();
        if(tmp!=-1 && tmp%2!=0){
            impossible=true;
        }
        else if(tmp==-1){
            res+=".";
        }
        else if(tmp==2){
            res+="BB";
        }
        else if(tmp>=4){
            int k = tmp/4;
            int l = tmp%4;
            for(int i = 0; i<k; i++){
                res+="AAAA";
            }
            if(l==2){
                res+="BB";
            }
        }
    }

    if(impossible){
        cout<<-1;
    }else{
        cout<<res;
    }
    

    return 0;
}