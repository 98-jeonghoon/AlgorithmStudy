import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[] first = new int[n];
        int[] second = new int[m];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            first[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            second[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(first);
        Arrays.sort(second);

        PriorityQueue<Point> pq = new PriorityQueue<>();

        for (int i = 0; i < n; i++) {
            pq.add(new Point(first[i], second[0], 0));
        }

        Point answer = null;
        for (int i = 0; i < k; i++) {
            answer = pq.poll();
            if (answer.yIndex + 1 < m) {
                pq.add(new Point(answer.x, second[answer.yIndex + 1], answer.yIndex + 1));
            }
        }

        System.out.println(answer.x + answer.y);
    }
}

class Point implements Comparable<Point> {
    int x, y, yIndex;

    public Point(int x, int y, int yIndex) {
        this.x = x;
        this.y = y;
        this.yIndex = yIndex;
    }

    @Override
    public int compareTo(Point point) {
        return Integer.compare(this.x + this.y, point.x + point.y);
    }
}