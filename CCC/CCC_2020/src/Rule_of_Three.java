import java.util.Scanner;
import java.util.*;
import java.util.List;
public class Rule_of_Three {
    public static void main(String[] args){
        Rules.Setup();
    }
}
class Rules {
    static List<String> fin = new ArrayList<>();
    static int Goal;
    static String Start;
    static String End;
    static Scanner input = new Scanner(System.in);
    private static void AddtoBuf(String[] a){
        for(int i=0;i<a.length;i++){
            fin.add(a[i]);
        }
    }
    public static void Setup(){
        for(int i=0;i<4;i++) {
            AddtoBuf(input.nextLine().split(" "));
        }
        Goal=Integer.parseInt(fin.get(6));
        Start = fin.get(7);
        End = fin.get(8);
    }
}