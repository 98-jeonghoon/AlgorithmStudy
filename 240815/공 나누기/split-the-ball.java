import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        
        // 최소 필요한 공의 개수 계산
        int minBalls = k * (k + 1) / 2;
        
        if (n < minBalls) {
            System.out.println(-1);
            return;
        }
        
        // 공을 분배하는 기본 개수
        int remainingBalls = n - minBalls;
        int maxExtra = remainingBalls / k;
        int leftover = remainingBalls % k;
        
        int maxBalls = k + maxExtra;
        int minBallsInBox = 1 + maxExtra;
        
        if (leftover > 0) {
            maxBalls++;
        }
        
        int result = maxBalls - minBallsInBox;
        System.out.println(result);
    }
}