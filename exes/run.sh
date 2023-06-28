#!/bin/bash
pysmt-install --yices --confirm-agreement --env
pysmt-install --check
python main.py -o files/block-grouping/domain.pddl -f files/block-grouping/instances/instance_100_10_2_1.pddl ;