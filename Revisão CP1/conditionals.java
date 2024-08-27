import java.util.Scanner;

public class conditionals {

    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);

        System.out.println("Enter number 1");
        int number1 = scan.nextInt();

        System.out.println("Enter number 2");
        int number2 = scan.nextInt();

        if (number1 > number2) {
            System.out.println(number1 + " é maior do que " + number2);
        } else {
            System.out.println(number1 + " é menor do que " + number2);
        }
    }

}
