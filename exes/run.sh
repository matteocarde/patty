#!/bin/bash
ff -o files/plant-watering/domain.pddl -f files/plant-watering/instances/instance_4_1.pddl -s 0
python benchmarks/benchmark.py