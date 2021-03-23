#include <bits/stdc++.h>
using namespace std;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    scanf("%d", &n);
    char a[1000];
    scanf("%*s%*s%*s%s%*s", a);

    for (int i = 0; i < n; i++) {
        if (a[4*i + 1] == '*') printf("1");
        else if (a[4*i + 0] == '*') printf("2");
        else printf("3");
    }
    printf("\n");

    return 0;
}