import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    static class Point {
        int x, y;
        Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
    
    static int getDistanceSquared(Point p1, Point p2) {
        return (p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y);
    }

    public static int findMinMaxDistance(List<Point> points, int m) {
        int minMaxDistanceSquared = Integer.MAX_VALUE;
        
        List<List<Point>> combinations = generateCombinations(points, m);
        
        for (List<Point> selectedPoints : combinations) {
            int maxDistanceSquared = 0;
            
            for (int i = 0; i < selectedPoints.size(); i++) {
                for (int j = i + 1; j < selectedPoints.size(); j++) {
                    int distanceSquared = getDistanceSquared(selectedPoints.get(i), selectedPoints.get(j));
                    maxDistanceSquared = Math.max(maxDistanceSquared, distanceSquared);
                }
            }
            
            minMaxDistanceSquared = Math.min(minMaxDistanceSquared, maxDistanceSquared);
        }
        
        return minMaxDistanceSquared;
    }
    
    public static List<List<Point>> generateCombinations(List<Point> points, int m) {
        List<List<Point>> combinations = new ArrayList<>();
        generateCombinationsHelper(points, m, 0, new ArrayList<>(), combinations);
        return combinations;
    }
    
    public static void generateCombinationsHelper(List<Point> points, int m, int start, List<Point> currentCombination, List<List<Point>> combinations) {
        if (currentCombination.size() == m) {
            combinations.add(new ArrayList<>(currentCombination));
            return;
        }
        
        for (int i = start; i < points.size(); i++) {
            currentCombination.add(points.get(i));
            generateCombinationsHelper(points, m, i + 1, currentCombination, combinations);
            currentCombination.remove(currentCombination.size() - 1);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt();
        int m = sc.nextInt();
        
        List<Point> points = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            points.add(new Point(x, y));
        }
        
        System.out.println(findMinMaxDistance(points, m));
        
        sc.close();
    }
}