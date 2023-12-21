#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pddl

if __name__ == "__main__":
    task = pddl.pddl_open()
    task.dump()
