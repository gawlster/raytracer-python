import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;

public class FileOpener {
    Path filepath;
    String filename;

    FileOpener(String filename) {
        Path filepath = Paths.get(filename);

        this.filepath = filepath;
        this.filename = filename;
    }

    public ArrayList<String> openFileAsArrayOfLines() throws IOException {
        BufferedReader bReader = null;
        try {
            bReader = new BufferedReader(new FileReader(this.filepath.toAbsolutePath().toString()));
        } catch (IOException e) {
            System.out.println(
                String.format("Could not fine file with name %1$s in root directory. Trying to find in testCases directory",
                              this.filename));
            Path path = Paths.get(String.format("testCases/%1$s", this.filename));
            this.filepath = path;

            bReader = new BufferedReader(new FileReader(this.filepath.toAbsolutePath().toString()));
        }

        ArrayList<String> arrayOfLines = new ArrayList();

        String line = bReader.readLine();
        while (line != null) {
            arrayOfLines.add(line);
            line = bReader.readLine();
        }

        bReader.close();

        return arrayOfLines;
    }
}
