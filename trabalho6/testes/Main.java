import java.math.BigInteger;
import java.util.Random;
import java.io.*;

class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader in = new BufferedReader(new InputStreamReader(System.in));

    BigInteger value1 = new BigInteger(in.readLine());

    String op = in.readLine();

    BigInteger value2 = new BigInteger(in.readLine());

    BigInteger modulo = new BigInteger(in.readLine());

    // value1 = value1.mod(modulo);
    // value2 = value2.mod(modulo);

    // System.out.println(value1.toString());
    // System.out.println(value2.toString());

    BigInteger result = new BigInteger("0");

    if (op.equals("+")) {
      result = value1.add(value2); //.mod(modulo);
    } else if (op.equals("*")) {
      result = value1.multiply(value2); //.mod(modulo);
    } else if (op.equals("^")) {
      result = value1.pow(value2.intValue()); //.mod(modulo);
    } else if (op.equals("-")) {
      result = value1.subtract(value2); //.mod(modulo);
    }

    System.out.println(result.toString());
  }
}
