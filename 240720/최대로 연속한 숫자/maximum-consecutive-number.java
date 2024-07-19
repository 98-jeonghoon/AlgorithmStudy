import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        TreeSet<Integer> s_num = new TreeSet<>();
        TreeSet<Tuple> s_len = new TreeSet<>();

        // 초기 값 설정
        s_num.add(-1);
        s_num.add(n + 1);
        s_len.add(new Tuple(n + 1, -1, n + 1));

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {

            int y = Integer.parseInt(st.nextToken());

            // y의 바로 뒤와 바로 앞의 숫자를 찾음
            int z = s_num.higher(y);
            int x = s_num.lower(y);

            // s_num에 y를 추가
            s_num.add(y);

            // 기존 구간 (x, z) 제거 및 새로운 구간 추가
            s_len.remove(new Tuple(z - x - 1, x, z));
            s_len.add(new Tuple(y - x - 1, x, y));
            s_len.add(new Tuple(z - y - 1, y, z));

            // 가장 긴 구간의 길이 출력
            Tuple best = s_len.last();
            System.out.println(best.length);
        }
    }

    // Tuple 클래스 정의
    static class Tuple implements Comparable<Tuple> {
        int length, start, end;

        Tuple(int length, int start, int end) {
            this.length = length;
            this.start = start;
            this.end = end;
        }

        @Override
        public int compareTo(Tuple other) {
            if (this.length != other.length) {
                return Integer.compare(this.length, other.length);
            } else if (this.start != other.start) {
                return Integer.compare(this.start, other.start);
            } else {
                return Integer.compare(this.end, other.end);
            }
        }

    }
}