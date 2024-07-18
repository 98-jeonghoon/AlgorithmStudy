import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        TreeSet<Coordinate> treeSet = new TreeSet<>();

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            treeSet.add(new Coordinate(x, y));
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            Coordinate query = new Coordinate(x, y);

            Coordinate closet = treeSet.ceiling(query);

            if (closet != null) {
                System.out.println(closet.x + " " + closet.y);
            }else{
                System.out.println("-1 -1");
            }
        }

        


    }
}

class Coordinate implements Comparable<Coordinate>{
    int x, y;

    public Coordinate(int x, int y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public int compareTo(Coordinate coordinate) {
        if (this.x == coordinate.x) {
            return Integer.compare(this.y, coordinate.y);
        }
        return Integer.compare(this.x, coordinate.x);
    }
}