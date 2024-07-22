import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    static int t, m;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        t = Integer.parseInt(st.nextToken());

        for (int i = 0; i < t; i++) {
            StringBuilder sb = new StringBuilder();
            PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Comparator.reverseOrder());
            PriorityQueue<Integer> minHeap = new PriorityQueue<>();

            st = new StringTokenizer(br.readLine());
            m = Integer.parseInt(st.nextToken());

            st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= m; j++) {
                int value = Integer.parseInt(st.nextToken());
                // maxHeap과 minHeap의 사이즈가 같다면 일단 maxHeap에 넣음
                if (maxHeap.size() == minHeap.size()) {
                    maxHeap.add(value);
                }else{
                    minHeap.add(value);
                }

                // 각 root의 대소를 비교하여 minHeap의 root값이 maxHeap의 root값보다 작다면 두수를 바꿔줌
                if (!maxHeap.isEmpty() && !minHeap.isEmpty()) {
                    int maxHeapRoot = maxHeap.poll();
                    int minHeapRoot = minHeap.poll();
                    if (minHeapRoot < maxHeapRoot) {
                        maxHeap.add(minHeapRoot);
                        minHeap.add(maxHeapRoot);
                    }
                    else{
                        maxHeap.add(maxHeapRoot);
                        minHeap.add(minHeapRoot);
                    }
                }

                if (j % 2 == 1) {
                    sb.append(maxHeap.peek()).append(" ");
                }
            }
            System.out.println(sb);

        }
    }
}