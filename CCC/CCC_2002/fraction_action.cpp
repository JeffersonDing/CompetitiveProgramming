#include <bits/stdc++.h>

using namespace std;

int gcd(int a, int b)
{
    if (b == 0)
    {
        return (a);
    }
    else
    {
        return (gcd(b, a % b));
    }
}

int main()
{
    int numerator, denominator, temp;
    string output;

    cin >> numerator;
    cin >> denominator;

    if (numerator == 0)
    {
        cout << "0" << endl;
        return (0);
    }
    temp = numerator;
    numerator = numerator / gcd(numerator, denominator);
    denominator = denominator / gcd(temp, denominator);
    if (numerator > denominator)
    {
        output += to_string(numerator / denominator);
    }
    if (numerator % denominator > 0)
    {
        output += " " + to_string(numerator % denominator) + "/" + to_string(denominator);
    }
    cout << output << endl;
}