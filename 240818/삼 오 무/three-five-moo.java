import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        int left = 1, right = Integer.MAX_VALUE;
        int answer = 0;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            int count = mid - (mid / 3) - (mid / 5) + (mid / 15);

            if (count >= N) {
                answer = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        System.out.println(answer);
    }
}