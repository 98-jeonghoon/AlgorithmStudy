import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        PriorityQueue<Integer> first = new PriorityQueue<>();
        PriorityQueue<Integer> second = new PriorityQueue<>();
        PriorityQueue<Point> pq = new PriorityQueue<>();

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            first.add(Integer.parseInt(st.nextToken()));
        }

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            second.add(Integer.parseInt(st.nextToken()));
        }

        while (!first.isEmpty()) {
            int value = first.poll();
            for (int secValue : second) {
                pq.add(new Point(value, secValue));
            }
        }

        for (int i = 0; i < pq.size(); i++) {
            if (i == k - 1) {
                break;
            }
            pq.poll();
        }

        Point answer = pq.poll();
        System.out.println(answer.x + answer.y);
    }
}

class Point implements Comparable<Point> {
    int x, y;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public int compareTo(Point point) {
        return Integer.compare(this.x + this.y, point.x + point.y);
    }
}