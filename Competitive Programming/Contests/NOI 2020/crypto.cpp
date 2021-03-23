#include <bits/stdc++.h>
using namespace std;

#define MOD 1000000007

typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vll;

ll N;
vi A, B;

int fac(int x) {
    int res = 1;
    for (int i = 1; i <= x; i++) {
        res *= i;
    }
    return res;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    cin >> N;
    for (int i = 0; i < N; i++) {
        int input;
        cin >> input;
        if (find(A.begin(), A.end(), input) == A.end())
            A.push_back(input); B.push_back(input);
    }

    ll fn = fac(N);

    sort(B.begin(), B.end());


    map<vi, int> permutations;
    for (int i = 0; i < fn; i++) {
        permutations[B] = i;
        next_permutation(B.begin(), B.end());
    }

    cout << (permutations[A] + 1) % MOD;

    return 0;
}
