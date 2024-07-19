import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        // 난이도, 문제번호
        TreeMap<Integer, TreeSet<Integer>> treeMap = new TreeMap<>();
        int n = Integer.parseInt(st.nextToken());

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int P = Integer.parseInt(st.nextToken());
            int L = Integer.parseInt(st.nextToken());
            if (!treeMap.containsKey(L)) {
                treeMap.put(L, new TreeSet<>());
            }
            treeMap.get(L).add(P);
        }

        int m = Integer.parseInt(br.readLine());

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            String command = st.nextToken();
            if (command.equals("ad")) {
                int P = Integer.parseInt(st.nextToken());
                int L = Integer.parseInt(st.nextToken());
                if (!treeMap.containsKey(L)) {
                    treeMap.put(L, new TreeSet<>());
                }
                treeMap.get(L).add(P);
                continue;
            }
            if (command.equals("sv")) {
                int P = Integer.parseInt(st.nextToken());
                int L = Integer.parseInt(st.nextToken());
                if (treeMap.containsKey(L)) {
                    TreeSet<Integer> set = treeMap.get(L);
                    set.remove(P);
                    if (set.isEmpty()) {
                        treeMap.remove(L);
                    }
                }
                continue;
            }
            if (command.equals("rc")) {
                int value = Integer.parseInt(st.nextToken());
                if (value == 1) {
                    Integer lastKey = treeMap.lastKey();
                    TreeSet<Integer> lastSet = treeMap.get(lastKey);
                    System.out.println(lastSet.last());
                }else{
                    Integer firstKey = treeMap.firstKey();
                    TreeSet<Integer> firstSet = treeMap.get(firstKey);
                    System.out.println(firstSet.first());
                }
            }
        }

    }
}