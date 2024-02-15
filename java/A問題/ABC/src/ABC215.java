import java.util.Scanner;

public class ABC215 {
    public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
        String S = scanner.next();
        if(S.equals("Hello,World!")){
            System.out.println("AC");
        }else{
            System.out.println("WA");
        }
    }
}