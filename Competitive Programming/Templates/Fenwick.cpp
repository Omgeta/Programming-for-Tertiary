#include <bits/stdc++.h>
using namespace std;

#define LSOne(S) ((S) & -(S))

typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vll;

class FenwickTree {
private:
    vll ft;
public:
    FenwickTree(int m) { ft.assign(m+1, 0); }

    void build(const vll &f) {
        int m = (int)f.size()-1;
        ft.assign(m+1, 0);
        for (int i = 1; i <= m; ++i) {
            ft[i] += ft[i];
            if (i+LSOne(i) <= m)
                ft[i+LSOne(i)] += ft[i];
        }
    }

    FenwickTree(const vll &f) { build(f); }

    FenwickTree(int m, const vi &s) {
        vll f(m+1, 0);
        for (int i = 0; i< (int)s.size(); ++i)
            ++f[s[i]];
        build(f);
    }

    int rsq(int j) {
        int sum = 0;
        for (; j; j -= LSOne(j))
            sum += ft[j];
        return sum;
    }
    int rsq(int i, int j) { return rsq(j) - rsq(i-1); }

    // update value of ith element by v
    void update(int i, int v) {
        for (; i < (int)ft.size(); i += LSOne(i))
            ft[i] += v;
    }

    int select(ll k) {
        int lo = 1, hi = ft.size() - 1;
        for (int i = 0; i < 30; ++i) {
            int mid = (lo+hi) / 2;
            (rsq(1, mid) < k) ? lo = mid : hi = mid;
        }
        return hi;
    }
};

int main() {

    return 0;
}