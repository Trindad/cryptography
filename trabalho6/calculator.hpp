#include "biginteger.hpp"

class Calculator
{
public:
	Calculator();
	~Calculator();

	BigInteger add(BigInteger a, BigInteger b);
	BigInteger mult(BigInteger a, BigInteger b);

	string operation;
};