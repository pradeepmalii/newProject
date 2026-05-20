#include <iostream.h>
#include<conio.h>
// Function to merge two subarrays
void merge(int arr[], int left, int mid, int right)
{
int i,j,k;
int n1 = mid - left + 1;
int n2 = right - mid;
int L[1000],R[1000];
for (i = 0; i < n1; i++)
L[i] = arr[left + i];
for (j = 0; j < n2; j++)
R[j] = arr[mid + 1 + j];
i = 0, j = 0, k = left;
while (i < n1 && j < n2)
{
if (L[i] <= R[j])
arr[k++] = L[i++];
else
arr[k++] = R[j++];
}
while (i < n1)
arr[k++] = L[i++];
while (j < n2)
arr[k++] = R[j++];
}
// Recursive Merge Sort
void mergeSort(int arr[], int left, int right)
{
if (left < right)
{
int mid = left + (right - left) / 2;
mergeSort(arr, left, mid);
mergeSort(arr, mid + 1, right);
merge(arr, left, mid, right);
}
}
void main()
{
int n;
clrscr();
cout << "Enter number of elements: ";
cin >> n;
int arr[1000];
cout << "Enter elements:\n";
for (int i = 0; i < n; i++)
cin >> arr[i];
mergeSort(arr, 0, n - 1);
cout << "Sorted array using Merge Sort:\n";
for (i = 0; i < n; i++)
cout << arr[i] << " ";
getch();
}
