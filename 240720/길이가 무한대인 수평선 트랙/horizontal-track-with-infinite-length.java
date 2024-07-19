import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int T = sc.nextInt();

        List<Long> finalPositions = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            long start = sc.nextLong();
            long speed = sc.nextLong();
            finalPositions.add(start + speed * T);
        }

        TreeSet<Long> groups = new TreeSet<>();

        for (long position : finalPositions) {
            Long higher = groups.ceiling(position);
            if (higher != null) {
                groups.remove(higher);
            }
            groups.add(position);
        }

        System.out.println(groups.size());
    }
}