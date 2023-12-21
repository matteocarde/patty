# Compiler flags...
CPP_COMPILER = g++
C_COMPILER = gcc

# Include paths...
#Debug_Include_Path=-I /media/software/code/TemporalSat
#Release_Include_Path=-I /media/software/code/TemporalSat
Debug_Include_Path=-I  ../
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
Debug: create_folders gccDebug/zchaff_base.o gccDebug/zchaff_cpp_wrapper.o gccDebug/zchaff_dbase.o gccDebug/zchaff_solver.o gccDebug/zchaff_utils.o 
	ar rcs ../gccDebug/libzchaff.a gccDebug/zchaff_base.o gccDebug/zchaff_cpp_wrapper.o gccDebug/zchaff_dbase.o gccDebug/zchaff_solver.o gccDebug/zchaff_utils.o  $(Debug_Implicitly_Linked_Objects)

# Compiles file zchaff_base.cpp for the Debug configuration...
-include gccDebug/zchaff_base.d
gccDebug/zchaff_base.o: zchaff_base.cpp
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -c zchaff_base.cpp $(Debug_Include_Path) -o gccDebug/zchaff_base.o
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -MM zchaff_base.cpp $(Debug_Include_Path) > gccDebug/zchaff_base.d

# Compiles file zchaff_cpp_wrapper.cpp for the Debug configuration...
-include gccDebug/zchaff_cpp_wrapper.d
gccDebug/zchaff_cpp_wrapper.o: zchaff_cpp_wrapper.cpp
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -c zchaff_cpp_wrapper.cpp $(Debug_Include_Path) -o gccDebug/zchaff_cpp_wrapper.o
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -MM zchaff_cpp_wrapper.cpp $(Debug_Include_Path) > gccDebug/zchaff_cpp_wrapper.d

# Compiles file zchaff_dbase.cpp for the Debug configuration...
-include gccDebug/zchaff_dbase.d
gccDebug/zchaff_dbase.o: zchaff_dbase.cpp
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -c zchaff_dbase.cpp $(Debug_Include_Path) -o gccDebug/zchaff_dbase.o
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -MM zchaff_dbase.cpp $(Debug_Include_Path) > gccDebug/zchaff_dbase.d

# Compiles file zchaff_solver.cpp for the Debug configuration...
-include gccDebug/zchaff_solver.d
gccDebug/zchaff_solver.o: zchaff_solver.cpp
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -c zchaff_solver.cpp $(Debug_Include_Path) -o gccDebug/zchaff_solver.o
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -MM zchaff_solver.cpp $(Debug_Include_Path) > gccDebug/zchaff_solver.d

# Compiles file zchaff_utils.cpp for the Debug configuration...
-include gccDebug/zchaff_utils.d
gccDebug/zchaff_utils.o: zchaff_utils.cpp
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -c zchaff_utils.cpp $(Debug_Include_Path) -o gccDebug/zchaff_utils.o
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -MM zchaff_utils.cpp $(Debug_Include_Path) > gccDebug/zchaff_utils.d

# Builds the Release configuration...
.PHONY: Release
Release: create_folders gccRelease/zchaff_base.o gccRelease/zchaff_cpp_wrapper.o gccRelease/zchaff_dbase.o gccRelease/zchaff_solver.o gccRelease/zchaff_utils.o 
	ar rcs ../gccRelease/libzchaff.a gccRelease/zchaff_base.o gccRelease/zchaff_cpp_wrapper.o gccRelease/zchaff_dbase.o gccRelease/zchaff_solver.o gccRelease/zchaff_utils.o  $(Release_Implicitly_Linked_Objects)

# Compiles file zchaff_base.cpp for the Release configuration...
-include gccRelease/zchaff_base.d
gccRelease/zchaff_base.o: zchaff_base.cpp
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -c zchaff_base.cpp $(Release_Include_Path) -o gccRelease/zchaff_base.o
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -MM zchaff_base.cpp $(Release_Include_Path) > gccRelease/zchaff_base.d

# Compiles file zchaff_cpp_wrapper.cpp for the Release configuration...
-include gccRelease/zchaff_cpp_wrapper.d
gccRelease/zchaff_cpp_wrapper.o: zchaff_cpp_wrapper.cpp
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -c zchaff_cpp_wrapper.cpp $(Release_Include_Path) -o gccRelease/zchaff_cpp_wrapper.o
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -MM zchaff_cpp_wrapper.cpp $(Release_Include_Path) > gccRelease/zchaff_cpp_wrapper.d

# Compiles file zchaff_dbase.cpp for the Release configuration...
-include gccRelease/zchaff_dbase.d
gccRelease/zchaff_dbase.o: zchaff_dbase.cpp
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -c zchaff_dbase.cpp $(Release_Include_Path) -o gccRelease/zchaff_dbase.o
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -MM zchaff_dbase.cpp $(Release_Include_Path) > gccRelease/zchaff_dbase.d

# Compiles file zchaff_solver.cpp for the Release configuration...
-include gccRelease/zchaff_solver.d
gccRelease/zchaff_solver.o: zchaff_solver.cpp
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -c zchaff_solver.cpp $(Release_Include_Path) -o gccRelease/zchaff_solver.o
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -MM zchaff_solver.cpp $(Release_Include_Path) > gccRelease/zchaff_solver.d

# Compiles file zchaff_utils.cpp for the Release configuration...
-include gccRelease/zchaff_utils.d
gccRelease/zchaff_utils.o: zchaff_utils.cpp
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -c zchaff_utils.cpp $(Release_Include_Path) -o gccRelease/zchaff_utils.o
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -MM zchaff_utils.cpp $(Release_Include_Path) > gccRelease/zchaff_utils.d

# Creates the intermediate and output folders for each configuration...
.PHONY: create_folders
create_folders:
	mkdir -p gccDebug
	mkdir -p ../gccDebug
	mkdir -p gccRelease
	mkdir -p ../gccRelease

# Cleans intermediate and output files (objects, libraries, executables)...
.PHONY: clean
clean:
	rm -fr gccDebug
	rm -fr ../gccDebug
	rm -fr gccRelease
	rm -fr ../gccRelease

