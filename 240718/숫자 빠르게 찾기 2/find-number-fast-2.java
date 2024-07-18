import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        TreeSet<Integer> treeSet = new TreeSet<>();

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            treeSet.add(Integer.parseInt(st.nextToken()));
        }
        
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            Integer value = treeSet.ceiling(Integer.parseInt(st.nextToken()));
            if (value != null) {
                System.out.println(value);
            } else {
                System.out.println(-1);
            }
        }
    }
}