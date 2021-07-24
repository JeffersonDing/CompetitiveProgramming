// time complexity O(n log log n)
// space complexity O(n)

// cpp sieve of eratosthenes algorithm
// source: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

#include <bits/stdc++.h>

using namespace std;

class Solution
{
public:
    vector<int> primes;
    vector<bool> isPrime;
    vector<int> sieve(int n)
    {
        primes.resize(n);
        isPrime.resize(n);
        for (int i = 0; i < n; i++)
        {
            primes[i] = i;
            isPrime[i] = true;
        }
        isPrime[0] = isPrime[1] = false;
        for (int i = 2; i < n; i++)
        {
            if (isPrime[i])
            {
                for (int j = i * i; j < n; j += i)
                {
                    isPrime[j] = false;
                }
            }
        }
        for (int i = 0; i < n; i++)
        {
            if (isPrime[i])
            {
                primes[i] = i;
            }
        }
        return primes;
    }
};

int main()
{
    Solution mySolution;
    vector<int> myPrimes = mySolution.sieve(1000000);
    for (int i = 0; i < myPrimes.size(); i++)
    {
        cout << myPrimes[i] << endl;
    }
    return 0;
}
