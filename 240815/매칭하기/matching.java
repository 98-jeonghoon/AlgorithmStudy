import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int count = 0;
        
        for(int i = 0; i < n; i++){
            String word = br.readLine();
            Stack<Character> stack = new Stack<>();
            for(char ch : word.toCharArray()){
                if(!stack.isEmpty() && stack.peek() == ch){
                    stack.pop();
                }else{
                    stack.push(ch);
                }
            }

            if(stack.isEmpty()){
                count++;
            }
            
        }

        System.out.println(count);
    }
}