import java.io.*;
import java.lang.*;

public class JavaRunCommand {

    public static void main(String[] args) {
        try{

            String siteName = "stackoverflow";
            int pageSize = 10;

            ProcessBuilder pb = new ProcessBuilder("python", "main.py", siteName, "" + pageSize);
            Process p = pb.start();

        } catch (IOException e){

            System.out.println(e);

        }
    }
}
