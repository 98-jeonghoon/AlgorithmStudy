import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        TreeSet<Integer> treeSet = new TreeSet<>();

        for (int i = 1; i <= m; i++) {
            treeSet.add(i);
        }

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            treeSet.remove(Integer.parseInt(st.nextToken()));
            System.out.println(treeSet.last());
        }
    }
}