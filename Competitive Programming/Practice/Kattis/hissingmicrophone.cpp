#include <bits/stdc++.h>
using namespace std;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    char x[30];
    scanf("%s", x);

    bool found = false;
    for (int i = 1; i < strlen(x); i++) {
        if (x[i-1] == x[i] && x[i] == 's') {
            found = true;
            break;
        }
    }

    printf("%shiss", found ? "" : "no ");

    return 0;
}