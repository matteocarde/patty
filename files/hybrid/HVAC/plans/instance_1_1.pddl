Domain parsed
Problem parsed
Grounding..
Grounding Time: 9
Aibr Preprocessing
|F|:1
|X|:4
Aibr Preprocessing
|A|:5
|P|:2
|E|:0
Delta time heuristic model:1.0
Delta time planning model:1.0
Delta time search-execution model:1.0
Delta time validation model:1
H1 Setup Time (msec): 4
Setting horizon to:NaN
Running Greedy Best First Search
h(n = s_0)=12.0
 g(n)= 1.0 h(n)=11.0
 g(n)= 2.0 h(n)=10.0
 g(n)= 3.0 h(n)=9.0
 g(n)= 4.0 h(n)=8.0
 g(n)= 5.0 h(n)=7.0
 g(n)= 6.0 h(n)=6.0
 g(n)= 7.0 h(n)=5.0
 g(n)= 8.0 h(n)=4.0
 g(n)= 9.0 h(n)=3.0
 g(n)= 10.0 h(n)=2.0
 g(n)= 19.0 h(n)=1.0
 g(n)= 20.0 h(n)=0.0
Extracting plan with execution delta: 1.0
Problem Solved

Found Plan:
0: (thermal_change r1)
0: (time_passing)
0: -----waiting---- [1.0]
1.0: (thermal_change r1)
1.0: (time_passing)
1.0: -----waiting---- [2.0]
2.0: (thermal_change r1)
2.0: (time_passing)
2.0: -----waiting---- [3.0]
3.0: (thermal_change r1)
3.0: (time_passing)
3.0: -----waiting---- [4.0]
4.0: (thermal_change r1)
4.0: (time_passing)
4.0: -----waiting---- [5.0]
5.0: (thermal_change r1)
5.0: (time_passing)
5.0: -----waiting---- [6.0]
6.0: (thermal_change r1)
6.0: (time_passing)
6.0: -----waiting---- [7.0]
7.0: (thermal_change r1)
7.0: (time_passing)
7.0: -----waiting---- [8.0]
8.0: (thermal_change r1)
8.0: (time_passing)
8.0: -----waiting---- [9.0]
9.0: (increase_air_flow r1)
9.0: (increase_air_flow r1)
9.0: (increase_temp r1)
9.0: (increase_temp r1)
9.0: (increase_temp r1)
9.0: (increase_temp r1)
9.0: (increase_temp r1)
9.0: (increase_air_flow r1)
9.0: (increase_temp r1)
9.0: (thermal_change r1)
9.0: (time_passing)
9.0: -----waiting---- [10.0]
10.0: (satisfier r1 k1)

Plan-Length:40
Elapsed Time: 10.0
Metric (Search):20.0
Planning Time (msec): 201
Heuristic Time (msec): 27
Search Time (msec): 64
Expanded Nodes:2838
States Evaluated:5879
Fixed constraint violations during search (zero-crossing):0
Number of Dead-Ends detected:2796
Number of Duplicates detected:6925
