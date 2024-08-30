import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int K = Integer.parseInt(br.readLine());

        if (K >= N) {
            System.out.println(0);
            return;
        }

        int[] sensors = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            sensors[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(sensors);

        Integer[] distances = new Integer[N-1];
        for (int i = 0; i < N-1; i++) {
            distances[i] = sensors[i+1] - sensors[i];
        }

        Arrays.sort(distances, Collections.reverseOrder());

        int answer = 0;
        for (int i = K-1; i < N-1; i++) {
            answer += distances[i];
        }

        System.out.println(answer);
    }
}