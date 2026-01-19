#define _CRT_SECURE_NO_WARNINGS 

#include <iostream> 

#include <vector> 

#include <queue> 

#include <limits> 

#include <cstdlib> 

#include <ctime> 
#include <iomanip>

using namespace std;



void generateRandomGraph(vector<vector<int>>& G, int numV) {

	for (int i = 0; i < numV; ++i) {

		for (int j = i; j < numV; ++j) {

			if (i == j) {

				G[i][j] = 0;

			}

			else {

				int weight = rand() % 11;



				if (rand() % 2 == 0) {

					G[i][j] = G[j][i] = weight;

				}

				else {

					G[i][j] = G[j][i] = 0;

				}

			}

		}

	}

}



void printMatrix(const vector<vector<int>>& G) {

	int n = G.size();

	cout << "Матрица смежности:\n";

	for (int i = 0; i < n; ++i) {

		for (int j = 0; j < n; ++j) {

			cout << G[i][j] << "\t";

		}

		cout << "\n";

	}

}



vector<int> dijkstra(const vector<vector<int>>& G, int start) {

	int n = G.size();

	vector<int> dist(n, INT_MAX);

	vector<bool> visited(n, false);

	dist[start] = 0;



	for (int i = 0; i < n; ++i) {

		int u = -1;

		int minDist = INT_MAX;

		for (int v = 0; v < n; ++v) {

			if (!visited[v] && dist[v] < minDist) {

				minDist = dist[v];

				u = v;

			}

		}

		if (u == -1) break;

		visited[u] = true;

		for (int v = 0; v < n; ++v) {

			if (G[u][v] > 0 && dist[u] != INT_MAX && dist[u] + G[u][v] < dist[v]) {

				dist[v] = dist[u] + G[u][v];

			}

		}

	}

	return dist;

}



void analyzeGraph(const vector<vector<int>>& G) {

	int n = G.size();

	vector<vector<int>> allDistances(n);

	vector<int> eccentricities(n, 0);



	int radius = INT_MAX;

	int diameter = -1;





	for (int i = 0; i < n; ++i) {

		vector<int> dist = dijkstra(G, i);

		allDistances[i] = dist;

		int maxDist = 0;

		for (int j = 0; j < n; ++j) {

			if (dist[j] != INT_MAX && dist[j] > maxDist) {

				maxDist = dist[j];

			}

		}

		eccentricities[i] = maxDist;

		if (maxDist < radius) radius = maxDist;

		if (maxDist > diameter) diameter = maxDist;

	}



	cout << "Радиус = " << radius << "\n";

	cout << "Диаметр = " << diameter << "\n";





	cout << "Центральные вершины:\n";

	for (int i = 0; i < n; ++i) {

		if (eccentricities[i] == radius) {

			cout << i << "";

		}

	}

	cout << "\n";





	cout << "Периферийные вершины:\n";

	for (int i = 0; i < n; ++i) {

		if (eccentricities[i] == diameter) {

			cout << i << "";

		}

	}

	cout << "\n";

	cout << "Экстраситеты:\n";
	

	for (int i = 0; i < n; ++i) {

		cout << eccentricities[i] << " ";

	}

}

void findAndPrintExtremities(const vector<vector<int>>& G) {

	int n = G.size();

	vector<int> degrees(n, 0);

	for (int i = 0; i < n; ++i) {

		int deg = 0;

		for (int j = 0; j < n; ++j) {

			if (G[i][j] > 0) {

				++deg;

			}

		}

		degrees[i] = deg;

	}

	int maxDeg = *max_element(degrees.begin(), degrees.end());

	//cout <<"Экстрасит(ы) с максимальной степенью ("<< maxDeg <<"): "; 

	//for (int i = 0; i < n; ++i) { 

	//if (degrees[i] == maxDeg) { 

	//cout << eccentricities[i] <<" ";

	//} 

	//} 

	//cout <<"\n"; 

}



int main() {

	setlocale(LC_ALL, "RUS");

	srand(static_cast<unsigned>(time(nullptr)));

	int numG;

	cout << "Введите число вершин: ";

	cin >> numG;



	vector<vector<int>> G(numG, vector<int>(numG, 0));



	generateRandomGraph(G, numG);

	printMatrix(G);



	analyzeGraph(G);

	findAndPrintExtremities(G);



	return 0;

}