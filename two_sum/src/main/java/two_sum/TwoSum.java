package two_sum;

import java.util.HashMap;
import java.util.Map;

/**
 * Hello world!
 *
 */
public class TwoSum
{
    public static int[] twoSumBruteforce(int[] nums, int target)
    {
        // Time Complexity(O(n^2))
        int[] indices = new int[2];
        for (int i = 0; i < nums.length; i++) {
            for (int j = i+1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    indices[0] = i;
                    indices[1] = j;
                }
            }
        }
        return indices;
    }
    public static int[] twoSum(int[] nums, int target)
    {
        Map<Integer, Integer> numbers = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int cur = nums[i];
            int x = target - cur;
            if (numbers.containsKey(x)) {
                return new int[] {numbers.get(x), i};
            }
            numbers.put(cur, i);
        }
        return new int[0];
    }
}