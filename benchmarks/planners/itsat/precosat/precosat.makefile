# Compiler flags...
CPP_COMPILER = g++
C_COMPILER = gcc

# Include paths...
#Debug_Include_Path=-I /cygdrive/c/Users/Ali/Desktop/TemporalSat
#Release_Include_Path=-I /cygdrive/c/Users/Ali/Desktop/TemporalSat
Debug_Include_Path=-I  /home/ali/Desktop/IPC/temp-sat-itsat
Release_Include_Path=-I   /home/ali/Desktop/IPC/temp-sat-itsat

# Library paths...
Debug_Library_Path=
Release_Library_Path=

# Additional libraries...
Debug_Libraries=
Release_Libraries=

# Preprocessor definitions...
Debug_Preprocessor_Definitions=-D GCC_BUILD -D _DEBUG -D NLOGPRECO -D NSTATSPRECO -D _LIB 
Release_Preprocessor_Definitions=-D GCC_BUILD -D NDEBUG -D NLOGPRECO -D NSTATSPRECO -D _LIB 

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
Debug: create_folders gccDebug/precosat.o 
	ar rcs ../gccDebug/libprecosat.a gccDebug/precosat.o  $(Debug_Implicitly_Linked_Objects)

# Compiles file precosat.cc for the Debug configuration...
-include gccDebug/precosat.d
gccDebug/precosat.o: precosat.cc
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -c precosat.cc $(Debug_Include_Path) -o gccDebug/precosat.o
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -MM precosat.cc $(Debug_Include_Path) > gccDebug/precosat.d

# Builds the Release configuration...
.PHONY: Release
Release: create_folders gccRelease/precosat.o 
	ar rcs ../gccRelease/libprecosat.a gccRelease/precosat.o  $(Release_Implicitly_Linked_Objects)

# Compiles file precosat.cc for the Release configuration...
-include gccRelease/precosat.d
gccRelease/precosat.o: precosat.cc
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -c precosat.cc $(Release_Include_Path) -o gccRelease/precosat.o
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -MM precosat.cc $(Release_Include_Path) > gccRelease/precosat.d

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

