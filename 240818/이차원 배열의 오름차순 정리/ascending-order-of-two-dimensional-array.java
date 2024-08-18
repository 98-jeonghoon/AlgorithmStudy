import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();

        int left = 1;
        int right = n * n;
        int answer = 0;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            int count = countLessThanOrEqual(mid, n);

            if (count >= k) {
                answer = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        System.out.println(answer);
    }

    static int countLessThanOrEqual(int mid, int n) {
        int count = 0;
        for (int i = 1; i <= n; i++) {
            count += Math.min(mid / i, n);
        }
        return count;
    }
}