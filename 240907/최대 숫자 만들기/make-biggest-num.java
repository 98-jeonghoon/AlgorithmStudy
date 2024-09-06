import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static Integer[] arr;
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        arr = new Integer[n];

        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        String[] strArr = new String[arr.length];
        for (int i = 0; i < arr.length; i++) {
            strArr[i] = String.valueOf(arr[i]);
        }

        Arrays.sort(strArr, new Comparator<String>(){
            @Override
            public int compare(String a, String b) {
                String first = a + b;
                String second = b + a;
                return second.compareTo(first);
            }
        });
        System.out.println(String.join("", strArr));
    }
}