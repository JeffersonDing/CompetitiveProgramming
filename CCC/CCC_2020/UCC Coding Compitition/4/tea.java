import java.util.*;
public class tea{
  public static void main(String[] args){
    ArrayList<Double> price = new ArrayList<Double>(Arrays.asList(100.00,100.00,4.00));
    System.out.println(bubble.solve(price));
    }
  }
class bubble{
  public static Double cost(ArrayList<Double> x){
    switch(x.size()){
      case 0: return 0.00;
      case 1: return x.get(0);
      case 2: return Math.min(x.get(0), x.get(1))*0.75+Math.max(x.get(0), x.get(1));
      case 3:
      Double n = Math.min(x.get(0), Math.min(x.get(1), x.get(2)))*0.5;
      x.remove(Math.min(x.get(0), Math.min(x.get(1), x.get(2))));
      return n+x.get(0)+x.get(1);
    }
    return -1.0;
  }



  private static double three(ArrayList<Double> x,ArrayList<Double> n,int length){
    n.removeRange(length-1,length-3);
    return solve(x)+cost(Arrays.asList(n.get(length-1),n.get(length-2),n.get(length-3)));
  }


  private static double two(ArrayList<Double> x,ArrayList<Double> n,int length){
    x.removeRange(length-1,length-2);
    return solve(x)+cost(Arrays.asList(n.get(length-1),n.get(length-2)));
  }


  private static double one(ArrayList<Double> x,ArrayList<Double> n,int length){
    x.remove(length-1);
    return solve(x)+cost(Arrays.asList(n.get(length-1)));
  }


  public static Double solve(ArrayList<Double> num){
    int length = n.size();
    if(length < 4){
      return cost(num);
    }else{
      double optimal = Math.min(one(num,num,length),Math.min(two(num,num,length),three(num,num,length)));
      return optimal;
  }
}





}
