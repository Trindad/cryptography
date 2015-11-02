/**
 * Calculadora para BigInteger
 */
#include "calculator.hpp"

Calculator::Calculator(){}
Calculator::~Calculator(){}

BigInteger Calculator::add(BigInteger a, BigInteger b)
{
	BigInteger result;

	int carry = 0,t1 = 0, t2 = 0;
	int alen = (int)a.number.size();
	int blen = (int)b.number.size();
  int siga = a.signal;
  int sigb = b.signal;

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

  if (siga != sigb)
  {
    BigInteger min, max;
    int sigmax = 0;

    a.signal = 1;
    b.signal = 1;

    int diff = a.compareTo(b);
    if (diff == 0) {
      return BigInteger(0);
    } else if (diff > 0) {
      min = b;
      max = a;
      sigmax = siga;
    } else {
      min = a;
      max = b;
      sigmax = sigb;
    }

    min.signal = 1;
    max.signal = 1;
    result = Calculator::sub(max, min);

    if (sigmax == -1) {
      result.signal = -1;
    }
  } else if (siga == -1) {
    result.signal = -1;
  }

	return result;
}

BigInteger Calculator::mult(BigInteger a, BigInteger b)
{
	int carry = 0;
	int alen = (int)a.number.size();
	int blen = (int)b.number.size();
  int siga = a.signal;
  int sigb = b.signal;

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

  if (siga != sigb)
  {
    s.signal = -1;
  }
  else
  {
    s.signal = 1;
  }

  s.clean();

	return s;
}

BigInteger Calculator::pow(BigInteger base, long int exponent)
{
  BigInteger result(1);
  for (long int i = 0; i < exponent; i++)
  {
    result = Calculator::mult(result, base);
  }

  return result;
}

BigInteger Calculator::multiplePrecisionDivision(BigInteger x, BigInteger y)
{
  x.signal = 1;
  y.signal = 1;

  int _n = (int)x.number.size() - 1;
	int _t = (int)y.number.size() - 1;

  if (y.compareTo(0) == 0)
  {
    return BigInteger(0);
  }

  if (_n < _t)
  {
    return x;
  }

  if (x.compareTo(y) < 0) {
    return x;
  }

  int n = _n - _t;

  BigInteger q;//quociente

  for (int i = 0; i <= n; i++)
  {
    q.number.push_back(0);
  }

  BigInteger temp = Calculator::pow(BigInteger::fromInt(10),(int) n);

  BigInteger t = Calculator::mult(y,temp);

  while(x.compareTo(t) >= 0)
  {
    int qs = (int) q.number.size() - 1;
    q.number[qs - n]++;
    x = Calculator::sub(x,t);
  }

	for (int i = _n; i > _t; i--)
	{
    int _qs = q.number.size() - 1;

		if (x.atBackwards(i) == y.number[0]) {
      q.number[_qs - (i - _t - 1)] = 9;
    }
    else
    {
			q.number[_qs - (i - _t - 1)] = floor(((x.atBackwards(i)*10) + x.atBackwards(i-1))/(float)y.number[0]);
		}

		while (q.number[_qs - (i - _t - 1)] * ((y.number[0]*10) + y.number[1]) > (x.atBackwards(i) * 100) + (x.atBackwards(i - 1) * 10) + x.atBackwards(i - 2))
		{
			q.number[_qs - (i - _t - 1)]--;
		}
		BigInteger a = Calculator::pow(BigInteger::fromInt(10),(long int) i - _t - 1);
		BigInteger tmp1 = Calculator::mult(a, y);

		BigInteger tmp2 = BigInteger::fromInt(q.atBackwards(i - _t - 1));
    BigInteger tmp3 = Calculator::mult(tmp1, tmp2);

    x = Calculator::sub(x, tmp3);

    if (x.compareTo(0) < 0) {
      x = Calculator::add(x, tmp1);
      q.number[_qs - (i - _t - 1)] = q.number[_qs - (i - _t - 1)] - 1;
    }
	}

	return x;
}

BigInteger Calculator::divide(BigInteger x, BigInteger d, BigInteger& remainder)
{
    if (d.isZero()) {
        return BigInteger(0);
    }

    BigInteger q = BigInteger(0);
    remainder.number = x.number;

    while (true) {
        BigInteger one = BigInteger(1);
        q = Calculator::add(q, one);
        BigInteger t = Calculator::sub(remainder, d);

        remainder.number.clear();
        for (int y = 0; y < (int) t.number.size(); y++)
        {
        	remainder.number.push_back(t.number[y]);
        }

        if (remainder.compareTo(d) < 0)
        {

        	break;
        }
        t.number.clear();
    }

    return q;
}

BigInteger Calculator::divide(BigInteger x, BigInteger d)
{
	BigInteger rem;
	return Calculator::divide(x, d, rem);
}

BigInteger Calculator::mod(BigInteger x, BigInteger n)
{
  return Calculator::multiplePrecisionDivision(x, n);
}

BigInteger Calculator::sub(BigInteger _a, BigInteger _b)
{
	BigInteger a, b;

	a.number = _a.number;
	b.number = _b.number;

  if (_b.signal == -1) {
    _b.signal = 1;
    return Calculator::add(_a, _b);
  } else if (_a.signal == -1) {
    _b.signal = -1;
    return Calculator::add(_a, _b);
  }


	int cmp = _a.compareTo(_b);

	if (cmp == 0)
	{
		return BigInteger(0);
	} else if (cmp == -1) {
    _b.signal = -1;
    return Calculator::add(_a, _b);
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

	// cout<<"\n\n\nRESULTADO "<<result.toString()<<endl;
	reverse( result.number.begin(),result.number.end() );
	result.clean();

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

BigInteger Calculator::inverse(BigInteger a, BigInteger n) {

	BigInteger result,newt,newr = a,r = n;

	result.number.push_back(0);
	newt.number.push_back(1);
	BigInteger zero = BigInteger(0);
	BigInteger one = BigInteger(1);

	while(newr.compareTo(zero) != 0) {
		BigInteger quotient = Calculator::divide(r,newr);

		BigInteger temp1 = Calculator::sub(result, Calculator::mult(quotient, newt));
		result.number = newt.number;
		newt.number = temp1.number;

		temp1 = Calculator::sub(r, Calculator::mult(quotient, newr));
		r.number = newr.number;
		newr.number = temp1.number;
	}

	if(r.compareTo(one) > 0)
	{
		cout << "Not invertible" << endl;
		exit(1);
	}

	if (result.compareTo(0) < 0)
	{
		result = Calculator::add(result, n);
	}

	return result;
}
