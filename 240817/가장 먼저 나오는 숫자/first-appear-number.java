import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int n, m;
    static int[] arr;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        arr = new int[n];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            int target = Integer.parseInt(st.nextToken());
            int index = lowerBound(target);
            if (index < n && target == arr[index]) {
                System.out.println(index + 1);
            }
            else {
                System.out.println(-1);
            }
        }

    }

    static int lowerBound(int target) {
        int left = 0, right = n - 1;
        int minIdx = n;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (arr[mid] >= target) {
                right = mid - 1;
                minIdx = Math.min(minIdx, mid);
            }
            else{
                left = mid + 1;
            }
        }
        return minIdx;
    }

    static int upperBound(int target) {
        int left = 0, right = n - 1;
        int minIdx = n;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (arr[mid] > target) {
                right = mid - 1;
                minIdx = Math.min(minIdx, mid);
            }
            else{
                left = mid + 1;
            }
        }
        return minIdx;
    }

}