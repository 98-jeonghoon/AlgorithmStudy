import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static List<segment> segments;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());

        segments = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            segments.add(new segment(a, b));
        }
        int left = 1;
        int right = 1000000000;
        int answer = 1;
        Collections.sort(segments);

        while (left <= right) {
            int mid = (left + right) / 2;
            if (check(mid)) {
                answer = Math.max(answer, mid);
                left = mid + 1;
            }else{
                right = mid - 1;
            }
        }

        System.out.println(answer);

    }

    private static boolean check(int mid) {
        int nowPoint = segments.get(0).start;
        for (int i = 1; i < n; i++) {
            segment seg = segments.get(i);
            if (nowPoint + mid > seg.end) {
                return false;
            }
            nowPoint = Math.max(nowPoint + mid, seg.start);
        }
        return true;
    }

    static class segment implements Comparable<segment>{
        int start, end;

        public segment(int start, int end) {
            this.start = start;
            this.end = end;
        }


        @Override
        public int compareTo(segment o) {
            int result = Integer.compare(this.start, o.start);
            return result;
        }
    }
}