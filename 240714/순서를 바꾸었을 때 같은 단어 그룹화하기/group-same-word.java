import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        HashMap<String, Integer> hashMap = new HashMap<>();
        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            String word = br.readLine();
            char[] chars = word.toCharArray();
            Arrays.sort(chars);
            String sortWord = new String(chars);
            hashMap.put(sortWord, hashMap.getOrDefault(sortWord, 0) + 1);
        }

        int maxValue = Integer.MIN_VALUE;

        for (Map.Entry<String, Integer> entry : hashMap.entrySet()) {
            if (entry.getValue() > maxValue) {
                maxValue = entry.getValue();
            }
        }

        System.out.println(maxValue);
    }
}