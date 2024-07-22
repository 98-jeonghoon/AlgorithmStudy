import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int[] arr = new int[n + 1];

        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        double maxValue = Double.MIN_VALUE;
        int idx = 1;

        while (true) {
            PriorityQueue<Integer> pq = new PriorityQueue<>();
            double sum = 0;
            double cnt = 0;

            for (int i = idx; i <= n; i++) {
                pq.add(arr[i]);
            }

            // 가장 작은수 하나를 삭제하고
            pq.poll();
            cnt = pq.size();
            while (!pq.isEmpty()) {
                sum += pq.poll();
            }

            double avg = sum / cnt;
            maxValue = Math.max(maxValue, avg);
            idx++;
            if (idx == n - 1) {
                break;
            }
        }
        System.out.printf("%.2f", maxValue);
    }

}