#include <iostream>
using namespace std;

int digitSum(int n) {
    int sum = 0;
    while(n > 0) {
        sum += n % 10;
        n /= 10;
    }
    return sum;
}

int main() {
    int t;
    cin >> t;
    while(t--) {
        int x;
        cin >> x;
        int count = 0;
        for(int y = x; y <= x + 100; y++) {
            if(y - digitSum(y) == x) {
                count++;
            }
        }
        cout << count << endl;
    }
    return 0;
}