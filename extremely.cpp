#include<iostream>
using namespace std;
int nonzero(int x){
    int check=0;
    while(x > 0){
        if(x % 10 != 0){
            check++;
        }
        x = x / 10;
    }
    return check;

}
int main(){
    int t;
    cin>>t;
    while (t--){
        int x;
        cin>>x;
        int count=0;
        for(int i=1;i<=x;i++){
            if (nonzero(i)==1){
                count++;
            }
        }
        cout<<count<<endl;

    }
}
         