#include<iostream.h>
#include<conio.h>
#define MAX 20
struct Job {
char id;
int deadline;
int profit;
};
void sortJobs(Job jobs[], int n) {
int i, j;
Job temp;
for(i=0; i<n-1; i++) {
for(j=0; j<n-i-1; j++) {
if(jobs[j].profit < jobs[j+1].profit) {
temp = jobs[j];
jobs[j] = jobs[j+1];
jobs[j+1] = temp;
}
}
}
}

void jobSequencing(Job jobs[], int n) {
int i, j, maxDeadline = 0, totalProfit = 0;
int slot[MAX];
for(i=0; i<n; i++) {
if(jobs[i].deadline > maxDeadline)
maxDeadline = jobs[i].deadline;
}
for(i=0; i<=maxDeadline; i++)
slot[i] = -1;
for(i=0; i<n; i++) {
for(j=jobs[i].deadline; j>0; j--) {
if(slot[j] == -1) {
slot[j] = i;
totalProfit += jobs[i].profit;
break;
}
}
}
cout<<"\nSelected Jobs: ";
for(i=1; i<=maxDeadline; i++) {
if(slot[i] != -1)
cout<<jobs[slot[i]].id<<" ";
}
cout<<"\nTotal Profit: "<<totalProfit;
}
void main() {
clrscr();
int n, i;
Job jobs[MAX];
cout<<"Enter number of jobs: ";
cin>>n;
for(i=0; i<n; i++) {
cout<<"\nEnter Job ID, Deadline, Profit: ";
cin>>jobs[i].id>>jobs[i].deadline>>jobs[i].profit;
}
sortJobs(jobs, n);
jobSequencing(jobs, n);
getch();
}