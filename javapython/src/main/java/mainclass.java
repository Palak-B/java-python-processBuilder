import java.io.IOException;

public class mainclass
{

    public static void main(String a[])
    {
        ProcessBuilder pb = new ProcessBuilder("python",
            "/Users/i506644/workbench/workbench/javapython/src/main/java/owb.py");

        Process p;

        {
            try {
                pb.redirectErrorStream(true);

                p = pb.start();

            }
            catch (IOException e) {
                System.out.println("Exception");
                e.printStackTrace();
            }
        }
        System.out.println("Saved");
    }

}
