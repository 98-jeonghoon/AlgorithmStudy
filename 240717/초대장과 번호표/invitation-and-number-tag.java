import java.util.*;
import java.io.*;

public class Main {
    static int n, g;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        g = Integer.parseInt(st.nextToken());

        Map<Integer, List<Integer>> groupByPerson = new HashMap<>();
        for (int i = 1; i <= n; i++) {
            groupByPerson.put(i, new ArrayList<>());
        }

        Map<Integer, Set<Integer>> notInvitedPeopleByGroup = new HashMap<>();
        for (int i = 1; i <= g; i++) {
            notInvitedPeopleByGroup.put(i, new HashSet<>());
        }

        for (int i = 1; i <= g; i++) {
            st = new StringTokenizer(br.readLine());
            int len = Integer.parseInt(st.nextToken());
            for (int j = 0; j < len; j++) {
                int person = Integer.parseInt(st.nextToken());

                List<Integer> group = groupByPerson.get(person);
                group.add(i);

                Set<Integer> notInvitedPeople = notInvitedPeopleByGroup.get(i);
                notInvitedPeople.add(person);
            }
        }

        int answer = 0;
        boolean[] visited = new boolean[n + 1];
        Queue<Integer> queue = new LinkedList<>();
        queue.add(1);
        visited[1] = true;

        while (!queue.isEmpty()) {
            int person = queue.poll();
            answer++;

            List<Integer> group = groupByPerson.get(person);
            for (int groupNumber :
                    group) {
                Set<Integer> notInvitedPeople = notInvitedPeopleByGroup.get(groupNumber);
                notInvitedPeople.remove(person);

                if (notInvitedPeople.size() == 1) {
                    int remainPerson = new ArrayList<>(notInvitedPeople).get(0);
                    if (!visited[remainPerson]) {
                        queue.add(remainPerson);
                        visited[remainPerson] = true;
                    }
                }
            }
        }

        System.out.println(answer);
    }
}