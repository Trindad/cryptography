#ifndef BIGINTEGER_H
#define BIGINTEGER_H

#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <cstdlib>
#include <algorithm>
#include <cmath>

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
	int compareTo(int y);
	int compareTo(BigInteger y);
	void clean();
	string toString();
	void print();
	long int asLongInt();
	int atBackwards(int index);

	/**
	 * Variáveis de entrada
	 */
	vector<int> number;
	short int signal;

	static BigInteger fromInt(int n);
	static BigInteger fromLongInt(long int n);

	void read();
};

#endif