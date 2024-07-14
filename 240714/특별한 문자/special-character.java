import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        HashMap<Character, Integer> hashMap = new HashMap<>();
        String word = br.readLine();
        char[] parseWord = word.toCharArray();

        for (int i = 0; i < parseWord.length; i++) {
            hashMap.put(parseWord[i], hashMap.getOrDefault(parseWord[i], 0) + 1);
        }
        
        
        for (char c : word.toCharArray()) {
            if (hashMap.get(c) == 1) {
                System.out.println(c);
                return;
            }
        }

        System.out.println("None");
        
    }
}