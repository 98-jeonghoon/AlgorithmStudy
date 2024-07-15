import java.util.*;
import java.io.*;

public class Main {
    static int n, k;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        
        List<int[]> moves = new ArrayList<>();
        for (int i = 0; i < k; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            moves.add(new int[]{a, b});
        }
        
        Map<Integer, HashSet<Integer>> map = new HashMap<>();
        for (int i = 1; i <= n; i++) {
            map.put(i, new HashSet<>());
            map.get(i).add(i);
        }
        
        int[] positions = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            positions[i] = i;
        }
        
        for (int i = 0; i < 3; i++) {
            for (int[] move : moves) {
                int idx1 = move[0];
                int idx2 = move[1];
                
                int person1 = positions[idx1];
                int person2 = positions[idx2];

                positions[idx1] = person2;
                positions[idx2] = person1;
                
                map.get(person1).add(idx2);
                map.get(person2).add(idx1);
            }
        }
        
        for (int i = 1; i <= n; i++) {
            System.out.println(map.get(i).size());
        }
    }
}