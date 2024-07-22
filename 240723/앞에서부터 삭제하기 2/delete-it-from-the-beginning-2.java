import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int N = scanner.nextInt();
        int[] nums = new int[N];
        
        for (int i = 0; i < N; i++) {
            nums[i] = scanner.nextInt();
        }
        
        System.out.printf("%.2f\n", getMaxAverageAfterDeletions(N, nums));
    }
    
    public static double getMaxAverageAfterDeletions(int N, int[] nums) {
        double maxAverage = 0;

        for (int K = 1; K <= N - 2; K++) {
            // 앞의 K개를 제외한 배열 생성
            PriorityQueue<Integer> minHeap = new PriorityQueue<>();
            int sum = 0;
            
            for (int i = K; i < N; i++) {
                minHeap.add(nums[i]);
                sum += nums[i];
            }
            
            // 가장 작은 숫자 하나를 제거합니다.
            sum -= minHeap.poll();
            
            // 나머지 숫자들의 평균을 구합니다.
            double average = (double) sum / (N - K - 1);
            maxAverage = Math.max(maxAverage, average);
        }
        
        return maxAverage;
    }
}