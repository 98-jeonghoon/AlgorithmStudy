import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        List<int[]> points = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            points.add(new int[]{x, y});
        }

        // x 오름차순, x가 같으면 y 오름차순으로 정렬
        Collections.sort(points, (a, b) -> {
            if (a[0] == b[0]) {
                return Integer.compare(a[1], b[1]);
            }
            return Integer.compare(a[0], b[0]);
        });

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            int[] closest = null;

            // 이진 탐색으로 x 좌표가 주어진 점보다 크거나 같은 첫 번째 점을 찾기
            int left = 0;
            int right = points.size() - 1;
            while (left <= right) {
                int mid = (left + right) / 2;
                if (points.get(mid)[0] > x || (points.get(mid)[0] == x && points.get(mid)[1] >= y)) {
                    closest = points.get(mid);
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            }

            if (closest != null) {
                System.out.println(closest[0] + " " + closest[1]);
            } else {
                System.out.println("-1 -1");
            }
        }
    }
}