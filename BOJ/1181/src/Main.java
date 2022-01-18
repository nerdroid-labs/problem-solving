import java.io.*;
import java.util.Comparator;
import java.util.HashSet;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());
        HashSet<String> set = new HashSet<>();

        for (int i = 0; i < N; i++) {
            set.add(br.readLine().strip());
        }

        set.stream()
                .sorted(Comparator
                        .comparing(String::length)
                        .thenComparing(String::compareTo)
                )
                .forEach(System.out::println);
    }
}
