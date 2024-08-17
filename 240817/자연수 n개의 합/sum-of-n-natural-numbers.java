import java.io.*;

public class Main {
    static long s;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        s = Long.parseLong(br.readLine());
        System.out.println(findMaxN());
    }

    static int findMaxN() {
        int left = 1, right = (int)Math.sqrt(2 * s);  // s의 크기에 따른 n의 최대 범위를 설정
        int maxN = 0;

        while (left <= right) {
            int mid = (left + right) / 2;
            long sum = (long) mid * (mid + 1) / 2;  // n까지의 합을 구함

            if (sum <= s) {
                maxN = mid;
                left = mid + 1;  // 가능한 n을 더 키워보기 위해 left를 증가
            } else {
                right = mid - 1;  // 합이 s를 넘으면 n을 줄이기 위해 right를 감소
            }
        }

        return maxN;
    }
}