#include <iostream>
#include <vector>

using namespace std;

int main(){
	freopen("test/3.in","r",stdin);

	int N;
	string S;
	cin >> N >> S;

	long long C=0;
	long long CO=0;
	long long W=0;

	for(int i=0;i<N;i++){
		if(S[i]=='C'){
			C++;
		} else if(S[i]=='O'){
			CO+=C;
		} else if(S[i]=='W'){
			W+=CO;
		}
	}
	cout << W << endl;
}
