import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;

public class Main {
  public static void main(String[] args) throws Exception {
    if (args.length != 1) {
      throw new Exception("Usage: java Main dataFile.txt");
    }

    String filename = args[0];
    FileOpener fileOpener = new FileOpener(filename);
    ArrayList<String> lines = fileOpener.openFileAsArrayOfLines();
    System.out.println(lines.toString());
  }
}
