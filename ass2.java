import java.util.*;

class Node{
    char ch;
    int freq;
    Node left,right;
    Node(char ch,int freq){
        this.ch=ch;
        this.freq=freq;
    }
}

class Main {
    public static void main(String[] args) {
        char[] ch = {'a', 'b', 'c', 'd', 'e', 'f'};
        int[] freq = {5, 9, 12, 13, 16, 45};
        PriorityQueue<Node> pq=new PriorityQueue<>(
            (a,b)->a.freq-b.freq
        );
        for(int i=0;i<freq.length;i++){
            pq.add(new Node(ch[i],freq[i]));
        }

        while(pq.size()>1){
            Node a=pq.poll();
            Node b=pq.poll();
            Node parent=new Node('-',a.freq+b.freq);
            parent.left=a;
            parent.right=b;
            pq.add(parent);
        }
        print(pq.poll(), "");
    }
}