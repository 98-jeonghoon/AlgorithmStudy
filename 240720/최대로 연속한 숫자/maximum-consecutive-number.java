import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();

        TreeSet<Integer> set = new TreeSet<>();
        for (int i = 0; i <= n; i++) {
            set.add(i);
        }

        int[] toRemove = new int[m];
        for (int i = 0; i < m; i++) {
            toRemove[i] = sc.nextInt();
        }

        for (int i = 0; i < m; i++) {
            int num = toRemove[i];

            // 현재 숫자 제거
            set.remove(num);

            // 현재 상태에서 가장 긴 연속된 부분 수열의 길이 계산
            int maxLen = 0;
            int currentLen = 0;
            Integer prev = null;
            for (Integer val : set) {
                if (prev == null || val == prev + 1) {
                    currentLen++;
                } else {
                    maxLen = Math.max(maxLen, currentLen);
                    currentLen = 1;
                }
                prev = val;
            }
            maxLen = Math.max(maxLen, currentLen); // 마지막 구간 체크

            // 결과 출력
            System.out.println(maxLen);
        }
    }
}