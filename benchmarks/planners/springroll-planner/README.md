# SPRINGROLL HAS BEEN MOVED TO GITLAB. FOLLOW [THIS LINK](git@gitlab.com:enricos83/SMT-Hybrid-Planner-public.git)


# README #

This repository contains Springroll, an SMT based planner implementing ideas from

**Numeric Planning with Disjunctive Global Constraints via SMT**

*Scala, E., Ramirez, M., Haslum, P. and Thiebaux, S., ICAPS 2016*

To run the planner you need  [JAVA 1.8](http://www.oracle.com/technetwork/java/javase/downloads/jre8-downloads-2133155.html) and [z3](https://github.com/Z3Prover/z3) installed on your machine.

Installing
JAVA 1.8 in Ubuntu versions earlier than 16.04 requires to acquire the packages
directly from Oracle as follows

```
sudo add-apt-repository ppa:webupd8team/java -y
sudo apt-get update
sudo apt-get install oracle-java8-installer
sudo apt-get install oracle-java8-set-default
```
You will need to install Z3 from its sources by following the how-to guide
provided by their authors. This means you will need to have GCC, make and Python
installed on your system. As of August 2016, the provided instructions work entirely
out of the box on Ubuntu systems. Compilation can take as much as half an hour
on laptops CPUs with modest clock speeds.



The planner reads a slightly extended version of PDDL 2.1 (Fox, M. and Long, D., 2003. PDDL2. 1: An Extension to PDDL for Expressing Temporal Planning Domains. J. Artif. Intell. Res.(JAIR), 20, pp.61-124.
Vancouver) and can be run by using:


```
./springroll -o <domain_file> -f <problem_file> -s <option>

<option> is an integer number from 0 to 3

0: 1-step semantics, no rolling-up
1: 1-step semantics, rolling-up
2: foreach-step semantics, no rolling-up
3: foreach-step semantics, rolling-up

```
#Compilation

In case you need to compile the planner simply type ```ant``` from the root directory. Note however that the low level encoding depends on a library called PPMaJal, which is provided in the ```lib``` directory but still not open sourced. Apart from lower level translation, this library handles all the PDDL parsing and something else. We plan to open source it ASAP.

For more information, send me an email (enricos83@gmail.com) or have a look at the aforementioned paper.

The version is experimental so there could be bugs. Please let me know if you find something which is not working.

The version comes with a motion planning problem in the mot_example folder. Other benchmarks can be found [here](https://bitbucket.org/enricode/sequential-numeric-planning-benchmarks)