import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

        TreeSet<Integer> points = new TreeSet<>();
        points.add(0);
        
        int minDistance = Integer.MAX_VALUE;

        for (int i = 0; i < n; i++) {
            int x = Integer.parseInt(st.nextToken());
            
            Integer lower = points.lower(x);
            Integer higher = points.higher(x);

            if (lower != null) {
                minDistance = Math.min(minDistance, x - lower);
            }
            if (higher != null) {
                minDistance = Math.min(minDistance, higher - x);
            }

            points.add(x);

            System.out.println(minDistance);
        }
    }
}