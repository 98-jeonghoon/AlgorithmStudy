import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        TreeMap<Integer, Integer> treeMap = new TreeMap<>();

        int n = Integer.parseInt(st.nextToken());
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            String command = st.nextToken();

            if (command.equals("add")) {
                int key = Integer.parseInt(st.nextToken());
                int value = Integer.parseInt(st.nextToken());
                treeMap.put(key, value);
                continue;
            }

            if (command.equals("find")) {
                int findValue = Integer.parseInt(st.nextToken());
                if (treeMap.containsKey(findValue)) {
                    System.out.println(treeMap.get(findValue));
                }else{
                    System.out.println("None");
                }
                continue;
            }

            if (command.equals("remove")) {
                int removeValue = Integer.parseInt(st.nextToken());
                treeMap.remove(removeValue);
                continue;
            }

            if (command.equals("print_list")) {
                if (treeMap.isEmpty()) {
                    System.out.println("None");
                }else{
                    for (Map.Entry<Integer, Integer> entry : treeMap.entrySet()) {
                        System.out.print(entry.getValue() + " ");
                    }
                    System.out.println();
                }
            }
        }
    }
}