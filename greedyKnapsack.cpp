#include <iostream.h>
#include <conio.h>

void greedyKnapsack()
{
    int n = 4;

    int weight[4] = {2, 3, 4, 5};
    int profit[4] = {3, 4, 5, 6};

    float ratio[4];

    int capacity = 5;

    int i, j;

    // Calculate ratio
    for (i = 0; i < n; i++)
        ratio[i] = (float)profit[i] / weight[i];

    // Sort by ratio descending
    for (i = 0; i < n - 1; i++)
    {
        for (j = i + 1; j < n; j++)
        {
            if (ratio[i] < ratio[j])
            {
                float temp = ratio[i];
                ratio[i] = ratio[j];
                ratio[j] = temp;

                int t = weight[i];
                weight[i] = weight[j];
                weight[j] = t;

                t = profit[i];
                profit[i] = profit[j];
                profit[j] = t;
            }
        }
    }

    int totalProfit = 0;
    int remaining = capacity;

    cout << "Greedy Knapsack Solution\n";
    cout << "Selected items:\n";

    for (i = 0; i < n; i++)
    {
        if (weight[i] <= remaining)
        {
            cout << "Weight: " << weight[i]
                 << " Profit: " << profit[i] << "\n";

            remaining -= weight[i];
            totalProfit += profit[i];
        }
    }

    cout << "Total Profit (Greedy): " << totalProfit;
}

void main()
{
    clrscr();

    greedyKnapsack();

    getch();
}