import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        HashMap<Integer, Integer> hashMap = new HashMap<>();

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            // 만약 키가 존재한다면
            if (hashMap.containsKey(x)) {
                int nowValue = hashMap.get(x);
                // 현재 값과 들어온 값을 비교해서 현재 들어온 값이 더 작으면 그걸로 바꿈
                if (y < nowValue) {
                    hashMap.put(x, y);
                }
            } else {
                hashMap.put(x, y);
            }
        }

        int answer = 0;
        for (Map.Entry<Integer, Integer> entry : hashMap.entrySet()) {
            answer += entry.getValue();
        }

        System.out.println(answer);
    }
}