import java.util.Scanner;
public class Time_to_Decompress {
    public static void main(String[]args){
        Scanner input=new Scanner(System.in);
        String buffer;
        String [] ans ;

        int L = input.nextInt();
        String [] decrypt = new String[L];
        buffer = input.nextLine();
        for(int x=0;x<L;x++) {
            decrypt[x]="";
            buffer = input.nextLine();
            ans = buffer.split(" ");
            for (int y = 0; y <= Integer.parseInt(ans[0])-1; y++) {
                decrypt[x] = decrypt[x] + ans[1];
            }
        }
        for (int x=0;x<L;x++){
            System.out.println(decrypt[x]);
        }
    }
}

