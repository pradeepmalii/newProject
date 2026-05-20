#include <iostream.h>
#include <conio.h>

int max(int a, int b)
{
    return (a > b) ? a : b;
}

/* ---------- GREEDY KNAPSACK ---------- */
void greedyKnapsack()
{
    clrscr();

    int n = 4;

    int weight[4] = {2, 3, 4, 5};
    int profit[4] = {3, 4, 5, 6};

    float ratio[4];

    int capacity = 5;

    int i, j;

    // Calculate profit/weight ratio
    for (i = 0; i < n; i++)
        ratio[i] = (float)profit[i] / weight[i];

    // Sort items by ratio in descending order
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
    cout << "Selected Items:\n";

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

    cout << "\nTotal Profit (Greedy): " << totalProfit;

    getch();
}

/* ---------- DYNAMIC PROGRAMMING KNAPSACK ---------- */
void dpKnapsack()
{
    clrscr();

    int n = 4;

    int weight[4] = {2, 3, 4, 5};
    int profit[4] = {3, 4, 5, 6};

    int capacity = 5;

    int dp[10][10];

    int i, w;

    for (i = 0; i <= n; i++)
    {
        for (w = 0; w <= capacity; w++)
        {
            if (i == 0 || w == 0)
            {
                dp[i][w] = 0;
            }
            else if (weight[i - 1] <= w)
            {
                dp[i][w] = max(
                    profit[i - 1] + dp[i - 1][w - weight[i - 1]],
                    dp[i - 1][w]
                );
            }
            else
            {
                dp[i][w] = dp[i - 1][w];
            }
        }
    }

    cout << "Dynamic Programming Knapsack Solution\n";
    cout << "Maximum Profit: " << dp[n][capacity];

    getch();
}

/* ---------- MAIN MENU ---------- */
void main()
{
    int choice;

    do
    {
        clrscr();

        cout << "0/1 KNAPSACK MENU\n";
        cout << "1. Greedy Approach\n";
        cout << "2. Dynamic Programming Approach\n";
        cout << "3. Exit\n";

        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice)
        {
            case 1:
                greedyKnapsack();
                break;

            case 2:
                dpKnapsack();
                break;

            case 3:
                cout << "Exiting Program...";
                break;

            default:
                cout << "Invalid Choice!";
                getch();
        }

    } while (choice != 3);

    getch();
}
