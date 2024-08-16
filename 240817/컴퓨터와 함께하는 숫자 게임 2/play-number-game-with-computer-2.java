import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static long m;
    static long a, b;
    static long[] arr;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        m = Long.parseLong(br.readLine());

        arr = new long[(int)m];
        for(int i = 0; i < m; i++){
            arr[i] = i + 1;
        }

        StringTokenizer st = new StringTokenizer(br.readLine());
        a = Long.parseLong(st.nextToken());
        b = Long.parseLong(st.nextToken());

        int maxValue = Integer.MIN_VALUE;
        int minValue = Integer.MAX_VALUE;
        for(long i = a; i <= b; i++){
            int value = search(i);
            maxValue = Math.max(maxValue, value);
            minValue = Math.min(minValue, value);
        }

        System.out.println(minValue + " " + maxValue);
    }

    static int search(long target){
        int left = 0, right = (int)m - 1;
        int count = 0;
        while(left <= right){
            count++;
            int mid = (left + right) / 2;
            if(arr[mid] == target){
                break;
            }

            if(arr[mid] > target){
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return count;
    }
}