
import java.util.*;

public class Main {
    public static void main(String[] args) {

        int[] profit = {60, 100, 120};
        int[] weight = {10, 20, 30};
        int capacity = 50;

        double[] ratio = new double[3];

        for (int i = 0; i < 3; i++) {
            ratio[i] = (double) profit[i] / weight[i];
        }

        // Sort in descending order
        for (int i = 0; i < 3; i++) {
            for (int j = i + 1; j < 3; j++) {
                if (ratio[i] < ratio[j]) {

                    double temp = ratio[i];
                    ratio[i] = ratio[j];
                    ratio[j] = temp;

                    int t = profit[i];
                    profit[i] = profit[j];
                    profit[j] = t;

                    t = weight[i];
                    weight[i] = weight[j];
                    weight[j] = t;
                }
            }
        }

        double total = 0;

        for (int i = 0; i < 3; i++) {

            if (weight[i] <= capacity) {
                total += profit[i];
                capacity -= weight[i];
            } 
            else {
                total += ratio[i] * capacity;
                break;
            }
        }

        System.out.println("Maximum Profit: " + total);
    }
}
