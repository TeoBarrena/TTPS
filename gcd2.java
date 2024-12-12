package gcd2;

import java.util.Scanner;
import java.math.BigInteger;

public class gcd2{

    //alg de Euclides -> gcd(a,b) = gcd(b, a mod b)
    public static BigInteger gcd(BigInteger a, BigInteger b){
        if(b.equals(BigInteger.ZERO)){
            return a;
        }
        return gcd(b, a.mod(b));
    }
    
    public static BigInteger modLargeNumber(String B, BigInteger A) {
        BigInteger remainder = BigInteger.ZERO;
        for (int i = 0; i < B.length(); i++) {
            char digit = B.charAt(i);
            remainder = remainder.multiply(BigInteger.TEN).add(BigInteger.valueOf(digit - '0'));
            remainder = remainder.mod(A);
        }
        return remainder;
    }

    /*
    Input
        The first line of the input file contains a number representing the number of lines to follow. Each line consists of two number A and B (0 <= A <= 40000 and A <= B < 10^250).
    Output
        Print for each pair (A,B) in the input one integer representing the GCD of A and B. */
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();  
        
        for(int i = 0; i < n; i++){
            int a = sc.nextInt();
            String b = sc.next(); //manejo de String porq puede ser numero muy grande
            
            if (a == 0){
                System.out.println(b);
            }
            else{
                BigInteger a_big = BigInteger.valueOf(a); //convierte a BigInteger por el tipo del parmtero de la func.
                BigInteger b_mod_a = modLargeNumber(b, a_big);

                BigInteger resultado = gcd(a_big, b_mod_a);
                System.out.println(resultado);
            }
    }
    }
}