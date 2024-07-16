import java.util.*;
import java.io.*;

public class Main {
    static int n, m;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        String[] groupA = new String[n];
        String[] groupB = new String[n];

        for (int i = 0; i < n; i++) {
            groupA[i] = br.readLine();
        }

        for (int i = 0; i < n; i++) {
            groupB[i] = br.readLine();
        }

        int answer = 0;

        // 3개를 선택해서 비교해야함, 비교한게 서로 다르면 가짓수 1개 추가함
        for (int i = 0; i < m - 2; i++) {
            for (int j = i + 1; j < m - 1; j++) {
                for (int k = j + 1; k < m; k++) {
                    Set<String> setA = new HashSet<>();
                    Set<String> setB = new HashSet<>();

                    for (String word : groupA) {
                        setA.add("" + word.charAt(i) + word.charAt(j) + word.charAt(k));
                    }

                    for (String word : groupB) {
                        setB.add("" + word.charAt(i) + word.charAt(j) + word.charAt(k));
                    }

                    boolean isCorrect = true;
                    for (String s : setA) {
                        if (setB.contains(s)) {
                            isCorrect = false;
                            break;
                        }
                    }
                    if (isCorrect) {
                        answer += 1;
                    }
                }
            }
        }
        System.out.println(answer);
    }
}