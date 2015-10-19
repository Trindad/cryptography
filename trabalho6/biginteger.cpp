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

// BigInteger BigInteger::fastModPow(BigInteger base, BigInteger exponent, BigInteger modulo) {
//     // plan: exploit the binary representation of the exponent, see for example http://en.wikipedia.org/w/index.php?title=Modular_exponentiation&oldid=517653653#Right-to-left_binary_method
//     BigInteger result = BigInteger.ONE;
//     while (exponent.compareTo(BigInteger.ZERO) > 0) {
//         if (exponent.testBit(0)) // then exponent is odd
//             result = (result.multiply(base)).mod(modulo);
//         exponent = exponent.shiftRight(1);
//         base = (base.multiply(base)).mod(modulo);
//     }
//     return result.mod(modulo);
// }
