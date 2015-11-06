import java.math.BigInteger;
import java.util.Random;
import java.io.*;

class Main{
	public static void main(String[] args) {
		BigInteger Q = BigInteger.probablePrime(2048,new Random());

		BigInteger p;
		int r = 1;
		BigInteger one = new BigInteger("1");

		while (true) {
			
			p = Q.multiply(BigInteger.valueOf(r)).add(one);

			if (p.isProbablePrime(25)) 
			{
				break;
			}

			r++;
		}

		BigInteger g = one;
		BigInteger u = new BigInteger(512,new Random());
		int t = p.subtract(one).divide(Q).intValue();

		while (g.compareTo(one) == 0) {
			u = new BigInteger(512,new Random());
			g = u.pow(t).mod(p);
		}

		System.out.println(p.toString());
		System.out.println(g.toString());
	}

}