// https://atcoder.jp/contests/abc182/tasks/abc182_a

import java.util.Scanner;

public class ABC182 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int A = scanner.nextInt();
        int B = scanner.nextInt();
        int XB = 2*A+100;
        System.out.println(XB-B);
    }
}