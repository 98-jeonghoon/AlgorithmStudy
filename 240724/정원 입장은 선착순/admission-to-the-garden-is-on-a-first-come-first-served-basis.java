import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        PriorityQueue<People> arrivalQueue = new PriorityQueue<>();
        PriorityQueue<People> waitQueue = new PriorityQueue<>(new Comparator<People>(){
            public int compare(People o1, People o2) {
                return Integer.compare(o1.idx, o2.idx);
            }
        });

        int n = Integer.parseInt(st.nextToken());

        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            int arrive = Integer.parseInt(st.nextToken());
            int stay = Integer.parseInt(st.nextToken());
            arrivalQueue.add(new People(i, arrive, stay));
        }

        int nowTime = 0;
        int maxWaitTime = 0;

        while (!arrivalQueue.isEmpty() || !waitQueue.isEmpty()) {
            if (!arrivalQueue.isEmpty() && (waitQueue.isEmpty() || arrivalQueue.peek().arrive <= nowTime)) {
                People person = arrivalQueue.poll();
                if (nowTime < person.arrive) {
                    nowTime = person.arrive;
                }
                waitQueue.add(person);
            } else if (!waitQueue.isEmpty()) {
                People person = waitQueue.poll();
                maxWaitTime = Math.max(maxWaitTime, nowTime - person.arrive);
                nowTime += person.stay;
            }
        }

        System.out.println(maxWaitTime);
//        for (People people : arrivalQueue) {
//            System.out.println(people.idx + " " + people.arrive + " " + people.stay);
//        }
    }
}

class People implements Comparable<People>{
    int idx, arrive, stay;

    public People(int idx, int arrive, int stay){
        this.idx = idx;
        this.arrive = arrive;
        this.stay = stay;
    }


    @Override
    public int compareTo(People people) {
        // 도착 시간이 가장 빠른순, idx 가 작은순으로 들어감
        if (this.arrive != people.arrive) {
            return Integer.compare(this.arrive, people.arrive);
        } else {
            return Integer.compare(this.idx, people.idx);
        }
    }
}