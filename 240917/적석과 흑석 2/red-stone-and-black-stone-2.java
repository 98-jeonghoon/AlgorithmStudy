import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static final int MAX_C = 100000;
    static int c, n;
    static int[] redStones = new int[MAX_C];
    static TreeSet<Integer> redS = new TreeSet<>();
    static ArrayList<Stone> blackStone = new ArrayList<>();
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        c = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());

        for (int i = 0; i < c; i++) {
            redStones[i] = Integer.parseInt(br.readLine());
        }

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            blackStone.add(new Stone(b, a));
        }

        for (int i = 0; i < c; i++) {
            redS.add(redStones[i]);
        }

        Collections.sort(blackStone);

        int answer = 0;
        for (int i = 0; i < n; i++) {
            int a = blackStone.get(i).a;
            int b = blackStone.get(i).b;

            if (redS.ceiling(a) != null) {
                int ti = redS.ceiling(a);
                if (ti <= b) {
                    answer++;
                    redS.remove(ti);
                }
            }
        }

        System.out.println(answer);
    }
}

class Stone implements Comparable<Stone> {
    int b, a;

    public Stone(int b, int a) {
        this.b = b;
        this.a = a;
    }

    @Override
    public int compareTo(Stone stone) {
        return this.b - stone.b;
    }
}