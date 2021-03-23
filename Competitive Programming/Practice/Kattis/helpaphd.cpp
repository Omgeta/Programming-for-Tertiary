#include <bits/stdc++.h>
using namespace std;
int main() {
    int n;
    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;

        if (s == "P=NP") {
            printf("skipped\n");
        } else {
            string a, b;
            bool found = false;
            for (int j = 0; j < s.length(); j++) {
                string curr = s.substr(j, 1);
                if (curr == "+") {
                    found = true;
                } else {
                    if (found) a += curr;
                    else b += curr;
                }
            }
            printf("%d\n", stoi(a) + stoi(b));
        }

    }


    return 0;
}