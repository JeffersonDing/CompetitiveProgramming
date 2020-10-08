import java.util.*;
public class MinStack{
    public static void main(String[] args){
      Stack minStack = new Stack();
      minStack.push(2);
      minStack.push(0);
      minStack.push(3);
      minStack.push(0);
      minStack.pop();
      minStack.pop();
      minStack.pop();
      System.out.println(minStack.getMin());
      minStack.printStack();
    }
}
class Stack {
    /** initialize your data structure here. */
    private static class Node{
      private int data;
      private Node next;
      private Node(int data){
        this.data=data;
      }
    }
    private Node top = new Node(0);
    public void push(int x) {
        Node node = new Node(x);
        node.next=top;
        top=node;
        }

    public void pop() {
        top = top.next;
    }

    public int top() {
      return top.data;
    }

    public int getMin() {
      int min=top.data;
      Node curr = top;
      while(curr.next!=null){
        if(curr.data<min){
          min=curr.data;
        }
        curr=curr.next;
      }
      return min;
    }
    public void printStack(){
      ArrayList<Integer> stack = new ArrayList<Integer>();
      Node curr = top;
      while(curr.next!=null){
        stack.add(curr.data);
        curr=curr.next;
      }
      System.out.println(stack);
}
}
/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */
