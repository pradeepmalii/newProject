#include<iostream.h>
#include<conio.h>
#define MAX 20

struct Edge {
int u, v, weight;
};
int parent[MAX];
int find(int i) {
while(parent[i] != i)
i = parent[i];
return i;
}
void unionSet(int i, int j) {
int a = find(i);
int b = find(j);
parent[a] = b;
}
void sortEdges(Edge edges[], int e) {
int i, j;
Edge temp;
for(i=0; i<e-1; i++) {
for(j=0; j<e-i-1; j++) {
if(edges[j].weight > edges[j+1].weight) {
temp = edges[j];
edges[j] = edges[j+1];
edges[j+1] = temp;
}
}
}
}
void kruskal(Edge edges[], int n, int e) {
int i;
int totalCost = 0;
for(i=0; i<n; i++)
parent[i] = i;
sortEdges(edges, e);
cout<<"\nEdges in MST:\n";
for(i=0; i<e; i++) {
    int u = find(edges[i].u);
    int v = find(edges[i].v);

    if(u != v) {
cout<<edges[i].u<<" - "<<edges[i].v<<" Cost: "<<edges[i].weight<<"\n";
totalCost += edges[i].weight;
unionSet(u, v);
}
}
cout<<"\nTotal Cost of MST: "<<totalCost;
}
void main() {
clrscr();
int n, e, i;
Edge edges[MAX];
cout<<"Enter number of vertices: ";
cin>>n;
cout<<"Enter number of edges: ";
cin>>e;
for(i=0; i<e; i++) {
cout<<"Enter u v weight: ";
cin>>edges[i].u>>edges[i].v>>edges[i].weight;
}
kruskal(edges, n, e);
getch();
}