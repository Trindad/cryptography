#include "calculator.hpp"

int main(int argc, char const *argv[])
{
	BigInteger value1,value2;

	value1.read();

	string op;
	getline(cin,op);

	value2.read();

	BigInteger result;

	if (op == "+") {
		result = Calculator::add(value1,value2);
	} 
	else if (op == "*") {
		result = Calculator::mult(value1,value2);
	} else if (op == "\%") {
		result = Calculator::mod(value1,value2);
	} 
	else if (op == "^") {
		BigInteger modulo;
		modulo.read();
		result = Calculator::modPow(value1,value2,modulo);
	}
	else if (op == "-") {
		result = Calculator::sub(value1,value2);
	}
	else if (op == "/") {
		BigInteger rem;
		result = Calculator::divide(value1,value2,rem);
	}
	else {
		cout << "Invalid operation. Aborting..." << endl;
		return 1;
	}

	for(int i = 0; i < (int)result.number.size();i++ )cout<<result.number[i];
	cout<<endl;

	return 0;
}
