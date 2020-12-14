#include <iostraem>;
#include <list>;
#include <forward_list>;
using namespace std;

//Insertion
l.push_front(value)//head
l.insert(l.begin()+index,value);//index
l.push_back(value);//tail

//Read
int head = l.front();
int value = next(l.begin(),index);
int tail = l.back();

//Size
unsigned int size = l.size()

//Remove
l.pop_front();
l.erase(l.begin()+index);
l.pop_back();

//Clear
l.clear();
