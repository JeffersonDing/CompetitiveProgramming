import java.util.Scanner;
public class Winning_Score {
    public static void main(String []args){
        Scanner input= new Scanner(System.in);
        int ascore=input.nextInt()*3+input.nextInt()*2+input.nextInt();
        int bscore=input.nextInt()*3+input.nextInt()*2+input.nextInt();
        if(ascore>bscore){
            System.out.println("A");
        }else if(ascore<bscore){
            System.out.println("B");
        }else{
            System.out.println("T");
        }

    }
}
