
import java.util.*;

class Main {
    public static void main(String[] args) {
        int[] freq = {5, 9, 12, 13, 16, 45};

        PriorityQueue<Integer> pq = new PriorityQueue<>();

        for (int f : freq) {
            pq.add(f);
        }
        int cost=0;
        while(pq.size()>1){
            int a=pq.poll();
            int b=pq.poll();
            int sum=a+b;
            cost+=sum;
            pq.add(sum);
        }
        System.out.println("Minimum cost "+cost);
    }
}