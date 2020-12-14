#include <iostream>;
#include <vector>;
using namespace std;

// Size

unsigned int size = v.size();


// Insertion
v.insert(v.begin(),value);//head
v.insert(v.begin(),index,value);//index
v.push_back(value)//tail


//Read
int head = v.front()//head
head = v[0]

int index = v.at(index)//index
index = v[index]

int tail = v.back()//tail
tail = v[v.size()-1]

//Remove head, index, tail
v.erase(v.begin());             // head
v.erase(v.begin() + index);     // index
v.pop_back();                   // tail


// Clear
v.clear();
