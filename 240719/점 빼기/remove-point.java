import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        TreeSet<Pointer> treeSet = new TreeSet<>();
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            treeSet.add(new Pointer(x, y));
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int query = Integer.parseInt(st.nextToken());
            Pointer result = treeSet.ceiling(new Pointer(query, Integer.MIN_VALUE));

            if (result != null) {
                System.out.println(result.x + " " + result.y);
                treeSet.remove(result);
            }else{
                System.out.println("-1 -1");
            }
        }
    }
}

class Pointer implements Comparable<Pointer>{
    int x, y;

    public Pointer(int x, int y){
        this.x = x;
        this.y = y;
    }

    @Override
    public int compareTo(Pointer pointer) {
        if (this.x == pointer.x) {
            return Integer.compare(this.y, pointer.y);
        }
        return Integer.compare(this.x, pointer.x);
    }
}