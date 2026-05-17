//文字列Sの前後からN文字ずつ取り除いた文字列を作成したい
//S は英小文字からなる文字列
//N は整数
//2N+1≤∣S∣≤30
//1≤N≤10
#include <iostream>
#include <string>
using namespace std;

int main() {
    string S;
    int N;

    cin >> S >> N;

    string ans = S.substr(N, S.size() - 2 * N);

    cout << ans << endl;

    return 0;
}