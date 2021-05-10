//https://www.acmicpc.net/problem/2800
//괄호 제거

#include<iostream>
#include<string>
#include<queue>
#include<deque>
#include<stack>
#include<algorithm>

using namespace std;

deque<string> Q;
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
        Q.push_back(s);

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
    

    // freopen("input.txt","rt",stdin);
    char str[300];
    cin>>str;
    string origin=str;
    int k=0;
    for(int i =0 ; i <(int)origin.length();i++){
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

    DFS(str,0);


    sort(Q.begin(),Q.end());
    Q.erase(unique(Q.begin(), Q.end()), Q.end());
    

    while(!Q.empty()){
        string s= Q.front();
        if(s!=origin) cout<<s<<'\n';
        Q.pop_front();
    }


    return 0;
}