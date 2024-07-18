import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        TreeSet<Integer> treeSet = new TreeSet<>();
        int n = Integer.parseInt(st.nextToken());

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            String command = st.nextToken();
            if (command.equals("add")) {
                treeSet.add(Integer.parseInt(st.nextToken()));
                continue;
            }
            if (command.equals("remove")) {
                treeSet.remove(Integer.parseInt(st.nextToken()));
                continue;
            }
            if (command.equals("find")) {
                if (treeSet.contains(Integer.parseInt(st.nextToken()))) {
                    System.out.println(true);
                } else {
                    System.out.println(false);
                }
                continue;
            }
            if (command.equals("lower_bound")) {
                Integer value = treeSet.ceiling(Integer.parseInt(st.nextToken()));
                if (value != null) {
                    System.out.println(value);
                }else {
                    System.out.println("None");
                }
                continue;
            }
            if (command.equals("upper_bound")) {
                Integer value = treeSet.higher(Integer.parseInt(st.nextToken()));
                if (value != null) {
                    System.out.println(value);
                }else{
                    System.out.println("None");
                }
                continue;
            }
            if (command.equals("largest")) {
                if (!treeSet.isEmpty()) {
                    System.out.println(treeSet.last());
                } else {
                    System.out.println("None");
                } continue;
            }
            if (command.equals("smallest")) {
                if (!treeSet.isEmpty()) {
                    System.out.println(treeSet.first());
                } else {
                    System.out.println("None");
                }continue;
            }
        }
    }
}