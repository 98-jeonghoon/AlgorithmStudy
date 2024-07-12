import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
public class Main {
    static int n, m;
    public static void main(String[] args) throws Exception {
        StringBuilder sb = new StringBuilder();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        HashMap<String, String> hashMap = new HashMap<>();

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        for (int i = 1; i <= n; i++) {
            String word = br.readLine();
            hashMap.put(word, String.valueOf(i));
            hashMap.put(String.valueOf(i), word);
        }

        for (int i = 0; i < m; i++) {
            String find = br.readLine();
            sb.append(hashMap.get(find)).append("\n");
        }
        System.out.println(sb);
//        for (Map.Entry<String, Integer> entry : hashMap.entrySet()) {
//            System.out.println("Key: " + entry.getKey() + " Value: " + entry.getValue());
//        }

    }
}