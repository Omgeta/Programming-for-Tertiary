#include <bits/stdc++.h>
using namespace std;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    map<char, int> m;
    char c[2];
    while (scanf("%s", c) == 1) {
        m[c[0]]++;
    }

    int high = 0;
    for (map<char, int>::iterator it = m.begin(); it != m.end(); it++) {
        high = max(high, it->second);
    }
    printf("%d\n", high);

    return 0;
}