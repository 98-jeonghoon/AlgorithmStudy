import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        long s = scanner.nextLong();
        scanner.close();

        System.out.println(findMaxN(s));
    }

    public static long findMaxN(long s) {
        long left = 1;
        long right = (long) Math.sqrt(2 * s);

        while (left <= right) {
            long mid = left + (right - left) / 2;
            long sum = (mid * (mid + 1)) / 2;

            if (sum <= s) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return right;
    }
}