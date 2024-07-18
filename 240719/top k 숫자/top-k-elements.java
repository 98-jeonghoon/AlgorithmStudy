import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        TreeSet<Integer> treeSet = new TreeSet<>(Comparator.reverseOrder());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            treeSet.add(Integer.parseInt(st.nextToken()));
        }
        
        for (int i = 0; i < k; i++) {
            System.out.print(treeSet.pollFirst() + " ");
        }
    }
}