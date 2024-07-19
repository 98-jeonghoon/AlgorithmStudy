import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        TreeSet<Integer> treeSet = new TreeSet<>();
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());


        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            treeSet.add(Integer.parseInt(st.nextToken()));
        }

        int answer = Integer.MAX_VALUE;
        for (int value : treeSet) {
            Integer target = treeSet.ceiling(value + m);
            if (target != null) {
                answer = Math.min(answer, target - value);
            }
        }

        if (answer == Integer.MAX_VALUE) {
            System.out.println("-1");
        }else{
            System.out.println(answer);
        }

    }
}