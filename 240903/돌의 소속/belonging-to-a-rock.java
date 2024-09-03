import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int N = sc.nextInt();
        int Q = sc.nextInt();
        
        int[] group1 = new int[N + 1];
        int[] group2 = new int[N + 1];
        int[] group3 = new int[N + 1];
        
        for (int i = 1; i <= N; i++) {
            int group = sc.nextInt();
            group1[i] = group1[i - 1] + (group == 1 ? 1 : 0);
            group2[i] = group2[i - 1] + (group == 2 ? 1 : 0);
            group3[i] = group3[i - 1] + (group == 3 ? 1 : 0);
        }
        
        for (int i = 0; i < Q; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            
            int count1 = group1[b] - group1[a - 1];
            int count2 = group2[b] - group2[a - 1];
            int count3 = group3[b] - group3[a - 1];
            
            System.out.println(count1 + " " + count2 + " " + count3);
        }
        
        sc.close();
    }
}