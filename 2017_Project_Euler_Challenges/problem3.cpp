//The prime factors of 13195 are 5, 7, 13 and 29.
//
//What is the largest prime factor of the number 600851475143 ?

#include <iostream>
#include <vector>

using namespace std;

void EnviarVetorTela(vector<int> v)
{
    for(int i = 0; i < v.size(); i++)

        cout << v[i] << ' ';
}

void ListaPrimos(vector<int> &v, int n)
{
//    v.push_back(1);
    int temp,temp2;
    for(int i = 1; i <= n; i++)
    {
        for(int j = 2; j < i; j++)
        {
            if(i%j == 0) break;
            temp = i-1;
            temp2 = j;

        }
        if((temp)%temp2 != 0) v.push_back(i);

    }
}

int main()
{
    vector<int> v;
    ListaPrimos(v, 29);
    EnviarVetorTela(v);
}
