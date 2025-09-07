#Tema Algoritmi
1. Sortare
	1.1. Implementează algoritmul Heap Sort și testează-l pe un vector de 100.000 de elemente random.
		Exemplu: input = [5, 2, 8, 1], output = [1, 2, 5, 8].

	1.2. Compară timpii de execuție pentru Merge Sort vs. Quick Sort vs. Heap Sort pe 3 seturi de date:

		- vector sortat crescător (ex: [1,2,3,4,5]),

		- vector sortat descrescător (ex: [5,4,3,2,1]),
	
		- vector random (ex: [3,1,4,5,2]).



2. Căutare
	2.1. Scrie o funcție care caută un cuvânt într-o listă de string-uri folosind căutare liniară și căutare binară.

		Exemplu: lista = ["ana", "ion", "paul"], caut "ion" → True.

	2.2. Implementare căutare într-o matrice sortată cu două metode:

	- metoda „staircase” (colțul dreapta-sus),

	- metoda „binary search” aplicată pe fiecare rând.

		Exemplu:

		matrice = [

		[1, 4, 7],

		[2, 5, 9],

		[3, 6, 10]

		], caut 5 → găsit.



3. Structuri de date		
	3.1. Implementează o coadă (queue) cu două stive.

		Exemplu: push(1), push(2), pop() → 1.

	3.2. Creează o listă dublu înlănțuită care să permită inserare, ștergere și parcurgere în ambele sensuri.

		Exemplu: listă = [1 &lt;-&gt; 2 &lt;-&gt; 3], șterge(2) → [1 &lt;-&gt; 3].



4. Grafuri
	4.1. Implementează algoritmul Dijkstra și aplică-l pe un graf cu 6 noduri.

		Exemplu: noduri = {1..6}, muchii cu ponderi pozitive, start = 1 → distanțe minime [0, 2, 4, 7, 3, 9].

	4.2. Folosește Kruskal și Prim pentru a găsi arborele parțial minim într-un graf dat. Compară rezultatele.

		Exemplu: graf cu 4 noduri, muchii {(1,2,1), (2,3,2), (3,4,3), (4,1,4)} → cost total = 6.



5. Recursivitate/Programare dinamică

	5.1. Scrie o funcție recursivă care calculează puterea unui număr (a^n) folosind exponentiere rapidă.

		Exemplu: 2^10 = 1024.

	5.2. Rezolvă problema 0/1 Knapsack cu programare dinamică și explică matricea de soluții.

		Exemplu: greutăți = [2,3,4], valori = [4,5,6], capacitate = 5 → valoare maximă = 9.



6. Algoritmi numerici

	6.1. Implementează algoritmul lui Euclid Extins și folosește-l pentru a rezolva ecuația ax + by = d.

		Exemplu: a=30, b=20 → gcd=10, soluție: 30*1 + 20*(-1) = 10.

	6.2. Scrie un program care verifică dacă un număr are o rădăcină primitivă modulo n.

		Exemplu: n=7 → rădăcini primitive: 3, 5.