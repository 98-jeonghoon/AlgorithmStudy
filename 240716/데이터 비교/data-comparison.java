import java.util.*;
import java.io.*;

public class Main {
    static int n, m;
    public static void main(String[] args) throws IOException {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());

        HashSet<Integer> firstSet = new HashSet<>();

        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < n; i++){
            firstSet.add(Integer.parseInt(st.nextToken()));
        }

        st = new StringTokenizer(br.readLine());
        m = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < m; i++){
            if (firstSet.contains(Integer.parseInt(st.nextToken()))) {
                System.out.printf("1" + " ");
            } else {
                System.out.printf("0" + " ");
            }
        }


    }
}