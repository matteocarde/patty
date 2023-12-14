Domain parsed
Problem parsed
Grounding..
Grounding Time: 8
Aibr Preprocessing
|F|:1
|X|:3
Aibr Preprocessing
|A|:3
|P|:2
|E|:1
Delta time heuristic model:1.0
Delta time planning model:1.0
Delta time search-execution model:1.0
Delta time validation model:1
H1 Setup Time (msec): 4
Setting horizon to:NaN
Running Greedy Best First Search
h(n = s_0)=2.0
 g(n)= 8.0 h(n)=0.0
Extracting plan with execution delta: 1.0
Problem Solved

Found Plan:
0: (turnOn)
0: (gas)
0: (move)
0: (speed)
0: -----waiting---- [1.0]
1.0: (break)
1.0: (move)
1.0: (speed)
1.0: -----waiting---- [2.0]
2.0: (move)
2.0: (speed)
2.0: -----waiting---- [3.0]
3.0: (break)
3.0: (move)
3.0: (speed)
3.0: -----waiting---- [4.0]
4.0: (idle)

Plan-Length:17
Elapsed Time: 4.0
Metric (Search):8.0
Planning Time (msec): 141
Heuristic Time (msec): 2
Search Time (msec): 5
Expanded Nodes:15
States Evaluated:25
Fixed constraint violations during search (zero-crossing):0
Number of Dead-Ends detected:0
Number of Duplicates detected:9
