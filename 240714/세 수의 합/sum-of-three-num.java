import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int n, k;
    static int answer = 0;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        int[] arr = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        
        HashMap<Integer, Integer> hashMap = new HashMap<>();

        for (int i = 0; i < n - 2; i++) {
            for (int j = i + 1; j < n; j++) {
                int sumOfTwo = arr[i] + arr[j];
                hashMap.put(sumOfTwo, hashMap.getOrDefault(sumOfTwo, 0) + 1);
            }
        }

        for (int i = 0; i < n; i++) {
            int target = k - arr[i];
            if (hashMap.containsKey(target)) {
                answer += hashMap.get(target);
            }
        }

        System.out.println(answer / 3);
    }
}