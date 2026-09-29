import java.util.Arrays;
import java.util.Scanner;

class Solution {

    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] result = new int[n];
        int curr = 1;

        Arrays.fill(result, 1);
        for (int i = 0; i < n; i++) {
            result[i] *= curr;
            curr *= nums[i];
        }

        curr = 1;
        for (int i = n - 1; i >= 0; i--) {
            result[i] *= curr;
            curr *= nums[i];
        }

        return result;
    }
}

class ProductOfArrayExceptSelf {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter integers separated by spaces: ");
        String input = scanner.nextLine().trim();
        int[] nums;
        if (input.isEmpty()) {
            nums = new int[0];
        } else {
            String[] values = input.split("\\s+");
            nums = new int[values.length];
            for (int i = 0; i < values.length; i++) {
                nums[i] = Integer.parseInt(values[i]);
            }
        }
        int[] result = new Solution().productExceptSelf(nums);
        System.out.println(Arrays.toString(result));

        scanner.close();
    }
}
