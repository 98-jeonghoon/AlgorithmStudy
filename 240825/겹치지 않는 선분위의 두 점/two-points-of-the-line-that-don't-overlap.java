import java.io.*;
import java.util.*;

public class Main {
    static int n, m;
    static List<segments> segment;
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        segment = new ArrayList<>();

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            segment.add(new segments(a, b));
        }

        Collections.sort(segment);

        int left = 1;
        int right = 1000000000;
        int answer = 0;

        while (left <= right) {
            int mid = (left + right) / 2;
            if (check(mid)) {
                answer = mid;
                left = mid + 1;
            }else
                right = mid - 1;
        }

        System.out.println(answer);

    }

    static boolean check(int mid) {
        int cnt = 0;
        int lastPosition = -1;

        for (segments s : segment) {
            int start = s.start;
            int end = s.end;

            if (lastPosition < start) {
                lastPosition = start;
            }

            while (lastPosition <= end) {
                cnt++;
                lastPosition += mid;
                if (cnt >= n) {
                    return true;
                }
            }
        }

        return cnt >= n;
    }

    static class segments implements Comparable<segments>{
        int start, end;

        public segments(int start, int end) {
            this.start = start;
            this.end = end;
        }


        @Override
        public int compareTo(segments o) {
            int result = Integer.compare(this.start, o.start);
            return result;
        }
    }

}