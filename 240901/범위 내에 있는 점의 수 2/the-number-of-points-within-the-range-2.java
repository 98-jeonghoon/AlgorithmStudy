import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int n = Integer.parseInt(st.nextToken());
        int q = Integer.parseInt(st.nextToken());
        
        int[] points = new int[n];
        st = new StringTokenizer(br.readLine());
        int maxPoint = 0;
        for (int i = 0; i < n; i++) {
            points[i] = Integer.parseInt(st.nextToken());
            maxPoint = Math.max(maxPoint, points[i]);
        }
        
        int[] prefixSum = new int[maxPoint + 2];
        
        for (int point : points) {
            prefixSum[point]++;
        }
        
        for (int i = 1; i <= maxPoint; i++) {
            prefixSum[i] += prefixSum[i - 1];
        }
        
        StringBuilder sb = new StringBuilder();
        
        for (int i = 0; i < q; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            
            if (a > maxPoint) {
                sb.append(0).append("\n");
            } else {
                b = Math.min(b, maxPoint);
                int result = prefixSum[b] - (a > 0 ? prefixSum[a - 1] : 0);
                sb.append(result).append("\n");
            }
        }
        
        System.out.print(sb.toString());
    }
}