import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
public class Main {
    static int n, m;
    static int[] arr;
    public static void main(String[] args) throws Exception {
        StringBuilder sb = new StringBuilder();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        HashMap<String, Integer> hashMap = new HashMap<>();

        n = Integer.parseInt(st.nextToken());
        for (int i = 0; i < n; i++) {
            String word = br.readLine();
            if (hashMap.containsKey(word)) {
                hashMap.put(word, hashMap.get(word) + 1);
            }else{
                hashMap.put(word, 1);
            }
        }

//        for (Map.Entry<String, Integer> entry: hashMap.entrySet()) {
//            System.out.println("Key: " + entry.getKey() + " Value: " + entry.getValue());
//        }

        int maxValue = Integer.MIN_VALUE;

        for (int count : hashMap.values()) {
            if (maxValue < count) {
                maxValue = count;
            }
        }

        System.out.println(maxValue);
    }
}