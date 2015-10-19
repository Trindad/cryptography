#include <iostream>
#include <vector>
#include <string>
#include "biginteger.hpp"

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
}