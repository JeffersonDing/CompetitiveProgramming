import java.util.*;

import static java.lang.Integer.parseInt;

public class CompareStones {
    public static void main(String[] args){
        CompareStonesSolution obj = new CompareStonesSolution();
        int[] x = {239,198,980,404,413,804,912,546,849,506,917,837,210,837,917,6,723,929,506,438,267,225,533,312,568,596,82,685,138,276};
        System.out.println(obj.lastStoneWeight(x));
    }
}
class CompareStonesSolution {
   /*public int lastStoneWeight(int[] stones) {
        ArrayList<Integer> list = new ArrayList<Integer>();
        for (int i = 0; i < stones.length; i++) {
            list.add(stones[i]);
        }
        while (list.size() > 1) {
            Collections.sort(list, Collections.reverseOrder());
            if (list.get(0) == list.get(1)) {
                list.remove(0);
                list.remove(0);
            } else if (list.get(0) > list.get(1)) {
                list.set(0, list.get(0) - list.get(1));
                list.remove(1);
            } else if (list.get(0) < list.get(1)) {
                list.set(1, list.get(1) - list.get(0));
                list.remove(0);
            }
            System.out.println(Arrays.toString(list.toArray()));
        }
        if (list.size() == 0) {
            return 0;
        } else {
            return list.get(0);
        }
    }
    */

    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> queue = new PriorityQueue<>(Collections.reverseOrder());
        for(int i : stones) {
            queue.add(i);
        }
        int x;
        int y;
        while(queue.size() > 1) {
            y = queue.poll();
            x = queue.poll();
            if(y > x) {
                queue.offer(y-x);
            }
        }
        return queue.isEmpty() ? 0 : queue.poll();
    }
}