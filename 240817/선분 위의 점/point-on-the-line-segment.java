import java.io.*;
import java.util.*;

public class Main {
    static int n, m;
    static int[] points;
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        points = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            points[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(points);
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            System.out.println(upperBound(end) - lowerBound(start));
        }
    }

    static int lowerBound(int target) {
        int left = 0, right = n - 1;
        int minIdx = n;
        while (left <= right) {
            int mid = (right + left) / 2;
            if (points[mid] >= target) {
                right = mid - 1;
                minIdx = Math.min(minIdx, mid);
            }
            else{
                left = mid + 1;
            }
        }
        return minIdx;
    }

    static int upperBound(int target) {
        int left = 0, right = n - 1;
        int minIdx = n;
        while (left <= right) {
            int mid = (right + left) / 2;
            if (points[mid] > target) {
                right = mid - 1;
                minIdx = Math.min(minIdx, mid);
            } else {
                left = mid + 1;
            }
        }
        return minIdx;
    }
}