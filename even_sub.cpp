#include <iostream>
#include <vector>
using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<int> a(n);
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }
        vector<int> res;   
        for (int i = 0; i < n; i++) {
            if (a[i] % 2 == 0) {
                res.push_back(i);
                break;
            }
        }
        if (res.empty()) {
            vector<vector<int>> ans = {{}};
            for (int i = 0; i < n && res.empty(); i++) {
                vector<vector<int>> temp;
                for (vector<int> p : ans) {
                    p.push_back(i);
                    int sum = 0;
                    for (int idx : p) {
                        sum += a[idx];
                    }
                    if (sum % 2 == 0) {
                        res = p;
                        break;
                    }
                    temp.push_back(p);
                }
                for (vector<int> q : temp) {
                    ans.push_back(q);
                }
            }
        }
        if (res.empty()) {
            cout << -1 << endl;
        } else {
            cout << res.size() << endl;
            for (int idx : res) {
                cout << idx + 1 << " ";
            }
            cout << endl;
        }
    }
    return 0;
}