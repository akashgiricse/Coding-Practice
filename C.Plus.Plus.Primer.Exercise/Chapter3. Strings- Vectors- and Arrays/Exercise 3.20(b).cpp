#include<iostream>
#include <string>
#include <vector>

using namespace std;

int main(){
     int num;
     vector<int> vect;
     while(cin >>num){
       vect.push_back(num);
     }
     if(vect.size()%2==0){
    for(int i =0;i<vect.size()/2;i++){
        for(int j= vect.size()-i;j>=vect.size()-i;j--){
          int sum = vect[i]+vect[j-1];
          cout << sum << " ";
        }
    }
    }
    else
    for(int i =0;i<vect.size()/2;i++){
        for(int j= vect.size()-i;j>=vect.size()-i;j--){
          int sum = vect[i]+vect[j-1];
          cout << sum << " ";
        }
    }
    cout << vect[vect.size()/2];

}
