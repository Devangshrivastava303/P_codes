#include<iostream>
#include<string>
using namespace std;

string is_even(string &s,int i,int j){
    if (j>=s.length()){
        return "YES";
    }
    if(s[i]!=s[j]){
        return "NO";
    }
    return is_even(s,i+1,j+1);
}
int main(){
    int t;
    cin>>t;

    while (t--){
        string s;
        cin>>s;
        int i=0;
        int j =s.length()/2;
        if (s.length()%2==0){
            cout<<is_even(s,i,j)<<endl;
        }
        else if (s.length()%2!=0)
        {
            cout<<"NO"<<endl;
        }
    }
    return 0;
}