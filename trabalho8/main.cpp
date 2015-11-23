/**
 * Algoritmo do RSA
 *
 * Implementar mecanismo de geração de chaves para a cifra RSA:

	xed = x (mod N)

	Onde e e’ a chave de cifragem e d e’ a chave de decifragem.

	Como xφ(N) = 1 (mod N)  (prova em [1]) segue que xφ(N) + 1 = x (mod N) 
	Como xφ(N) + 1 = x (mod N) e xed = x (mod N), entao φ(N) + 1 = ed


	Aplicando o modulo φ(N) em φ(N) + 1 = ed temos 1 = ed (mod φ(N)) 
	Ou seja e e d são um número e seu inverso multiplicativo modulo φ(N)

	1 -Para calcular pares de números e e d:
	2 - Escolher quaisquer dois números primos p e q e um numero N sendo pq = N
	3 - Calcular φ(N), usando φ(N) = φ(p)φ(q) (prova em [2])
	4 -Escolher um número qualquer e que seja coprimo a φ(N)
	5 -Calcular d = e-1 (mod φ(N))
 */
#include <calculator.hpp>
	
int main(int argc, char const *argv[])
{
	BigInteger p, q, n;
	
	p.read();
	p.read();

	n = Calculator::mult(p,q);// ( p * q ) = n


	
	return 0;
}