#include <iostream>
#include <vector>
#include <string>
// #include "biginteger.hpp"
#include "calculator.hpp"

using namespace std;

BigInteger::BigInteger() {
}

BigInteger::BigInteger(int i) {
	this->number.push_back(i);
}

BigInteger::BigInteger(vector<int> t) {
	this->number = t;
}

BigInteger::~BigInteger() {
}

bool BigInteger::isZero()
{
    return this->compareTo(BigInteger(0)) == 0;
}

void BigInteger::read()
{
    char c = '\0';
    int i = 0;
    this->number = vector<int>();

    while(cin.get(c))
    {
    	if (c == '\n')
    	{
        	break;
        }

        this->number.push_back( atoi(&c) );
        i++;
    }

    this->clean();
}

void BigInteger::clean()
{
	if ((int) this->number.size() > 1 && this->number[0] == 0) {
		this->number.erase(this->number.begin(),this->number.begin()+1);
		this->clean();
	}
}

bool BigInteger::gte(BigInteger y)
{
    return this->compareTo(y) >= 0;
}

int BigInteger::compareTo(BigInteger y)
{
    int xlen = (int) this->number.size();
    int ylen = (int) y.number.size();

    if (xlen != ylen) {
        return xlen > ylen ? 1 : -1;
    }

    for (int i = 0; i < xlen; i++)
    {
        if (this->number[i] > y.number[i]) {
            return 1;
        } else if (this->number[i] < y.number[i]) {
            return -1;
        }
    }

    return 0;
}

string BigInteger::toString()
{
	string s = "";

	for (int i = 0; i < (int) this->number.size(); i++)
	{
		s += to_string(this->number[i]);
	}

	return s;
}
