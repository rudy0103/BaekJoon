//https://www.acmicpc.net/problem/10828
//스택
#include<iostream>
#include<string>

using namespace std;

int arr[10001];
int n;
int point=-1;


void push(int item){
    point++;
    arr[point]=item;
}

void top(){
    if(point==-1) cout<<-1<<endl;
    else cout<<arr[point]<<endl;
}

void s_empty(){
    if(point==-1) cout<<1<<endl;
    else cout<<0<<endl;
}

void pop(){
    if(point==-1) cout<<-1<<endl;
    else {cout<<arr[point]<<endl;
    point--;}
}

void size(){
    cout<<point+1<<endl;
}

int main(){

    // freopen("input.txt","rt",stdin);
    ios::sync_with_stdio(false);
    int n;
    int i;
    string instruction;
    int item;
    cin>>n;

    for(i=1; i<=n; i++){
        cin>>instruction;

        if(instruction=="push"){
            cin>>item;
            push(item);
            
        }else if(instruction=="top"){
            top();
        }
        else if(instruction=="size"){
            size();
        }
        else if(instruction=="empty"){
            s_empty();
        }else if(instruction=="pop"){
            pop();
        }
    }



    return 0;
}