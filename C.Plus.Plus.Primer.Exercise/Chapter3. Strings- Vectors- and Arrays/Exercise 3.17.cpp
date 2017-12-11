#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
   string words;
   vector<string> strVec;
   while(getline(cin,words)){
        strVec.push_back(words);
   }
// here we have to use for range twice: 
// one for accessing every char in strVec
// other for applying toupper(because toupper can be applied only on char datatype)
   for (auto &i : strVec){
         for(auto &j : i)
         j = toupper(j);
         cout << i;
   }

   return 0;
}
