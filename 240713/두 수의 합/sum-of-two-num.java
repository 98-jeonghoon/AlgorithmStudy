import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
public class Main {
    static int n, m;
    static int answer = 0;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        HashMap<Integer, Integer> hashMap = new HashMap<>();

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            int nowValue = Integer.parseInt(st.nextToken());
            if (hashMap.containsKey(nowValue)) {
                hashMap.put(nowValue, hashMap.get(nowValue) + 1);
            }else{
                hashMap.put(nowValue, 1);
            }

            if (hashMap.containsKey(m - nowValue)) {
                hashMap.put(nowValue, hashMap.get(nowValue) - 1);
                hashMap.put(m - nowValue, hashMap.get(m - nowValue) - 1);
                answer++;
            }
        }
        System.out.println(answer);

    }
}