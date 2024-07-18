import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

        TreeSet<Integer> points = new TreeSet<>();
        points.add(0);

        PriorityQueue<Integer> minDistances = new PriorityQueue<>();

        for (int i = 0; i < n; i++) {
            int x = Integer.parseInt(st.nextToken());

            Integer lower = points.lower(x);
            Integer higher = points.higher(x);

            if (lower != null) {
                minDistances.add(x - lower);
            }
            if (higher != null) {
                minDistances.add(higher - x);
            }
            if (lower != null && higher != null) {
                minDistances.remove(higher - lower);
            }

            points.add(x);

            System.out.println(minDistances.peek());
        }
    }
}