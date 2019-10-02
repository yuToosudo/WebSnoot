/* SteamFitter
* @Bryspeelm
* Description:
* Goal: Identify extra pipes and what line they occur in a .tsv file.
* Ver 1.0
*/

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
public class SteamFitter{

    public static void main(String[] args) {
        int numOfPipes = 23; // !!do not change unless number fields change!!
        int lineNum = 1; // start at one to take header into account
        String filename = "community_users.tsv";

        // Find pipes out of range in community_users.tsv file
        try{
            //Open file
            BufferedReader reader = new BufferedReader(new FileReader(filename));
            String line;
            int count;

            //Read lines and count number of pipes
            while ((line = reader.readLine()) != null)
            {
                count =0; // reset pipe counter for each new line
                //iterate through line and find pipes
                char[] chars = line.toCharArray();
                for (char ch : chars) {
                   if(ch == '|'){
                       count++;
                   }
                }

                //print line that has too many pipes along with the number of pipes
                if (count > numOfPipes){
                    System.out.println((count - numOfPipes) + " extra pipes @ line " +
                            lineNum);
                }
                lineNum++;
            }
        }
        catch(IOException ex){
            System.out.println("Cannot find file");
        }
    }
}