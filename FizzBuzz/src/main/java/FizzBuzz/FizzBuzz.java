package FizzBuzz;

import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class FizzBuzz {

    public static String run(int range) {
        return IntStream.rangeClosed(1, range).mapToObj(FizzBuzz::getFizzBuzzStringByNumber).collect(Collectors.joining(", "));
    }

    public static String getFizzBuzzStringByNumber(int currentIndex) {
        if (isDivisibleBy(currentIndex, 15)) {
            return "FizzBuzz";
        } else if (isDivisibleBy(currentIndex, 5)) {
            return "Buzz";
        } else if (isDivisibleBy(currentIndex, 3)) {
            return "Fizz";
        } else {
            return String.valueOf(currentIndex);
        }
    }

        public static Boolean isDivisibleBy ( int index, int divisor){
            return index % divisor == 0;
        }
    }
