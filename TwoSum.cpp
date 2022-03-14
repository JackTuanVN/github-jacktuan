#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define fr(i, a, b) for (long long i = a; i <= b; i++)
#define fd(i, a, b) for (long long i = a; i >= b; i--)
const ll MAXN = 1e6 + 1;
ll a[MAXN], save[MAXN], saveLocation[MAXN];
ll target;
ll n;

void enter()
{
    cin >> n;
    cin >> target;
    fr(i, 1, n)
    {
        cin >> a[i];

        saveLocation[a[i]] = i;
    }
}

void solve()
{
    fr(i, 1, n)
    {
        save[a[i]] = 1;
    }
    fr(i, 1, n)
    {
        if (save[target - a[i]] == 1)
        {
            cout << saveLocation[a[i]] << '\t' << saveLocation[target - a[i]];
            break;
        }
    }
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    enter();
    solve();
    // cout << "hello world";
    return 0;
}