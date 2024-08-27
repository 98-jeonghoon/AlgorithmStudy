import java.io.*;
import java.util.*;

public class Main {
    static int n, tMax;
    static int[] arr;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        tMax = Integer.parseInt(st.nextToken());

        arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        int left = 1;
        int right = n;  // 최대 n명까지 무대에 오를 수 있으므로 초기값을 n으로 설정
        int answer = n;

        while (left <= right) {
            int mid = (left + right) / 2;
            if (canCompleteWithinTime(mid)) {
                answer = mid;  // 가능한 K 값을 갱신
                right = mid - 1;  // 더 작은 K 값을 시도해보기 위해 right를 줄임
            } else {
                left = mid + 1;  // 시간이 초과되었으므로, 더 큰 K 값을 시도
            }
        }

        System.out.println(answer);
    }

    private static boolean canCompleteWithinTime(int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();

        int currentTime = 0;
        for (int i = 0; i < n; i++) {
            if (pq.size() == k) {
                currentTime = pq.poll();  // 무대에서 가장 먼저 내려가는 사람의 시간을 가져옴
            }

            int finishTime = currentTime + arr[i];

            if (finishTime > tMax) {
                return false;  // Tmax를 초과하면 false 반환
            }
            pq.add(finishTime);
        }

        return true;
    }
}