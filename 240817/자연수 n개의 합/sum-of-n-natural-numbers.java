import java.io.*;
import java.util.*;

public class Main {
    public static final int MAX_S =2000000000;
    static long s;
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        s = Long.parseLong(br.readLine());
        System.out.println(parametricSeach());

    }

    static long parametricSeach(){
        long left = 1, right = MAX_S;
        long maxNum = 0;
        while(left <= right){
            long mid = (left + right) / 2;
            // 1부터 n까지 합이 s보다 같거나 작다면
            if(mid * (mid + 1) / 2 <= s ){
                left = mid + 1;
                maxNum = Math.max(maxNum, mid);
            }else{
                right = mid - 1;
            }
        }
        return maxNum;
    }
}