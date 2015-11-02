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
	BigInteger value1;
	BigInteger value2;

	value1.read();

	string op;
	getline(cin,op);

	value2.read();

	BigInteger modulo;
	modulo.read();

	// cout << modulo.toString() << endl;
	// cout << "antes" << "---------------" << endl;
	// cout << value1.toString() << endl;
	// cout << value2.toString() << endl;

	value1 = Calculator::mod(value1, modulo);
	value2 = Calculator::mod(value2, modulo);
	// value2 = Calculator::mod(value2, modulo);

	// cout << "depois" << "---------------" << endl;

	cout << value1.toString() << endl;
	cout << value2.toString() << endl;
	

	// cout  << "---------------" << endl;
	BigInteger result;

	/**
	 * Opções da calculadora
	 */
	if (op == "+") {
		result = Calculator::mod(Calculator::add(value1,value2), modulo);
		// result = Calculator::add(value1,value2);
	}
	else if (op == "*") {
		// result = Calculator::mod(Calculator::mult(value1,value2), modulo);
		result = Calculator::mult(value1,value2);
	} else if (op == "\%") {
		result = Calculator::mod(value1,value2);
	}
	else if (op == "^") {
		// result = Calculator::mod(Calculator::pow(value1,value2.asLongInt()), modulo);
		result = Calculator::pow(value1,value2.asLongInt());
	}
	else if (op == "-") {
		// result = Calculator::mod(Calculator::sub(value1,value2), modulo);
		result = Calculator::sub(value1,value2);
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

	cout << result.toString() << endl;

	return 0;
}
