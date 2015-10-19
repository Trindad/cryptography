#include "calculator.hpp"

int main(int argc, char const *argv[])
{
	BigInteger value1,value2;

	value1.read();

	Calculator c;

	string op;
	getline(cin,op);

	value2.read();

	// BigInteger result = c.add(value1,value2);
	BigInteger result = c.mult(value1,value2);

	for(int i = 0; i < (int)result.number.size();i++ )cout<<result.number[i];
	cout<<endl;

	return 0;
}