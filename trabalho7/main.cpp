#include <calculator.hpp>

int main(int argc, char const *argv[])
{
	BigInteger p, g;
	int a, b;
	
	p.read();
	g.read();
	scanf("%d", &a);
	scanf("%d", &b);

	BigInteger A = Calculator::pow(g,(long int)a,p);
	BigInteger B = Calculator::pow(g,(long int)b,p);

	BigInteger sa = Calculator::pow(B,(long int)a,p);
	BigInteger sb = Calculator::pow(A,(long int)b,p);

	if (sa.compareTo(sb) == 0)
	{
		cout<<"Diffie Hellman concluído."<<endl;
	}

	return 0;
}