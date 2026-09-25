#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
    int t;
    cin >> t;
    while(t--)
    {
        int n;
        cin >> n;
        vector<int> a(n);
        for(int &x : a)
        {
            cin >> x;
        }
        vector<int> b;
        vector<int> c;
        int index = 0;
        for(int &x : a)
        {
            if(x != index + 1)
            {
                b.push_back(x);
                c.push_back(index + 1);
            }
            index++;
        }
        reverse(b.begin(), b.end());

        cout << (b == c ? "YES" : "NO") << endl;
    }

    return 0;
}