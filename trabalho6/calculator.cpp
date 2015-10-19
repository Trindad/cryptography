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
			cout << modulo << " " << val - modulo << endl;
			temp.push_back(modulo);
			carry = (val - modulo)/10;
		}

		if (carry > 0) {
			temp.push_back(carry);
		}

		reverse(temp.begin(), temp.end());
		for (int f = 0; f < temp.size(); f++)
		{
			cout << temp[f];
		}

		cout << endl;
		BigInteger v = BigInteger(temp);
		s = add(s, v);

		carry = 0;
	}

	return s;
}