#include <bits/stdc++.h>
using namespace std;

int main() {
    char month[3];
    int day;
    scanf("%3s %d", month, &day);
    if ((strcmp(month, "OCT") == 0 && day == 31) || (strcmp(month, "DEC") == 0 && day == 25)) {
        printf("yup");
    } else {
        printf("nope");
    }

    return 0;
}