#include "biginteger.hpp"

class Calculator
{
public:
	Calculator();
	~Calculator();

	static BigInteger add(BigInteger a, BigInteger b);
	static BigInteger mult(BigInteger a, BigInteger b);
  static BigInteger multiplePrecisionDivision(BigInteger x, BigInteger y);
  static BigInteger divide(BigInteger x, BigInteger n, BigInteger& remainder);
  static BigInteger divide(BigInteger x, BigInteger n);
  static BigInteger mod(BigInteger x, BigInteger n);
  static BigInteger sub(BigInteger x, BigInteger n);
  static BigInteger gcd(BigInteger a, BigInteger b);
  static BigInteger inverse(BigInteger a, BigInteger n);
  static BigInteger modPow(BigInteger base, BigInteger exponent, BigInteger modulo);
  static BigInteger pow(BigInteger base, long int exponent,BigInteger);
  static BigInteger pow10(long int exponent);
  static BigInteger pow(BigInteger x, BigInteger n, BigInteger m);
  static bool isPrime(BigInteger number);
};
