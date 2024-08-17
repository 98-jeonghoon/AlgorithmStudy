import java.io.*;
import java.util.*;

public class Main {
    static int s = 2000000000;
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        s = Integer.parseInt(br.readLine());
        System.out.println(parametricSeach());

    }

    static int parametricSeach(){
        int left = 1, right = s;
        int maxNum = 0;
        while(left <= right){
            int mid = (left + right) / 2;
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