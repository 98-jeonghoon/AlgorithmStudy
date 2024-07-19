import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        TreeSet<Integer> treeSet = new TreeSet<>();
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] arr = new int[n];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 1; i <= m; i++) {
            treeSet.add(i);
        }

        int answer = 0;

        for (int i = 0; i < n; i++) {
            if (treeSet.floor(arr[i]) != null) {
                int num = treeSet.floor(arr[i]);
                treeSet.remove(num);
                answer += 1;
            } else {
                break;
            }
        }

        System.out.println(answer);



    }
}