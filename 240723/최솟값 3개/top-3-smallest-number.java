import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        PriorityQueue<Long> pq = new PriorityQueue<>();

        for (int i = 0; i < n; i++) {
            pq.add(Long.parseLong(st.nextToken()));
            if (pq.size() < 3) {
                System.out.println(-1);
            }else{
                long val1 = pq.poll();
                long val2 = pq.poll();
                long val3 = pq.poll();
                System.out.println(val1 * val2 * val3);
                pq.add(val1);
                pq.add(val2);
                pq.add(val3);
            }

        }


    }
}