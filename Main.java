import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) throws Exception {
        if (args.length > 2) {
            throw new Exception("Usage:\njava Main dataFile.txt\njava Main dataFile.txt debug\njava Main dataFile.txt info");
        }

        Log log = null;

        switch (args[1]) {
        case "debug":
            log = new Log(LogLevelEnum.DEBUG);
            break;
        case "info":
            log = new Log(LogLevelEnum.INFO);
            break;
        default:
            log = new Log(LogLevelEnum.OFF);
        }

        String filename = args[0];
        FileOpener fileOpener = new FileOpener(filename);
        ArrayList<String> lines = fileOpener.openFileAsArrayOfLines();
        System.out.println(lines.toString());
    }
}
