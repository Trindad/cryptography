/**
 *********************************************************
 * 			CALCULADORA PARA BIGINTEGER
 *********************************************************
 *
 * -Funções: modulo,divisão,multiplicação,adição, subtração
 * 			inverso multiplicativo, exponenciação
 *
 * -Compilar:  g++ *.cpp -o main -g --std=c++11
 *
 * Alunos: Silvana Trindade e Maurício André Cinelli
 * *******************************************************
 */
#include "calculator.hpp"

int main(int argc, char const *argv[])
{
	long int a = 46513;
	BigInteger value1;
	BigInteger value2;


	value1.read();

	string op;
	// getline(cin,op);


	value2.read();
	BigInteger r = Calculator::multiplePrecisionDivision(value1, value2);
	cout << r.toString() << endl;
	return 0;

	BigInteger modulo;
	modulo.read();

	value1 = Calculator::mod(value1, modulo);
	value2 = Calculator::mod(value2, modulo);

	BigInteger result;

	/**
	 * Opções da calculadora
	 */
	if (op == "+") {
		result = Calculator::mod(Calculator::add(value1,value2), modulo);
	}
	else if (op == "*") {
		result = Calculator::mod(Calculator::mult(value1,value2), modulo);
	} else if (op == "\%") {
		result = Calculator::mod(value1,value2);
	}
	else if (op == "^") {
		result = Calculator::modPow(value1,value2,modulo);
	}
	else if (op == "-") {
		result = Calculator::mod(Calculator::sub(value1,value2), modulo);
	}
	else if (op == "/") {
		BigInteger rem;
		result = Calculator::mod(Calculator::divide(value1,value2,rem), modulo);
	}
	else if (op == "~") {
		result = Calculator::mod(Calculator::inverse(value1,value2), modulo);
	}
	else {
		cout << "Invalid operation. Aborting..." << endl;
		return 1;
	}

	for(int i = 0; i < (int)result.number.size();i++ )cout<<result.number[i];
	cout<<endl;

	return 0;
}
