import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int[] arr = new int[n];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        double maxValue = Double.MIN_VALUE;

        // Sliding window and priority queue for efficiency
        for (int k = 1; k <= n - 2; k++) {
            PriorityQueue<Integer> pq = new PriorityQueue<>();
            double sum = 0;

            for (int i = k; i < n; i++) {
                pq.add(arr[i]);
                sum += arr[i];
            }

            // Remove the smallest element
            sum -= pq.poll();

            // Calculate the average
            double avg = sum / (n - k - 1);
            maxValue = Math.max(maxValue, avg);
        }

        System.out.printf("%.2f", maxValue);
    }
}