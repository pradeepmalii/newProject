#include<iostream.h>
#include<conio.h>
#include<string.h>
int max(int a, int b)
{
return (a > b) ? a : b;
}
void main()
{
clrscr();
char X[20], Y[20];
int m, n, i, j;
cout<<"Enter first string: ";
cin>>X;
cout<<"Enter second string: ";
cin>>Y;

m = strlen(X);
n = strlen(Y);
int dp[20][20];
// Initialize first row and column
for(i = 0; i <= m; i++)
dp[i][0] = 0;
for(j = 0; j <= n; j++)
dp[0][j] = 0;
// Fill DP table

for(i = 1; i <= m; i++)
{
for(j = 1; j <= n; j++)
{
if(X[i-1] == Y[j-1])
dp[i][j] = dp[i-1][j-1] + 1;
else
dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
}
}
cout<<"\nLength of LCS is: "<<dp[m][n];
getch();
}
