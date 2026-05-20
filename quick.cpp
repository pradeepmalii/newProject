#include <iostream.h>
#include<conio.h>
// Function to swap two elements
void swap(int &a, int &b)
{
int temp = a;
a = b;
b = temp;
}
// Partition function
int partition(int arr[], int low, int high)
{
int pivot = arr[high];
int i = low - 1;
for (int j = low; j < high; j++)
{
if (arr[j] < pivot)
{
i++;
swap(arr[i], arr[j]);
}
}
swap(arr[i + 1], arr[high]);
return i + 1;
}
// Recursive Quick Sort
void quickSort(int arr[], int low, int high)
{
if (low < high)
{
int pi = partition(arr, low, high);
quickSort(arr, low, pi - 1);
quickSort(arr, pi + 1, high);
}
}

void main()
{
clrscr();
int n,i;
cout << "Enter number of elements: ";
cin >> n;
int arr[1000];
cout << "Enter elements:\n";
for (i = 0; i < n; i++)
cin >> arr[i];
quickSort(arr, 0, n - 1);
cout << "Sorted array using Quick Sort:\n";
for (i = 0; i < n; i++)
cout << arr[i] << " ";
getch();
}