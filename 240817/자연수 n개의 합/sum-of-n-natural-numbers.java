import java.io.*;

public class Main {
    static long s;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        s = Long.parseLong(br.readLine());
        System.out.println(parametricSearch());
    }

    static long parametricSearch() {
        long left = 1, right = s;  // s 자체를 최댓값으로 설정
        long maxNum = 0;

        while (left <= right) {
            long mid = (left + right) / 2;
            long sum = mid * (mid + 1) / 2;  // 1부터 mid까지의 합 계산

            if (sum <= s) {
                maxNum = mid;  // 가능한 최대 n을 업데이트
                left = mid + 1;  // n을 더 크게 탐색
            } else {
                right = mid - 1;  // n을 줄여서 탐색
            }
        }

        return maxNum;
    }
}