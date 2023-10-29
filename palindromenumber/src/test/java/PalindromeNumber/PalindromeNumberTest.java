package PalindromeNumber;

import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;
import static org.junit.jupiter.api.Assertions.*;

class PalindromeNumberTest {
    @Test
    void ShouldReturnTrue() {
        int number =  121;
        assertThat(PalindromeNumber.isPalindrome(number)).isTrue();
    }
    @Test
    void ShouldAlsoReturnFalse() {
        int number =  -121;
        assertThat(PalindromeNumber.isPalindrome(number)).isFalse();
    }
    @Test
    void ShouldReturnFalse() {
        int number =  10;
        assertThat(PalindromeNumber.isPalindrome(number)).isFalse();
    }
}