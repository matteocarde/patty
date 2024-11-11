# LAMA Planner

This package serves as integration package and allows to use the LAMA planner either standalone or embedded in the [Robot Construction Kit](https://rock-robotics.org)

The original README is located [here](./README-original.md).
## Build & Installation

Parts of the planner are implemented in C++, and parts are implemented in Python. The C++ code was only tested under g++ and uses hash tables from the original STL which are part of the g++ libraries but not of the C++ standard. So if you want to make the planner run under a different C++ environment, you will need to adjust the parts of the planner that use these features.

To build and install LAMA, you can use the provided install script:

```shell
$ ./install.sh
```

By default, the resulting excutables and libraries are placed under `lama-planner/` folder. To change that, edit the installation script and change `INSTALL_DIR` variable.

## Running the Planner

LAMA runs in three separate phases: _translation_, _knowledge compilation_, and _search_. These are partitioned into three separate programs. The three directories `lama/translate`, `lama/preprocess` and
`lama/search` contain these programs.

To run the planner, you can simply use the Bash script `lama-planner`:

```shell
$ ./plan <domain_path> <problem_path> <result_path>
```

This script contains the settings used for LAMA during IPC-6. For other possible arguments modify the run script accordingly. The search component of the planner understands four options which can be combined in any way:

* `l`: Use the landmark heuristic.
* `L`: Use preferred operators of the landmark heuristic.
* `f`: Use the FF heuristic.
* `F`: Use helpful actions ("preferred operators" of the FF heuristic).

At least one heuristic (`l` or `f`) must be used; on average, using all features of the planner (`lLfF`) appears to produce the best results, which is therefore the default in the `lama-planner` script.

The planner can be told to run in iterated mode (keep searching for better solutions) using option `i`. Note that in this case, the planner may never stop (unless it can exhaust the search space) and needs to be aborted at some point.

By default, the first solution is found using best-first search, later search iterations use weighted A*. In order to use weighted A* for the first iteration as well, use option `w`.

Or, you can _run the three steps of LAMA separately_ (e.g., if you want to re-use output from earlier translation/pre-processing steps):

First, run:

```shell
$ /path/to/lama-planner/translate/translate.py domain.pddl problem.pddl
```

The translator will will write its result to a file called `output.sas`, which serves as an input to the next phase, knowledge compilation. The translator also writes a file called `test.groups`, which is some sort of translation key (see `sas-format.txt` in the documentation directory mentioned above). This second file is not needed by the planner, but might help you understand what the translated task looks like. It also writes a file called `all.groups` which is needed by the landmark heuristic.

Second, run:

```shell
$ /path/to/lama-planner/preprocess/preprocess < output.sas
```

This will run the knowledge compilation component, writing its output to the file aptly named `output`.

Finally, run:

```shell
$ /path/to/lama-planner/search/search <args>  < output
```

This runs the search component of the planner. On success, it will write a file called `sas_plan` containing the plan.

## Documentation

A comprehensive description of LAMA can be found in the JAIR article "[The LAMA Planner: Guiding Cost-Based Anytime Planning with Landmarks](doc/lama-jair10.pdf)" by Silvia Richter and Matthias Westphal (2010). A brief description of the planner is furthermore given in "[lama-short.pdf](doc/lama-short.pdf.

The AIJ article "[Concise finite-domain representations for PDDL  planning tasks](https://www.sciencedirect.com/science/article/pii/S0004370208001926)" by Malte Helmert (2009) describes the translation component in detail.  The description is somewhat idealized, as the actual implementation has some limitations in dealing with some ADL features. Still, the article provides a fairly good description of  what the translator does (or should do, at any rate).

File [sas-format.txt](doc/sas-format.txt) contains a description of the translator output format.  You will only need this if you want to use SAS+ tasks/multi-valued planning tasks within your own planner.

File [pre-format.txt](doc/pre-format.txt) contains a description of the output format of the knowledge compilation component (program `preprocess`). You will only need this if you want to use the preprocessed multi-valued planning task information within your own planner.

## LICENSE & CONTACT

LAMA was written by Silvia Richter and Matthias Westphal, copyright (c) 2008 NICTA and Matthias Westphal. Distributed under the GNU General Public License (GPL, see separate licence file).

This program uses source code of the Fast Downward planner, (c) 2003-2004 by Malte Helmert and Silvia Richter. Permission to redistribute this code under the terms of the GPL has been granted.

Note of Caution: Please be aware that LAMA has bugs. In particular the component responsible for  parsing and translating the PDDL input has known problems. However, for all classical (i.e. non-numerical, no preferences etc.) tasks from past international planning competitions, formulations exist that LAMA can parse. E.g.: for Airport, use the STRIPS formulation. For Freecell (IPC 2002), the untyped variant. For Philosophers, Optical Telegraph and PSR, use the ADL variant with derived predicates. For Mprime and Assembly, domain files are included in this distribution in the  "bench-patch" directory which correct known bugs of the competition files (Mprime) or features not supported by LAMA (Assembly).

If you encounter further problems, please email me at silvia.richter@nicta.com.au. The lama/translate directory also contains a patch that can be applied to skip the invariant generation step in the translator component. This eliminates many problems and may be helpful e.g. if you are interested in using the framework of LAMA with a heuristic other than the landmark heuristic.

Lastly, I would be happy to know if you are using LAMA. Just drop me a short email at the above address. Then I can also inform you about bug fixes and new versions.

### Questions and Feedback

Please feel free to e-mail us at silvia.richter@nicta.com.au if you have any questions, encounter bugs, or would like to discuss any issues regarding the planner.

Have fun,

Silvia Richter & Matthias Westphal