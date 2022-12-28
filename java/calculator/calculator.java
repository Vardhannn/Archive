package calculator;

import java.awt.*;
import javax.swing.*;

public class calculator {
    JPanel panel;
    JFrame Frame;
    JButton But;
    calculator(){
        panel = new JPanel();
        Frame = new JFrame("hehe");
        But = new JButton("But ra");

        panel.setBounds(100,100,300,300);
        panel.setBackground(Color.BLACK);

        But.setBounds(100,100,300,60);

        panel.add(But);

        Frame.add(panel);
        Frame.setSize(500,500);
        Frame.setLayout(null);
        Frame.setVisible(true);

    }
    public static void main(String[] args){
        new calculator();
    }
}
