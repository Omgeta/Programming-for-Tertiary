#include <bits/stdc++.h>
using namespace std;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    scanf("%d", &T);
    while (T--) {
        char a[80];
        scanf("%s", a);

        int total = 0, score = 1;
        for (int i = 0; i < strlen(a); i++) {
            if (a[i] == 'O') total += score++;
            else if (a[i] == 'X') score = 1;
        }
        printf("%d\n", total);
    }

    return 0;
}