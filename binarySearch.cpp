#include <iostream.h>
#include<conio.h>
// Function for Binary Search
int binarySearch(int arr[], int n, int key)
{
int low = 0, high = n - 1;
while (low <= high)
{
int mid = low + (high - low) / 2;
if (arr[mid] == key)
return mid; // Element found
else if (arr[mid] < key)
low = mid + 1;
else
high = mid - 1;
}
return -1; // Element not found
}
void main()
{
clrscr();
int n, key;
cout << "Enter number of elements: ";
cin >> n;
int arr[100];
cout << "Enter elements in sorted order:\n";
for (int i = 0; i < n; i++)
cin >> arr[i];
cout << "Enter element to search: ";
cin >> key;
int result = binarySearch(arr, n, key);
if (result != -1)
cout << "Element found at position: " << result + 1;
else
cout << "Element not found!";
getch();
}
