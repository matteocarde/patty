#! /usr/bin/env python
# -*- coding: utf-8 -*-

from . import pddl

if __name__ == "__main__":
  task = pddl.open()
  task.dump()
