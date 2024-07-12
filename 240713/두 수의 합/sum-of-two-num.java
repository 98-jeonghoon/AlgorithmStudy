import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
public class Main {
    static int n, k;
    static int answer = 0;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        HashMap<Integer, Integer> hashMap = new HashMap<>();

        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        int[] arr = new int[n];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 0; i < n; i++) {
            int nowValue = arr[i];
            int complement = k - nowValue;

            if (hashMap.containsKey(complement)) {
                answer += hashMap.get(complement);
            }

            if (hashMap.containsKey(nowValue)) {
                hashMap.put(nowValue, hashMap.get(nowValue) + 1);
            } else {
                hashMap.put(nowValue, 1);
            }
        }
        System.out.println(answer);

    }
}