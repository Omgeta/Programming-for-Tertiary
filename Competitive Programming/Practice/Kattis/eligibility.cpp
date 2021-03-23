#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        string name, psd, dob;
        int c;
        cin >> name >> psd >> dob >> c;

        string eligibility = ((stoi(psd.substr(0, 4)) >= 2010) || (stoi(dob.substr(0, 4)) >= 1991)) ? "eligible" : ((c > 40) ? "ineligible" : "coach petitions");


        cout << name << " " << eligibility << "\n";
    }

    return 0;
}