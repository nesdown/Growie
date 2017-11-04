import javax.swing.*;
import java.awt.*;
import java.applet.Applet;

public class Webpage extends Applet
{
    /*public void init (Graphics g) {
        g.drawString("Hello World!", 0, 50);
    }*/

    public static void main(String[] args) {
        //Initializing all needed elements
        JPanel mainWebpage = new JPanel();
        GridLayout webLayout = new GridLayout(2, 5);
        mainWebpage.setLayout(webLayout);

        JFrame pageContainer = new JFrame("Growie");
        pageContainer.setContentPane(mainWebpage);
        pageContainer.setSize(800, 600);

        JLabel firstProject;
        JProgressBar milstonesProgress;
        JLabel currentMilestone;

    }
}
