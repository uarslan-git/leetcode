package FizzBuzz;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class FizzBuzzTest {

    @Test
    public void ShouldReturnZero() {
        Assertions.assertEquals("0", FizzBuzz.run(1));
    }

    @Test
    public void ShouldSolveFizzBuzz() {
        Assertions.assertEquals("1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz", FizzBuzz.run(15));
    }
}
