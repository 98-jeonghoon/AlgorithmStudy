import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int T = Integer.parseInt(st.nextToken());
        for (int test = 0; test < T; test++) {
            int k = Integer.parseInt(br.readLine());
            Queue<String> queue = new LinkedList<>();
            for (int i = 0; i < k; i++) {
                queue.offer(br.readLine());
            }

            TreeSet<Integer> treeSet = new TreeSet<>();

            while (!queue.isEmpty()) {
                String commandLine = queue.poll();
                st = new StringTokenizer(commandLine);
                String command = st.nextToken();
                int n = Integer.parseInt(st.nextToken());

                if (command.equals("I")) {
                    treeSet.add(n);
                } else if (command.equals("D")) {
                    if (treeSet.isEmpty()) {
                        continue;
                    }
                    if (n == 1) {
                        treeSet.pollLast();
                    } else if (n == -1) {
                        treeSet.pollFirst();
                    }
                }
            }

            if (treeSet.isEmpty()) {
                System.out.println("EMPTY");
            } else {
                System.out.println(treeSet.last() + " " + treeSet.first());
            }
        }
    }
}