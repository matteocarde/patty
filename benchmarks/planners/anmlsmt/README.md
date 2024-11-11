TAMER: An Application-Oriented ANML Planner
===========================================

Overview
--------

TAMER is a planner for the ANML (read as "animal") planning
specification language. The objective of TAMER is to provide a library
of functionalities to model, solve and analyze planning problems in
practice.

TAMER can be used in two ways. As a standalone, command-line planner
to develop, debug and solve planning problems and as a library that
can be embedded in applications offering planning functionalities.


ANML and TAMER
--------------

TAMER internal formalism and representation is adherent to the
principles of the ANML (Action Notation Modeling Language) planning
language. ANML is the default and more comprehensive textual input
format for TAMER (but it is not the only one, also PDDL 2.1 is
supported). See [doc/ANML.md](doc/ANML.md) for a detailed
description of the supported ANML fragment and extensions.


Command-Line Usage
------------------

TAMER currently offers a very basic command-line functionality that is
described in [doc/CommandLine.md](doc/CommandLine.md).


Architecture and Basic Concepts
-------------------------------

The overall architecture and the basic modeling concepts are described
in [doc/Architecture.md](doc/Architecture.md).


API
---

TAMER offers a comprehensive API that allows to interact with the
system modeling framework and to the algorithms. From the API it is
possible to construct, parse and analyze planning problems, to
generate plans and to analyze them. The API is reentrant and allows
for multi-threading. An high-level description of the API is available
in [doc/API.md](doc/API.md), while a comprehensive documentation is
available in the documentation of [tamer.h](@ref tamer.h).


License
-------

The planner is copyrighted by the Fondazione Bruno Kessler.

TAMER is currently available under the following conditions:

* It can be used only for non-commercial or academic purposes.

* The source code in the distribution can be used only for reading,
  with no right of modification.

See the [LICENSE.txt](doc/LICENSE.md) file for a detailed description of
the licensing conditions.


Development
-----------

Some basic info about the development tools and processes is provided
in [doc/Development.md](doc/Development.md).
