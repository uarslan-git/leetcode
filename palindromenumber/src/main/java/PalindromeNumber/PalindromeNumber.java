package PalindromeNumber;

public class PalindromeNumber {
    public static boolean isPalindrome(int x) {
        int number = x;
        int reverse = 0;
        if(x == 0) return true;
        if(x < 0) return false;
        while (number > 0) {
            reverse = reverse * 10 + number % 10;
            number /= 10;
        }
        return x == reverse;
    }
}