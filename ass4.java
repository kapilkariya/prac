
public class Main {
    public static void main(String[] args) {

        int[] weight = {10, 20, 30};
        int[] profit = {60, 100, 120};

        int capacity = 50;
        int n = weight.length;

        int[][] dp = new int[n + 1][capacity + 1];

        for (int i = 1; i <= n; i++) {
            for (int w = 0; w <= capacity; w++) {

                if (weight[i - 1] <= w) {

                    int take = profit[i - 1] +
                               dp[i - 1][w - weight[i - 1]];

                    int skip = dp[i - 1][w];

                    dp[i][w] = Math.max(take, skip);

                } else {
                    dp[i][w] = dp[i - 1][w];
                }
            }
        }

        System.out.println("Maximum Profit: " + dp[n][capacity]);
    }
}
