import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
public class Main {
    static int n, key, value;
    static String command;
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());

        HashMap<Integer, Integer> hashMap = new HashMap<>();

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            command = st.nextToken();
            key = Integer.parseInt(st.nextToken());
            if (command.equals("add")) {
                value = Integer.parseInt(st.nextToken());
                hashMap.put(key, value);
                continue;
            }
            if (command.equals("find")) {
                if (hashMap.containsKey(key)) {
                    System.out.println(hashMap.get(key));
                } else {
                    System.out.println("None");
                }
                continue;
            }
            if (command.equals("remove")) {
                hashMap.remove(key);
                continue;
            }

        }

    }
}