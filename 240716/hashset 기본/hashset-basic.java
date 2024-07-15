import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        HashSet<Integer> hashSet = new HashSet<>();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        for (int i = 0; i < n; i++) {
            String command = sc.next();
            int value = sc.nextInt();
            if (command.equals("find")) {
                if (hashSet.contains(value)) {
                    System.out.println(true);
                } else {
                    System.out.println(false);
                }
                continue;
            }
            if (command.equals("add")) {
                hashSet.add(value);
                continue;
            }
            if (command.equals("remove")) {
                hashSet.remove(value);
            }
        }
    }
}