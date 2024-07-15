import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        TreeMap<Integer, Integer> treeMap = new TreeMap<>();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        for (int i = 1; i <= n; i++) {
            int value = sc.nextInt();
            if (!treeMap.containsKey(value)) {
                treeMap.put(value, i);
            }
        }

        for (Map.Entry<Integer, Integer> entry : treeMap.entrySet()) {
            System.out.println(entry.getKey() + " " + entry.getValue());
        }
    }
}