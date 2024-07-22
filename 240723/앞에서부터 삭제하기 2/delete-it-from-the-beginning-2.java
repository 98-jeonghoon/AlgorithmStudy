import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int N = scanner.nextInt();
        int[] arr = new int[N + 1];

        for (int i = 1; i <= N; i++) {
            arr[i] = scanner.nextInt();
        }

        System.out.printf("%.2f\n", getMaxAverageAfterDeletions(N, arr));
    }

    public static double getMaxAverageAfterDeletions(int N, int[] arr) {
        int[] prefix = new int[N + 1];
        for (int i = 1; i <= N; i++) {
            prefix[i] = prefix[i - 1] + arr[i];
        }
        
        int[] postfix = new int[N + 1];
        int temp = 10001;
        for (int i = N; i >= 0; i--) {
            postfix[i] = Math.min(temp, arr[i]);
            temp = postfix[i];
        }

        int total = 0;
        for (int i = 1; i <= N; i++) {
            total += arr[i];
        }

        double ans = 0;
        for (int k = 1; k < N - 1; k++) {
            int summation = total - prefix[k] - postfix[k + 1];
            double avg = (double) summation / (N - k - 1);
            ans = Math.max(ans, avg);
        }

        return ans;
    }
}