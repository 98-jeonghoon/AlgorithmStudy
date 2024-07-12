import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
public class Main {
    static int n, m;
    static int[] arr;
    public static void main(String[] args) throws Exception{
        StringBuilder sb = new StringBuilder();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        HashMap<Integer, Integer> hashMap = new HashMap<>();

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        arr = new int[n];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            // 현재의 키값을 받는다
            int key = Integer.parseInt(st.nextToken());
            // 만약 키값이 존재하면
            if (hashMap.containsKey(key)) {
                // 현재 키에 해당하는 value를 가져오고
                int newValue = hashMap.get(key);
                // 지금 있는 key를 삭제한다
                hashMap.remove(key);
                // 다시금 key와 value를 넣어준다
                hashMap.put(key, newValue + 1);
            }else {
                // key 값이 존재하지 않는다면
                hashMap.put(key, 1);
            }
        }

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            int answer = Integer.parseInt(st.nextToken());
            if (hashMap.containsKey(answer)) {
                sb.append(hashMap.get(answer) + " ");
            } else {
                sb.append(0 + " ");
            }

        }
        System.out.println(sb);
    }
}