import java.io.*;
import java.util.*;

public class Main {
    static int SIZE = 1000001;
    static int n, q;
    static int[] arr, prefixSum;
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        q = Integer.parseInt(st.nextToken());

        arr = new int[SIZE];
        prefixSum = new int[SIZE];

        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= n; i++) {
            int point = Integer.parseInt(st.nextToken());
            arr[i] = point;
            prefixSum[arr[i]]++;
        }

        prefixSum[0] = arr[0];
        for (int i = 1; i < SIZE; i++) {
            prefixSum[i] += prefixSum[i - 1];
        }

        for (int i = 0; i < q; i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            int answer = prefixCalc(s, e);
            if (answer > 0) {
                System.out.println(answer);
            } else {
                System.out.println(0);
            }
        }

    }

    static int prefixCalc(int s, int e) {
        if (s == 0){
            return prefixSum[e];
        }
        return prefixSum[e] - prefixSum[s - 1];
    }
}