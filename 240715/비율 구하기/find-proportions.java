import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = Integer.parseInt(scanner.nextLine());

        TreeMap<String, Integer> map = new TreeMap<>();
        for (int i = 0; i < n; i++) {
            String str = scanner.nextLine();
            map.put(str, map.getOrDefault(str, 0) + 1);
        }
        
        double total = n;
        for (Map.Entry<String, Integer> entry : map.entrySet()) {
            String key = entry.getKey();
            int count = entry.getValue();
            double percentage = (count / total) * 100;
            System.out.printf("%s %.4f%n", key, percentage);
        }
        
        scanner.close();
    }
}