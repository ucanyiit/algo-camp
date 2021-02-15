#include <bits/stdc++.h>

using namespace std;

#define endl '\n'
#define ll long long
#define pb push_back
#define pll pair<ll, ll>
#define fi first
#define se second

const int md = (int) 1e9 + 7;
const int siz = 300005;

ll arr1[siz], arr2[siz], arr3[siz], sm2[siz], sm3[siz];
ll n, m, k, mp, kp, res;

int main(){
    ios_base::sync_with_stdio(false); cin.tie(NULL);

    cin>>n>>m>>k;
    for(int i=0;i<n;i++) cin>>arr3[i];
    sort(arr3, arr3+n);
    for(int i=0;i<m;i++) cin>>arr2[i];
    sort(arr2, arr2+m);
    for(int i=0;i<k;i++) cin>>arr1[i];
    sort(arr1, arr1+k);

    for(int i=0;i<m;i++) {
        while(kp!=n && arr3[kp]<arr2[i]) kp++;
        sm2[i]=kp;
    }
    
    for(int i=0;i<k;i++) {
        if(i!=0) sm3[i]+=sm3[i-1];
        while(mp!=m && arr2[mp]<arr1[i]){
            sm3[i]+=sm2[mp];
            mp++;
        }
        res+=sm3[i];
    }
    cout<<res;
    
}
