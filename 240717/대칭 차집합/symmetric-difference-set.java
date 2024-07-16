import java.util.*;
import java.io.*;

public class Main {
    static int n, m;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        HashSet<Integer> hashSetA = new HashSet<>();
        HashSet<Integer> hashSetB = new HashSet<>();

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            hashSetA.add(Integer.parseInt(st.nextToken()));
        }

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            hashSetB.add(Integer.parseInt(st.nextToken()));
        }

        int answer = 0;

        for (Integer element : hashSetA) {
            if (!hashSetB.contains(element)) {
                answer += 1;
            }
        }

        for (Integer element : hashSetB) {
            if (!hashSetA.contains(element)) {
                answer += 1;
            }
        }

        System.out.println(answer);
    }
}