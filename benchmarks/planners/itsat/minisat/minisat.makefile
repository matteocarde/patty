# Compiler flags...
CPP_COMPILER = g++
C_COMPILER = gcc

# Include paths...
#Debug_Include_Path=-I /media/software/code/TemporalSat
#Release_Include_Path=-I /media/software/code/TemporalSat
Debug_Include_Path=-I   ../
Release_Include_Path=-I  ../

# Library paths...
Debug_Library_Path=
Release_Library_Path=

# Additional libraries...
Debug_Libraries=
Release_Libraries=

# Preprocessor definitions...
Debug_Preprocessor_Definitions=-D GCC_BUILD -D _DEBUG -D _LIB 
Release_Preprocessor_Definitions=-D GCC_BUILD -D NDEBUG -D _LIB 

# Implictly linked object files...
Debug_Implicitly_Linked_Objects=
Release_Implicitly_Linked_Objects=

# Compiler flags...
Debug_Compiler_Flags=-O0 -g
Release_Compiler_Flags=-O2 

# Builds all configurations for this project...
.PHONY: build_all_configurations
build_all_configurations: Debug Release 

# Builds the Debug configuration...
.PHONY: Debug
Debug: create_folders gccDebug/core/Solver.o gccDebug/simp/SimpSolver.o gccDebug/utils/System.o 
	ar rcs ../gccDebug/libminisat.a gccDebug/core/Solver.o gccDebug/simp/SimpSolver.o gccDebug/utils/System.o  $(Debug_Implicitly_Linked_Objects)

# Compiles file core/Solver.cc for the Debug configuration...
-include gccDebug/core/Solver.d
gccDebug/core/Solver.o: core/Solver.cc
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -c core/Solver.cc $(Debug_Include_Path) -o gccDebug/core/Solver.o
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -MM core/Solver.cc $(Debug_Include_Path) > gccDebug/core/Solver.d

# Compiles file simp/SimpSolver.cc for the Debug configuration...
-include gccDebug/simp/SimpSolver.d
gccDebug/simp/SimpSolver.o: simp/SimpSolver.cc
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -c simp/SimpSolver.cc $(Debug_Include_Path) -o gccDebug/simp/SimpSolver.o
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -MM simp/SimpSolver.cc $(Debug_Include_Path) > gccDebug/simp/SimpSolver.d

# Compiles file utils/System.cc for the Debug configuration...
-include gccDebug/utils/System.d
gccDebug/utils/System.o: utils/System.cc
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -c utils/System.cc $(Debug_Include_Path) -o gccDebug/utils/System.o
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -MM utils/System.cc $(Debug_Include_Path) > gccDebug/utils/System.d

# Builds the Release configuration...
.PHONY: Release
Release: create_folders gccRelease/core/Solver.o gccRelease/simp/SimpSolver.o gccRelease/utils/System.o 
	ar rcs ../gccRelease/libminisat.a gccRelease/core/Solver.o gccRelease/simp/SimpSolver.o gccRelease/utils/System.o  $(Release_Implicitly_Linked_Objects)

# Compiles file core/Solver.cc for the Release configuration...
-include gccRelease/core/Solver.d
gccRelease/core/Solver.o: core/Solver.cc
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -c core/Solver.cc $(Release_Include_Path) -o gccRelease/core/Solver.o
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -MM core/Solver.cc $(Release_Include_Path) > gccRelease/core/Solver.d

# Compiles file simp/SimpSolver.cc for the Release configuration...
-include gccRelease/simp/SimpSolver.d
gccRelease/simp/SimpSolver.o: simp/SimpSolver.cc
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -c simp/SimpSolver.cc $(Release_Include_Path) -o gccRelease/simp/SimpSolver.o
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -MM simp/SimpSolver.cc $(Release_Include_Path) > gccRelease/simp/SimpSolver.d

# Compiles file utils/System.cc for the Release configuration...
-include gccRelease/utils/System.d
gccRelease/utils/System.o: utils/System.cc
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -c utils/System.cc $(Release_Include_Path) -o gccRelease/utils/System.o
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -MM utils/System.cc $(Release_Include_Path) > gccRelease/utils/System.d

# Creates the intermediate and output folders for each configuration...
.PHONY: create_folders
create_folders:
	mkdir -p ../gccDebug
	mkdir -p ../gccRelease
	mkdir -p gccDebug
	mkdir -p gccDebug/core
	mkdir -p gccDebug/simp
	mkdir -p gccDebug/utils
	mkdir -p gccRelease
	mkdir -p gccRelease/core
	mkdir -p gccRelease/simp
	mkdir -p gccRelease/utils

# Cleans intermediate and output files (objects, libraries, executables)...
.PHONY: clean
clean:
	rm -fr gccDebug
	rm -fr ../gccDebug
	rm -fr gccRelease
	rm -fr ../gccRelease

