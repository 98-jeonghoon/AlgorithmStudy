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

        boolean found = false;
        char answer = 0;
        for (Map.Entry<Character, Integer> entry : hashMap.entrySet()) {
            if (entry.getValue() == 1) {
                found = true;
                answer = entry.getKey();
                break;
            }
        }
        if (found) {
            System.out.println(answer);
        }else{
            System.out.println("None");
        }
    }
}