import java.util.Scanner;
import java.util.*;
import java.util.List;
public class Cold_Compress {
    public static void main(String[] args){
    Compress.Compress();

    }
}
class Compress {
    static int a;
    static int b = 1;
    static  String bufferS;
    static List<String> fin = new ArrayList<>();
    static List<Character> buffer = new ArrayList<>();
    static List<String> output = new ArrayList<>();
    static  Scanner input = new Scanner(System.in);
    public static void AddtoBuf(int a, char b){
        fin.add(String.valueOf(a));
        fin.add(String.valueOf(b));
    }
    public static void Compress(){
        a = input.nextInt();
        input.nextLine();
        for(int i=0;i<a;i++){
            buffer.clear();
            System.out.println();
            bufferS = input.nextLine();
            for(char x : bufferS.toCharArray()){
                buffer.add(x);
            }
            buffer.add(' ');
            for(int q = 0;q<buffer.size()-1;q++){
                if(buffer.get(q)==buffer.get(q+1)){
                    b+=1;
                }else if(buffer.get(q)!=buffer.get(q+1)){
                    AddtoBuf(b,buffer.get(q));
                    b = 1;
                }
            }
            output.add(String.join(" ",fin));
            fin.clear();

        }
        for(String line:output){
            System.out.println(line);
        }
    }


}