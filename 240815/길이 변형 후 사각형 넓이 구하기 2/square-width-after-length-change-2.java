import java.io.*;
import java.util.*;

public class Main {
    static int x, y;
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        x = Integer.parseInt(st.nextToken());
        y = Integer.parseInt(st.nextToken());
        x = x * 4;
        y = y + 3;

        System.out.println(x);
        System.out.println(y);
        System.out.println(x * y);
    }
}