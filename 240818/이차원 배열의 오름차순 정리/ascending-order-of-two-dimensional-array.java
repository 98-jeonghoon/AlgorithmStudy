import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();

        long left = 1;
        long right = (long) n * n;
        long answer = 0;

        while (left <= right) {
            long mid = left + (right - left) / 2;
            long count = countLessThanOrEqual(mid, n);

            if (count >= k) {
                answer = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        System.out.println(answer);
    }

    static long countLessThanOrEqual(long mid, int n) {
        long count = 0;
        for (int i = 1; i <= n; i++) {
            count += Math.min(mid / i, n);
        }
        return count;
    }
}