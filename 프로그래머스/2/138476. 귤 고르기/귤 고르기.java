import java.util.*;

class Solution {
    public int solution(int k, int[] tangerine) {
        // 크기별 빈도를 저장할 HashMap
        Map<Integer, Integer> count = new HashMap<>();
        
        // 귤 크기별 빈도 계산
        for (int fruit : tangerine) {
            count.put(fruit, count.getOrDefault(fruit, 0) + 1);
        }
        
        // 빈도를 리스트에 저장
        List<Integer> arr = new ArrayList<>(count.values());
        
        // 빈도를 내림차순 정렬
        Collections.sort(arr, Collections.reverseOrder());
        
        int answer = 0;
        int total = 0;
        
        // 가장 많은 빈도의 귤부터 선택
        for (int freq : arr) {
            total += freq;
            answer++;  // 종류의 수 증가
            if (total >= k) {
                break;
            }
        }
        
        return answer;  // 최소 종류의 수 반환
    }
}
