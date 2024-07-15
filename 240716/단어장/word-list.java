import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        TreeMap<String, Integer> treeMap = new TreeMap<>();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        for (int i = 0; i < n; i++) {
            String value = sc.next();
            treeMap.put(value, treeMap.getOrDefault(value, 0) + 1);
        }

        for (Map.Entry<String, Integer> entry : treeMap.entrySet()) {
            System.out.println(entry.getKey() + " " + entry.getValue());
        }
    }
}