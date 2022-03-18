// https://arsiv.cclub.metu.edu.tr/problem/indirim/

#include <algorithm>
#include <iostream>
using namespace std;

int arr[300005], n, m, res;

int main(){
    cin>>n>>m;
    for(int i=0;i<n;i++) cin>>arr[i]; 
    sort(arr, arr+n);
    for(int i=0;i<n;i++){
        if(arr[i]>m) break;
        m-=arr[i];
        res++;
    }
    cout<<res;    
}
