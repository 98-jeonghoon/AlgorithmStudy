import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        scanner.close();
        
        long[] dp = new long[n + 1];
        dp[0] = 1;
        dp[1] = 1;

        for (int i = 2; i <= n; i++) {
            long sum = 0;
            for (int j = 0; j < i; j++) {
                sum += dp[j] * dp[i - j - 1];
            }
            dp[i] = sum;
        }

        System.out.println(dp[n]);
    }
}