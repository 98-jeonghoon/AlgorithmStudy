import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int N = scanner.nextInt();
        int K = scanner.nextInt();
        int B = scanner.nextInt();

        int[] broken = new int[N + 1];
        
        for (int i = 0; i < B; i++) {
            int brokenNumber = scanner.nextInt();
            broken[brokenNumber] = 1;
        }

        int[] brokenSum = new int[N + 1];
        for (int i = 1; i <= N; i++) {
            brokenSum[i] = brokenSum[i - 1] + broken[i];
        }

        int minBroken = Integer.MAX_VALUE;
        for (int i = 1; i <= N - K + 1; i++) {
            int currentBroken = brokenSum[i + K - 1] - brokenSum[i - 1];
            minBroken = Math.min(minBroken, currentBroken);
        }

        System.out.println(minBroken);
        
        scanner.close();
    }
}