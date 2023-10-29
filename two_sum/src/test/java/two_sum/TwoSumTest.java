package two_sum;

import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;

class TwoSumTest {

    @Test
    void ShouldReturnZeroAndOne() {
        int[] nums = {2, 7, 11, 15};
        int target = 9;

        assertThat(TwoSum.twoSum(nums, target)).isEqualTo(new int[]{0, 1});
    }

    @Test
    void ShouldReturnOneAndTwo() {
        int[] nums = {3, 2, 4};
        int target = 6;

        assertThat(TwoSum.twoSum(nums, target)).isEqualTo(new int[]{1, 2});
    }

    @Test
    void ShouldReturnZeroAndTwo() {
        int[] nums = {3, 2, 3};
        int target = 6;

        assertThat(TwoSum.twoSum(nums, target)).isEqualTo(new int[]{0, 2});
    }

}