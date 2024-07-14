import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        HashMap<Integer, Integer> hashMap = new HashMap<>();
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(st.nextToken());
            hashMap.put(num, hashMap.getOrDefault(num, 0) + 1);
        }

        List<Map.Entry<Integer, Integer>> mapToList = new ArrayList<>(hashMap.entrySet());

        mapToList.sort((e1, e2) -> {
            int countComparison = Integer.compare(e2.getValue(), e1.getValue());
            if (countComparison == 0) {
                return Integer.compare(e2.getKey(), e1.getKey());
            }
            return countComparison;
        });

        for (int i = 0; i < k; i++) {
            sb.append(mapToList.get(i).getKey()).append(" ");
        }

        System.out.println(sb.toString().trim());
    }
}