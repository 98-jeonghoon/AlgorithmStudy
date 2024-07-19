import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        Long n = Long.parseLong(st.nextToken());
        Long t = Long.parseLong(st.nextToken());

        TreeSet<Long> groups = new TreeSet<>();

        while (n-- > 0) {
            st = new StringTokenizer(br.readLine());
            long a = Long.parseLong(st.nextToken());
            long b = Long.parseLong(st.nextToken());

            long target = a + b * t;

            while (true) {
                Long higher = groups.ceiling(target);
                if (higher != null) {
                    break;
                }
                groups.remove(higher);
            }
            groups.add(target);

        }
        System.out.println(groups.size());
    }
}