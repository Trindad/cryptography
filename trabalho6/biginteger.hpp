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

	bool isZero();
	bool gte(BigInteger n);
	int compareTo(BigInteger y);
	void clean();
	string toString();
	/**
	 * Variáveis de entrada
	 */
	vector<int> number;

	void read();
};
