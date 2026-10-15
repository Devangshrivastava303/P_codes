#include <iostream>
#include <string>
using namespace std;

string change(string &s, int i, int j, int times) {
    if (i >= j) {
        if (times == 1) return "YES";
        if (times == 0 && s.length() % 2 == 1) return "YES";
        return "NO";
    }

    if (s[i] != s[j]) {
        if (times == 1) return "NO";
        s[i] = s[j];
        times++;
    }

    return change(s, i + 1, j - 1, times);
}

string check(string &s) {
    return change(s, 0, s.length() - 1, 0);
}

int main() {
    string s;
    cin >> s;
    cout << check(s) << endl;
    return 0;
}