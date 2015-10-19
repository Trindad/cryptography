#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <cstdlib>
#include <algorithm>

using namespace std;

class BigInteger
{
public:
	BigInteger();
	BigInteger(vector<int>);
	BigInteger(int);
	~BigInteger();
	
	/**
	 * Variáveis de entrada
	 */
	vector<int> number;

	void read();
};