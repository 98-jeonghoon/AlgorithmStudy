import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int N = scanner.nextInt();
        int G = scanner.nextInt();
        List<Set<Integer>> groups = new ArrayList<>();

        for (int i = 0; i < G; i++) {
            int groupSize = scanner.nextInt();
            Set<Integer> group = new HashSet<>();
            for (int j = 0; j < groupSize; j++) {
                group.add(scanner.nextInt());
            }
            groups.add(group);
        }

        // 초대장을 받을 확실한 사람들을 저장할 집합
        Set<Integer> invited = new HashSet<>();
        // 1번 사람은 무조건 초대장을 받음
        invited.add(1);

        boolean changed = true;

        while (changed) {
            changed = false;

            for (Set<Integer> group : groups) {
                // 현재 그룹에서 초대된 사람 수를 센다
                int count = 0;
                for (int person : group) {
                    if (invited.contains(person)) {
                        count++;
                    }
                }

                // 그룹 내 k-1명이 초대되었다면 나머지 한 명도 초대해야 함
                if (count == group.size() - 1) {
                    for (int person : group) {
                        if (!invited.contains(person)) {
                            invited.add(person);
                            changed = true;
                        }
                    }
                }
            }
        }

        // 확실하게 초대장을 받는 인원 수 출력
        System.out.println(invited.size());

        scanner.close();
    }
}