#include<iostream>
using namespace std;
int main(){
    int t;
    cin>>t;
    while(t--){
        int n;
        int k;
        cin>>n;
        cin>>k;
       cout <<(1<<(n-k+1))+2*(k-1)<<endl;
    }
}