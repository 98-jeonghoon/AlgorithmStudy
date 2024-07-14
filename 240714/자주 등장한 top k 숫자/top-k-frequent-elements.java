import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;
public class Main {
    static int n, k;
    static int answer = 0;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        HashMap<Integer, Integer> hashMap = new HashMap<>();
        StringBuilder sb = new StringBuilder();

        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        int[] arr = new int[n];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 0; i < n; i++) {
            if (hashMap.containsKey(arr[i])) {
                hashMap.put(arr[i], hashMap.get(arr[i]) + 1);
            }else{
                hashMap.put(arr[i], 1);
            }
        }
        List<Map.Entry<Integer, Integer>> mapToList = new LinkedList<>(hashMap.entrySet());
        List<Integer> answerSort = new ArrayList<>();

        Collections.sort(mapToList, new Comparator<Map.Entry<Integer, Integer>>() {
            @Override
            public int compare(Map.Entry<Integer, Integer> o1, Map.Entry<Integer, Integer> o2) {
                return o2.getValue().compareTo(o1.getValue());
            }
        });

        for(Map.Entry<Integer, Integer> entry : mapToList){
            answerSort.add(entry.getKey());
            if (answerSort.size() == k) {
                break;
            }
//            System.out.println(entry.getKey()+" "+entry.getValue());
        }
//        System.out.println(answerSort);
        Collections.reverse(answerSort);
        for (int i = 0; i < answerSort.size(); i++) {
            sb.append(answerSort.get(i)).append(" ");
        }
        System.out.println(sb);
    }
}