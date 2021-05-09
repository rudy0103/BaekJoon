//https://www.acmicpc.net/problem/2800
//괄호 제거

#include<iostream>
#include<string>
#include<queue>
#include<deque>
#include<stack>
#include<algorithm>
#include<fstream>

using namespace std;

priority_queue<string> pQ;
int ch[30];
int cnt;

void DFS(string str, int l){
    
    if(l>cnt){
        char a[201];
        string s="";
        for(int i=0; str[i]!='\0';i++){
            if(str[i]>='A' && str[i] <= 'Z'){
                if(ch[str[i]-'A']==1){
                    ch[str[i]-'A']=-1;
                    s+='(';
                }else if(ch[str[i]-'A']==-1)
                {
                    ch[str[i]-'A']=1;
                    s+=')';
                }

            }
            else{
                s+=str[i];
            }

        }
        pQ.push(s);

    }
    else{
            ch[l]=0;
            DFS(str,l+1);
            ch[l]=1;
            DFS(str,l+1);
    }
}

int main(){
    stack<char> S;
    deque<string> dQ;

    freopen("input.txt","rt",stdin);
    char str[300];
    cin>>str;
    string origin=str;
    int k=0;
    for(int i =0 ;str[i]!='\0';i++){
        cout<<"i:"<<i<<"str[i]:"<<str[i]<<endl;
        if(str[i]=='('){
            str[i]='A'+k;
            ch[k]=1;
            k++;
        }
    }
    cnt=k-1;
    for(int i =0 ; i <(int)origin.length();i++){
        S.push(str[i]);
        if(str[i]==')'){
            while(!(S.top()>='A'&& S.top()<='Z')){
                S.pop();
            }
            char a = S.top();
            str[i]=a;
            S.pop();
        }
    }
    // cout<<cnt;
    DFS(str,0);


    while (!pQ.empty())
    {
        string s=pQ.top();
        if(s!=origin) dQ.push_back(s);
        pQ.pop();
    }
    sort(dQ.begin(),dQ.end());
    dQ.erase(unique(dQ.begin(), dQ.end()), dQ.end());
    

    cnt=0;
    while(!dQ.empty()){
        string s= dQ.front();
        dQ.pop_front();
        // cout<<s<<endl;

    }
    // cout<<cnt;


    return 0;
}