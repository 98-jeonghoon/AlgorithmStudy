import java.util.*;

public class Main {
    static int[] parent;
    static int[] size;
    static boolean[] invited;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // 입력 받기
        int N = scanner.nextInt();
        int G = scanner.nextInt();
        List<int[]> groups = new ArrayList<>();

        for (int i = 0; i < G; i++) {
            int groupSize = scanner.nextInt();
            int[] group = new int[groupSize];
            for (int j = 0; j < groupSize; j++) {
                group[j] = scanner.nextInt();
            }
            groups.add(group);
        }

        // Union-Find 초기화
        parent = new int[N + 1];
        size = new int[N + 1];
        invited = new boolean[N + 1];

        for (int i = 1; i <= N; i++) {
            parent[i] = i;
            size[i] = 1;
        }

        // 1번 사람은 무조건 초대장을 받음
        invited[1] = true;

        // 그룹 정보를 이용해 Union 연산 수행
        for (int[] group : groups) {
            for (int i = 1; i < group.length; i++) {
                union(group[0], group[i]);
            }
        }

        // 초대장을 받을 확실한 사람들을 추적
        for (int[] group : groups) {
            int count = 0;
            for (int person : group) {
                if (invited[find(person)]) {
                    count++;
                }
            }
            if (count == group.length - 1) {
                for (int person : group) {
                    invited[find(person)] = true;
                }
            }
        }

        // 확실하게 초대장을 받는 인원 수 계산
        Set<Integer> uniqueInvited = new HashSet<>();
        for (int i = 1; i <= N; i++) {
            if (invited[find(i)]) {
                uniqueInvited.add(find(i));
            }
        }

        System.out.println(uniqueInvited.size());
        scanner.close();
    }

    // Find 연산 (경로 압축)
    static int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    // Union 연산 (사이즈 기반)
    static void union(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);

        if (rootX != rootY) {
            if (size[rootX] < size[rootY]) {
                parent[rootX] = rootY;
                size[rootY] += size[rootX];
            } else {
                parent[rootY] = rootX;
                size[rootX] += size[rootY];
            }
        }
    }
}