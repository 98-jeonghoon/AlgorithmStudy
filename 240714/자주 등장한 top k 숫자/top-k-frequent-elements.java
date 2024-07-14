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

        Collections.sort(mapToList, new Comparator<Map.Entry<Integer, Integer>>() {
            @Override
            public int compare(Map.Entry<Integer, Integer> o1, Map.Entry<Integer, Integer> o2) {
                if (o2.getValue().equals(o1.getValue())) {
                    return o2.getKey() - o1.getKey();
                }
                return o2.getValue() - o1.getValue();
            }
        });

        for (int i = 0; i < k; i++) {
            sb.append(mapToList.get(i).getKey()).append(" ");
        }
        
        System.out.println(sb.toString().trim());
    }
}