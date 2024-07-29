import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        scanner.close();
        
        long[] dp = new long[1001];
        long[] dphalf = new long[1001];
        int MOD = 1000000007;

        dp[1] = 2;
        dp[2] = 7;
        dphalf[1] = 1;
        dphalf[2] = 3;
        
        for (int i = 3; i <= n; i++) {
            dp[i] = (dp[i-1]*2 + dp[i-2] + dphalf[i-1] * 2) % MOD;
            dphalf[i] = (dp[i-1] + dphalf[i-1]) % MOD;
        }
        
        System.out.println(dp[n]);
    }
}