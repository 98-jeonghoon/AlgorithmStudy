import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
public class Main {
    static int n, m;
    public static void main(String[] args) throws Exception {
        HashMap<Integer, Integer> hashMap = new HashMap<>();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(st.nextToken());
            hashMap.put(num, hashMap.getOrDefault(num, 0) + 1);
        }

        List<topNum> list = new ArrayList<>();
        for (Map.Entry<Integer, Integer> entry : hashMap.entrySet()) {
            list.add(new topNum(entry.getKey(), entry.getValue()));
        }

        Collections.sort(list);

        for (int i = 0; i < m; i++) {
            System.out.print(list.get(i).key + " ");
        }

    }

    static class topNum implements Comparable<topNum>{
        int key;
        int values;

        public topNum(int key, int values) {
            this.key = key;
            this.values = values;
        }


        @Override
        public int compareTo(topNum topnum) {
            // 등장 횟수가 같으면 숫자가 큰 순서로 정렬
            if (this.values == topnum.values) {
                return Integer.compare(topnum.key, this.key);
            }
            return Integer.compare(topnum.values, this.values);
        }
    }
}