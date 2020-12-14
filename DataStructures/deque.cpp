#include <iostream>;
#include <vector>;
#include <interator>;
using namespace std;

//Insertion
d.push_front(value);//head
d.insert(d.begin()+index,value)//index
d.push_back(value)//tail

//Read
int head = d.head();
int index = d.at(value);
int tail = d.back();

//Size
unsigned int size = d.size();

//Remove
d.pop_front();
d.erase(d.begin()+index);
d.pop_back();

//Clear
d.clear
