#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
    int t;
    cin >> t;

    while (t--) {
        long long a, b, c;
        cin >> a >> b >> c;

        long long diff = abs(a - b);
        long long ans;

        if (c <= diff) {
            ans = diff;
        }
        else {
            if (a >= b) {
                ans = diff + c;
            }
            else {
                ans = c - diff;
            }
        }
        cout << ans << '\n';
    }
    return 0;
}