import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        PriorityQueue<Integer> pq = new PriorityQueue<>(Comparator.reverseOrder());

        int n = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            pq.add(Integer.parseInt(st.nextToken()));
        }

        while (true) {
            // 만약 현재 큐의 사이즈가 1개 이하일때 멈춤
            if (pq.size() <= 1) {
                break;
            }
            int first = pq.poll();
            int second = pq.poll();

            // 두 숫자의 차이가 0이면 집어넣지 않음
            if (first - second == 0) {
                continue;
            }
            pq.add(first - second);
        }

        if (pq.size() == 0) {
            System.out.println(-1);
        }else{
            System.out.println(pq.peek());
        }

    }
}