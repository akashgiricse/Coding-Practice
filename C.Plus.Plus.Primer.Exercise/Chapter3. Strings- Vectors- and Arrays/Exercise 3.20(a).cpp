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
    for(int i =0;i<vect.size();i+=2){
        for(int j=i+1;j<=i+1;j++){
          int sum = vect[i]+vect[j];
          cout << sum << " ";
        }
    }
}
