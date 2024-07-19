import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int N = sc.nextInt();
        int T = sc.nextInt();
        
        long[] finalPositions = new long[N];
        
        for (int i = 0; i < N; i++) {
            long start = sc.nextLong();
            long speed = sc.nextLong();
            finalPositions[i] = start + speed * T;
        }
        
        Arrays.sort(finalPositions);
        
        int groups = 0;
        
        for (int i = 1; i < N; i++) {
            if (finalPositions[i] != finalPositions[i - 1]) {
                groups++;
            }
        }
        
        System.out.println(groups);
    }
}