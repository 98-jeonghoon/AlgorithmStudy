import java.io.*;
import java.util.*;

public class Main {
	static StringTokenizer st;
	static int n, A[], B[], dp[][];
	
	static int solve(int a, int b) {
		if(a == n+1 || b == n+1)
			return 0;
		
		if(dp[a][b] != -1)
			return dp[a][b];
		
		
		if(A[a] < B[b]) 
			dp[a][b] = Math.max(dp[a][b], solve(a+1, b));
		
		if(A[a] > B[b])
			dp[a][b] = Math.max(dp[a][b], solve(a, b+1) + B[b]);
		
		dp[a][b] = Math.max(dp[a][b], solve(a+1, b+1));
		
		return dp[a][b];
	}
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		A = new int[n+1];
		B = new int[n+1];
		
		st = new StringTokenizer(br.readLine());
		for(int i = 1; i <= n; i++)
			A[i] = Integer.parseInt(st.nextToken());
		st = new StringTokenizer(br.readLine());
		for(int i = 1; i <= n; i++)
			B[i] = Integer.parseInt(st.nextToken());
		
		dp = new int[n+1][n+1]; 
		for(int y = 0; y <= n; y++)
			Arrays.fill(dp[y], -1);

		int ans = solve(1, 1);
		System.out.println(ans);
	}
}