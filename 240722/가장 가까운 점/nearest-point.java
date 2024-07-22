import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        PriorityQueue<Point> pq = new PriorityQueue<>();

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            pq.add(new Point(x, y));
        }

        for (int i = 0; i < m; i++) {
            Point nowPoint = pq.poll();
            pq.add(new Point(nowPoint.x + 2, nowPoint.y + 2));
        }

        Point answer = pq.poll();
        System.out.println(answer.x + " " + answer.y);
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
        int thisDistance = Math.abs(this.x + this.y);
        int otherDistance = Math.abs(point.x + point.y);

        if (thisDistance != otherDistance) {
            return Integer.compare(thisDistance, otherDistance);
        } else if (this.x != point.x) {
            return Integer.compare(this.x, point.x);
        }else{
            return Integer.compare(this.y, point.y);
        }
    }
}