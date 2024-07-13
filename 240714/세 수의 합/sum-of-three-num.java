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
            for (int j = i + 1; j < n; j++) {
                int first = arr[i];
                int second = arr[j];
                int complement = k - first - second;

                if (hashMap.containsKey(complement)) {
                    answer += hashMap.get(complement);
                }

            }
            if (hashMap.containsKey(arr[i])) {
                hashMap.put(arr[i], hashMap.get(arr[i]) + 1);
            } else {
                hashMap.put(arr[i], 1);
            }
        }
        System.out.println(answer);

    }
}