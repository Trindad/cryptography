#include "calculator.hpp"

Calculator::Calculator(){}
Calculator::~Calculator(){}

BigInteger Calculator::add(BigInteger a, BigInteger b)
{
	BigInteger result;

	int carry = 0,t1 = 0, t2 = 0;
	int alen = (int)a.number.size();
	int blen = (int)b.number.size();

	int n = alen < blen ? blen : alen;//pega maior limite

	for (int i = 0; i < n; i++)
	{
		t1 = i < alen ? a.number[alen - i - 1] : 0;
		t2 = i < blen ? b.number[blen - i - 1] : 0;

		int s = t1 + t2 + carry;

		result.number.push_back(s%10);

		carry = s >= 10 ? 1 : 0;
	}

	if (carry == 1)
	{
		result.number.push_back(1);
	}

	reverse( result.number.begin(),result.number.end() );

	return result;
}

BigInteger Calculator::mult(BigInteger a, BigInteger b)
{
	int carry = 0;
	int alen = (int)a.number.size();
	int blen = (int)b.number.size();

	BigInteger max, min;
	int minLength = 0, maxLength = 0;

	if (alen < blen )
	{
		min = a, max = b;
		minLength = alen, maxLength = blen;
	}
	else
	{
		min = b, max = a;
		minLength = blen, maxLength = alen;
	}

	// cout << minLength << " " << maxLength << endl;

	BigInteger s = BigInteger(0);

	for (int i = minLength-1; i >= 0 ; i--)
	{
		vector<int> temp;

		for (int m = i; m < minLength - 1; m++)
		{
			temp.push_back(0);
		}

		for (int j = maxLength-1; j >= 0; j--)
		{
			int val = ( min.number[i] * max.number[j] ) + carry;
			int modulo = val % 10;
			// cout << modulo << " " << val - modulo << endl;
			temp.push_back(modulo);
			carry = (val - modulo)/10;
		}

		if (carry > 0) {
			temp.push_back(carry);
		}

		reverse(temp.begin(), temp.end());
		
		BigInteger v = BigInteger(temp);
		s = add(s, v);

		carry = 0;
	}

	return s;
}

BigInteger Calculator::divide(BigInteger x, BigInteger d, BigInteger& remainder)
{
    if (d.isZero()) {
        return BigInteger(0);
    }

    BigInteger q = BigInteger(0);
    remainder.number = x.number;

    while (remainder.gte(d)) {
        BigInteger one = BigInteger(1);
        q = Calculator::add(q, one);
        BigInteger t = Calculator::sub(remainder, d);
    	remainder.number = t.number;
    }

    return q;
}

BigInteger Calculator::mod(BigInteger x, BigInteger n)
{
    BigInteger remainder;
    Calculator::divide(x, n, remainder);

    return remainder;
}

BigInteger Calculator::sub(BigInteger a, BigInteger b)
{
	int cmp = a.compareTo(b);

  	if (cmp == 0) 
  	{
  		return BigInteger(0);
	}

	BigInteger result;

	int t1 = 0, t2 = 0;
	int alen = (int)a.number.size();
	int blen = (int)b.number.size();

	int n = alen < blen ? blen : alen;//pega maior limite

	BigInteger max, min;
	int minLength = 0, maxLength = 0;

	min = a.compareTo(b) < 0 ? a : b;
	max = a.compareTo(b) > 0 ? a : b;
	minLength = (int) min.number.size();
	maxLength = (int) max.number.size();

	for (int i = 0; i < n; i++)
	{
		t2 = i < minLength ? min.number[minLength - i - 1] : 0;
		t1 = i < maxLength ? max.number[maxLength - i - 1] : 0;

		int difference = t1 - t2;

		if (difference < 0)
		{
			max.number[maxLength-i-2]--;
			difference += 10;
		}

		result.number.push_back(difference);
	}

	reverse( result.number.begin(),result.number.end() );

	if (result.number[0] == 0)
	{
		result.number.erase(result.number.begin(),result.number.begin()+1);
	}

  return result;
}

BigInteger Calculator::gcd(BigInteger a, BigInteger b)
{
  if (b.isZero())
  {
    return a;
  }

  return Calculator::gcd(b, Calculator::mod(a, b));
}

BigInteger Calculator::modPow(BigInteger base, BigInteger exponent, BigInteger modulo) {
    BigInteger result = BigInteger(1);
   
    while (exponent.compareTo(BigInteger(0)) > 0) 
    {
    	// expoente impar
        if( (exponent.number[(int) exponent.number.size() - 1] % 2 ) == 1) {
            result = Calculator::mod(Calculator::mult(result,base), modulo);
        }
        BigInteger rem = BigInteger();
        exponent = Calculator::divide(exponent, BigInteger(2), rem);
        base = Calculator::mod(Calculator::mult(base, base), modulo);
    }

    return Calculator::mod(result, modulo);
}
