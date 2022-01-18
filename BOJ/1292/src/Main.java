import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int A = sc.nextInt();
        int B = sc.nextInt();
        int[] total = new int[1001];

        int idx = 1;
        int num = 0;
        int sub_total = 0;

        main:while (true){
            for (int i = 0; i < num; i++){
                if (idx > 1000) break main;
                total[idx++] = sub_total += num;
            }

            num++;
        }

        System.out.println(total[B] - total[A - 1]);
    }
}
