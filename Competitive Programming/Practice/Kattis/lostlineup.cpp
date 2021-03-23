#include <bits/stdc++.h>
using namespace std;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m[100];
    scanf("%d", &n);
    
    m[0] = 1;
    for (int i = 2; i <= n; i++) {
        int x;
        scanf("%d", &x);

        m[x+1] = i;
    }

    for (int i = 0; i < n; i++) {
        printf("%d ", m[i]);
    }

    return 0;
}