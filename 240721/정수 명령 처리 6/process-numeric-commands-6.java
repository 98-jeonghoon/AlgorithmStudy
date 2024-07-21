import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        PriorityQueue<Integer> pq = new PriorityQueue<>();

        int n = Integer.parseInt(st.nextToken());
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            String command = st.nextToken();
            if (command.equals("push")) {
                pq.add(-Integer.parseInt(st.nextToken()));
                continue;
            }
            if (command.equals("pop")) {
                System.out.println(-pq.poll());
                continue;
            }
            if (command.equals("size")) {
                System.out.println(pq.size());
                continue;
            }
            if (command.equals("empty")) {
                if (pq.isEmpty()) {
                    System.out.println(1);
                }else{
                    System.out.println(0);
                }
                continue;
            }
            if (command.equals("top")) {
                System.out.println(-pq.peek());
            }

        }

    }
}