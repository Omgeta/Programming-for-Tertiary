#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);

    int min = 1e9;
    int days = 0;
    for (int i = 0; i < n; i++) {
        int a;
        scanf("%d", &a);
        
        if (a < min) {
            min = a;
            days = i;
        }
    }
    printf("%d", days);

    return 0;
}