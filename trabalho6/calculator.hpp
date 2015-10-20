#include "biginteger.hpp"

class Calculator
{
public:
	Calculator();
	~Calculator();

	static BigInteger add(BigInteger a, BigInteger b);
	static BigInteger mult(BigInteger a, BigInteger b);
  static BigInteger divide(BigInteger x, BigInteger n, BigInteger& remainder);
  static BigInteger mod(BigInteger x, BigInteger n);
  static BigInteger sub(BigInteger x, BigInteger n);
  static BigInteger gcd(BigInteger a, BigInteger b);
  static BigInteger modPow(BigInteger base, BigInteger exponent, BigInteger modulo);
};
