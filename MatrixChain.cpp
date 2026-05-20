#include<iostream.h>
#include<conio.h>
#include<limits.h>
void main()
{
clrscr();
int n, i, j, k, L;
cout<<"Enter number of matrices: ";
cin>>n;
int p[10];

cout<<"Enter dimensions array (size "<<n+1<<"): ";
for(i = 0; i <= n; i++)
cin>>p[i];
int m[10][10];
// Initialize diagonal as 0
for(i = 0; i < n; i++)
m[i][i] = 0;
// L is chain length
for(L = 2; L <= n; L++)
{
for(i = 0; i <= n - L; i++)
{
j = i + L - 1;

m[i][j] = INT_MAX;
for(k = i; k < j; k++)
{
int cost = m[i][k] + m[k+1][j] +
p[i] * p[k+1] * p[j+1];
if(cost < m[i][j])
m[i][j] = cost;
}
}
}
cout<<"\nMinimum number of multiplications is: "
<<m[0][n-1];
getch();
}