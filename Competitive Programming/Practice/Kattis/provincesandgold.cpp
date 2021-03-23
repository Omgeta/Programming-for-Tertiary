#include <bits/stdc++.h>
using namespace std;

// There are 3 kinds of victory cards in Dominion:

// Province (costs 8, worth 6 victory points)

// Duchy (costs 5, worth 3 victory points)

// Estate (costs 2, worth 1 victory point)

// And, there are 3 kinds of treasure cards:

// Gold (costs 6, worth 3 buying power)

// Silver (costs 3, worth 2 buying power)

// Copper (costs 0, worth 1 buying power)

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int x, y, z;
    scanf("%d %d %d", &x, &y, &z);

    int c = x*3 + y*2 + z;

    string vc = (c >= 8) ? "Province" : ((c >= 5) ? "Duchy": ((c >= 2) ? "Estate" : ""));
    string tc = (c >= 6) ? "Gold" : ((c >= 3) ? "Silver" : "Copper");

    if (vc.length() == 0) {
        cout << tc << "\n";
    }
    else {
        cout << vc << " or " << tc << "\n";
    }

    return 0;
}