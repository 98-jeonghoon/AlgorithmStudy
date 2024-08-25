import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int M = sc.nextInt();
        List<int[]> segments = new ArrayList<>();

        for (int i = 0; i < M; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            segments.add(new int[]{a, b});
        }

        Collections.sort(segments, Comparator.comparingInt(o -> o[0]));

        int left = 1;
        int right = 1000000000;
        int answer = 0;

        while (left <= right) {
            int mid = (left + right) / 2;

            if (canPlacePoints(segments, N, mid)) {
                answer = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        System.out.println(answer);
    }

    private static boolean canPlacePoints(List<int[]> segments, int N, int d) {
        int count = 0;
        int lastPosition = -1;

        for (int[] segment : segments) {
            int start = segment[0];
            int end = segment[1];

            if (lastPosition < start) {
                lastPosition = start;
            }

            while (lastPosition <= end) {
                count++;
                lastPosition += d;

                if (count >= N) {
                    return true;
                }
            }
        }

        return count >= N;
    }
}