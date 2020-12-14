#include <iostream>
#include <map>
#include <unordered_map>
using namespace std;

//Insert
m.insert(pair<string,string>("hello","world"));

//Access by key
string value = m.at("hello");

//Size
unsigned int size = m.size();

//Remove
m.erase("key");

//Clear
m.clear()
