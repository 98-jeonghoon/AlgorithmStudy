import java.io.*;
import java.util.*;

public class Main {
    static int n, m, k;
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        int[][] prefixA = new int[n + 1][m + 1];
        int[][] prefixB = new int[n + 1][m + 1];
        int[][] prefixC = new int[n + 1][m + 1];

        for (int i = 1; i <= n; i++) {
            String row = br.readLine();
            for (int j = 1; j <= m; j++) {
                char ch = row.charAt(j - 1);
                prefixA[i][j] = prefixA[i - 1][j] + prefixA[i][j - 1] - prefixA[i - 1][j - 1];
                prefixB[i][j] = prefixB[i - 1][j] + prefixB[i][j - 1] - prefixB[i - 1][j - 1];
                prefixC[i][j] = prefixC[i - 1][j] + prefixC[i][j - 1] - prefixC[i - 1][j - 1];

                if (ch == 'a') {
                    prefixA[i][j]++;
                } else if (ch == 'b') {
                    prefixB[i][j]++;
                } else if (ch == 'c') {
                    prefixC[i][j]++;
                }
            }
        }

        for (int q = 0; q < k; q++) {
            st = new StringTokenizer(br.readLine());
            int r1 = Integer.parseInt(st.nextToken());
            int c1 = Integer.parseInt(st.nextToken());
            int r2 = Integer.parseInt(st.nextToken());
            int c2 = Integer.parseInt(st.nextToken());

            int cntA = prefixSumCalc(prefixA, r1, c1, r2, c2);
            int cntB = prefixSumCalc(prefixB, r1, c1, r2, c2);
            int cntC = prefixSumCalc(prefixC, r1, c1, r2, c2);

            System.out.println(cntA + " " + cntB + " " + cntC);
        }
    }

    static int prefixSumCalc(int[][] prefix, int r1, int c1, int r2, int c2) {
        return prefix[r2][c2]
                - prefix[r1 - 1][c2]
                - prefix[r2][c1 - 1]
                + prefix[r1 - 1][c1 - 1];
    }
}