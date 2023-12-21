# Compiler flags...
CPP_COMPILER = g++
C_COMPILER = gcc

# Include paths...
Debug_Include_Path=-I   ../
Release_Include_Path=-I   ../

# Library paths...
Debug_Library_Path=-L  ../gccDebug
Release_Library_Path=-L   ../gccRelease

# Additional libraries...
Debug_Libraries= -lprecosat -lzchaff -lminisat
Release_Libraries= -lprecosat -lzchaff -lminisat

# Preprocessor definitions...
Debug_Preprocessor_Definitions=-D GCC_BUILD -D _DEBUG -D _CONSOLE 
Release_Preprocessor_Definitions=-D GCC_BUILD -D NDEBUG -D _CONSOLE 

# Implictly linked object files...
Debug_Implicitly_Linked_Objects=
Release_Implicitly_Linked_Objects=

# Compiler flags...
Debug_Compiler_Flags=-O0 -g 
Release_Compiler_Flags=-O2 

# Builds all configurations for this project...
.PHONY: build_all_configurations
build_all_configurations: Debug Release 

#### 32Bit x86 ==> Builds the Debug configuration...
.PHONY: Debug
Debug: create_folders gccDebug/main.o gccDebug/utils.o gccDebug/val/DebugWriteController.o gccDebug/val/pddl+.o gccDebug/val/ptree.o gccDebug/SatTimePrecosat.o gccDebug/sattime/SatTime.o gccDebug/sattime/SatTimeMinisat.o gccDebug/sattime/SatTimeZchaff.o gccDebug/satlayer/SatLayer.o gccDebug/satlayer/SatLayerMinisat.o gccDebug/satlayer/SatLayerPrecosat.o gccDebug/parser/ParserClasses.o gccDebug/graph/ETGraph.o gccDebug/graph/ITGraph.o gccDebug/alg2layer/Alg2Layer.o gccDebug/alg2layer/EventPlanOrders.o gccDebug/alg2layer/FindTimedPlan.o gccDebug/alg2layer/FSMSpecific.o gccDebug/alg2layer/FSM_General.o gccDebug/alg2layer/ITGraphUsage.o gccDebug/alg2layer/NegativeCycle.o gccDebug/alg2layer/PrintTimedPlan.o gccDebug/alg2layer/PruneTimedPlan.o gccDebug/alg1time/Alg1Time.o gccDebug/alg1time/ETGraphUsage.o 
	g++ gccDebug/main.o gccDebug/utils.o gccDebug/val/DebugWriteController.o gccDebug/val/pddl+.o gccDebug/val/ptree.o gccDebug/SatTimePrecosat.o gccDebug/sattime/SatTime.o gccDebug/sattime/SatTimeMinisat.o gccDebug/sattime/SatTimeZchaff.o gccDebug/satlayer/SatLayer.o gccDebug/satlayer/SatLayerMinisat.o gccDebug/satlayer/SatLayerPrecosat.o gccDebug/parser/ParserClasses.o gccDebug/graph/ETGraph.o gccDebug/graph/ITGraph.o gccDebug/alg2layer/Alg2Layer.o gccDebug/alg2layer/EventPlanOrders.o gccDebug/alg2layer/FindTimedPlan.o gccDebug/alg2layer/FSMSpecific.o gccDebug/alg2layer/FSM_General.o gccDebug/alg2layer/ITGraphUsage.o gccDebug/alg2layer/NegativeCycle.o gccDebug/alg2layer/PrintTimedPlan.o gccDebug/alg2layer/PruneTimedPlan.o gccDebug/alg1time/Alg1Time.o gccDebug/alg1time/ETGraphUsage.o  $(Debug_Library_Path) $(Debug_Libraries) -o ../gccDebug/tsat.exe

# Compiles file main.cpp for the Debug configuration...
-include gccDebug/main.d
gccDebug/main.o: main.cpp
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -c main.cpp $(Debug_Include_Path) -o gccDebug/main.o
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -MM main.cpp $(Debug_Include_Path) > gccDebug/main.d

# Compiles file utils.cpp for the Debug configuration...
-include gccDebug/utils.d
gccDebug/utils.o: utils.cpp
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -c utils.cpp $(Debug_Include_Path) -o gccDebug/utils.o
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -MM utils.cpp $(Debug_Include_Path) > gccDebug/utils.d

# Compiles file val/DebugWriteController.cpp for the Debug configuration...
-include gccDebug/val/DebugWriteController.d
gccDebug/val/DebugWriteController.o: val/DebugWriteController.cpp
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -c val/DebugWriteController.cpp $(Debug_Include_Path) -o gccDebug/val/DebugWriteController.o
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -MM val/DebugWriteController.cpp $(Debug_Include_Path) > gccDebug/val/DebugWriteController.d

# Compiles file val/pddl+.cpp for the Debug configuration...
-include gccDebug/val/pddl+.d
gccDebug/val/pddl+.o: val/pddl+.cpp
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -c val/pddl+.cpp $(Debug_Include_Path) -o gccDebug/val/pddl+.o
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -MM val/pddl+.cpp $(Debug_Include_Path) > gccDebug/val/pddl+.d

# Compiles file val/ptree.cpp for the Debug configuration...
-include gccDebug/val/ptree.d
gccDebug/val/ptree.o: val/ptree.cpp
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -c val/ptree.cpp $(Debug_Include_Path) -o gccDebug/val/ptree.o
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -MM val/ptree.cpp $(Debug_Include_Path) > gccDebug/val/ptree.d

# Compiles file SatTimePrecosat.cpp for the Debug configuration...
-include gccDebug/SatTimePrecosat.d
gccDebug/SatTimePrecosat.o: SatTimePrecosat.cpp
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -c SatTimePrecosat.cpp $(Debug_Include_Path) -o gccDebug/SatTimePrecosat.o
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -MM SatTimePrecosat.cpp $(Debug_Include_Path) > gccDebug/SatTimePrecosat.d

# Compiles file sattime/SatTime.cpp for the Debug configuration...
-include gccDebug/sattime/SatTime.d
gccDebug/sattime/SatTime.o: sattime/SatTime.cpp
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -c sattime/SatTime.cpp $(Debug_Include_Path) -o gccDebug/sattime/SatTime.o
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -MM sattime/SatTime.cpp $(Debug_Include_Path) > gccDebug/sattime/SatTime.d

# Compiles file sattime/SatTimeMinisat.cpp for the Debug configuration...
-include gccDebug/sattime/SatTimeMinisat.d
gccDebug/sattime/SatTimeMinisat.o: sattime/SatTimeMinisat.cpp
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -c sattime/SatTimeMinisat.cpp $(Debug_Include_Path) -o gccDebug/sattime/SatTimeMinisat.o
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -MM sattime/SatTimeMinisat.cpp $(Debug_Include_Path) > gccDebug/sattime/SatTimeMinisat.d

# Compiles file sattime/SatTimeZchaff.cpp for the Debug configuration...
-include gccDebug/sattime/SatTimeZchaff.d
gccDebug/sattime/SatTimeZchaff.o: sattime/SatTimeZchaff.cpp
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -c sattime/SatTimeZchaff.cpp $(Debug_Include_Path) -o gccDebug/sattime/SatTimeZchaff.o
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -MM sattime/SatTimeZchaff.cpp $(Debug_Include_Path) > gccDebug/sattime/SatTimeZchaff.d

# Compiles file satlayer/SatLayer.cpp for the Debug configuration...
-include gccDebug/satlayer/SatLayer.d
gccDebug/satlayer/SatLayer.o: satlayer/SatLayer.cpp
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -c satlayer/SatLayer.cpp $(Debug_Include_Path) -o gccDebug/satlayer/SatLayer.o
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -MM satlayer/SatLayer.cpp $(Debug_Include_Path) > gccDebug/satlayer/SatLayer.d

# Compiles file satlayer/SatLayerMinisat.cpp for the Debug configuration...
-include gccDebug/satlayer/SatLayerMinisat.d
gccDebug/satlayer/SatLayerMinisat.o: satlayer/SatLayerMinisat.cpp
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -c satlayer/SatLayerMinisat.cpp $(Debug_Include_Path) -o gccDebug/satlayer/SatLayerMinisat.o
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -MM satlayer/SatLayerMinisat.cpp $(Debug_Include_Path) > gccDebug/satlayer/SatLayerMinisat.d

# Compiles file satlayer/SatLayerPrecosat.cpp for the Debug configuration...
-include gccDebug/satlayer/SatLayerPrecosat.d
gccDebug/satlayer/SatLayerPrecosat.o: satlayer/SatLayerPrecosat.cpp
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -c satlayer/SatLayerPrecosat.cpp $(Debug_Include_Path) -o gccDebug/satlayer/SatLayerPrecosat.o
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -MM satlayer/SatLayerPrecosat.cpp $(Debug_Include_Path) > gccDebug/satlayer/SatLayerPrecosat.d

# Compiles file parser/ParserClasses.cpp for the Debug configuration...
-include gccDebug/parser/ParserClasses.d
gccDebug/parser/ParserClasses.o: parser/ParserClasses.cpp
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -c parser/ParserClasses.cpp $(Debug_Include_Path) -o gccDebug/parser/ParserClasses.o
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -MM parser/ParserClasses.cpp $(Debug_Include_Path) > gccDebug/parser/ParserClasses.d

# Compiles file graph/ETGraph.cpp for the Debug configuration...
-include gccDebug/graph/ETGraph.d
gccDebug/graph/ETGraph.o: graph/ETGraph.cpp
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -c graph/ETGraph.cpp $(Debug_Include_Path) -o gccDebug/graph/ETGraph.o
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -MM graph/ETGraph.cpp $(Debug_Include_Path) > gccDebug/graph/ETGraph.d

# Compiles file graph/ITGraph.cpp for the Debug configuration...
-include gccDebug/graph/ITGraph.d
gccDebug/graph/ITGraph.o: graph/ITGraph.cpp
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -c graph/ITGraph.cpp $(Debug_Include_Path) -o gccDebug/graph/ITGraph.o
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -MM graph/ITGraph.cpp $(Debug_Include_Path) > gccDebug/graph/ITGraph.d

# Compiles file alg2layer/Alg2Layer.cpp for the Debug configuration...
-include gccDebug/alg2layer/Alg2Layer.d
gccDebug/alg2layer/Alg2Layer.o: alg2layer/Alg2Layer.cpp
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -c alg2layer/Alg2Layer.cpp $(Debug_Include_Path) -o gccDebug/alg2layer/Alg2Layer.o
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -MM alg2layer/Alg2Layer.cpp $(Debug_Include_Path) > gccDebug/alg2layer/Alg2Layer.d

# Compiles file alg2layer/EventPlanOrders.cpp for the Debug configuration...
-include gccDebug/alg2layer/EventPlanOrders.d
gccDebug/alg2layer/EventPlanOrders.o: alg2layer/EventPlanOrders.cpp
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -c alg2layer/EventPlanOrders.cpp $(Debug_Include_Path) -o gccDebug/alg2layer/EventPlanOrders.o
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -MM alg2layer/EventPlanOrders.cpp $(Debug_Include_Path) > gccDebug/alg2layer/EventPlanOrders.d

# Compiles file alg2layer/FindTimedPlan.cpp for the Debug configuration...
-include gccDebug/alg2layer/FindTimedPlan.d
gccDebug/alg2layer/FindTimedPlan.o: alg2layer/FindTimedPlan.cpp
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -c alg2layer/FindTimedPlan.cpp $(Debug_Include_Path) -o gccDebug/alg2layer/FindTimedPlan.o
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -MM alg2layer/FindTimedPlan.cpp $(Debug_Include_Path) > gccDebug/alg2layer/FindTimedPlan.d

# Compiles file alg2layer/FSMSpecific.cpp for the Debug configuration...
-include gccDebug/alg2layer/FSMSpecific.d
gccDebug/alg2layer/FSMSpecific.o: alg2layer/FSMSpecific.cpp
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -c alg2layer/FSMSpecific.cpp $(Debug_Include_Path) -o gccDebug/alg2layer/FSMSpecific.o
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -MM alg2layer/FSMSpecific.cpp $(Debug_Include_Path) > gccDebug/alg2layer/FSMSpecific.d

# Compiles file alg2layer/FSM_General.cpp for the Debug configuration...
-include gccDebug/alg2layer/FSM_General.d
gccDebug/alg2layer/FSM_General.o: alg2layer/FSM_General.cpp
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -c alg2layer/FSM_General.cpp $(Debug_Include_Path) -o gccDebug/alg2layer/FSM_General.o
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -MM alg2layer/FSM_General.cpp $(Debug_Include_Path) > gccDebug/alg2layer/FSM_General.d

# Compiles file alg2layer/ITGraphUsage.cpp for the Debug configuration...
-include gccDebug/alg2layer/ITGraphUsage.d
gccDebug/alg2layer/ITGraphUsage.o: alg2layer/ITGraphUsage.cpp
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -c alg2layer/ITGraphUsage.cpp $(Debug_Include_Path) -o gccDebug/alg2layer/ITGraphUsage.o
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -MM alg2layer/ITGraphUsage.cpp $(Debug_Include_Path) > gccDebug/alg2layer/ITGraphUsage.d

# Compiles file alg2layer/NegativeCycle.cpp for the Debug configuration...
-include gccDebug/alg2layer/NegativeCycle.d
gccDebug/alg2layer/NegativeCycle.o: alg2layer/NegativeCycle.cpp
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -c alg2layer/NegativeCycle.cpp $(Debug_Include_Path) -o gccDebug/alg2layer/NegativeCycle.o
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -MM alg2layer/NegativeCycle.cpp $(Debug_Include_Path) > gccDebug/alg2layer/NegativeCycle.d

# Compiles file alg2layer/PrintTimedPlan.cpp for the Debug configuration...
-include gccDebug/alg2layer/PrintTimedPlan.d
gccDebug/alg2layer/PrintTimedPlan.o: alg2layer/PrintTimedPlan.cpp
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -c alg2layer/PrintTimedPlan.cpp $(Debug_Include_Path) -o gccDebug/alg2layer/PrintTimedPlan.o
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -MM alg2layer/PrintTimedPlan.cpp $(Debug_Include_Path) > gccDebug/alg2layer/PrintTimedPlan.d

# Compiles file alg2layer/PruneTimedPlan.cpp for the Debug configuration...
-include gccDebug/alg2layer/PruneTimedPlan.d
gccDebug/alg2layer/PruneTimedPlan.o: alg2layer/PruneTimedPlan.cpp
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -c alg2layer/PruneTimedPlan.cpp $(Debug_Include_Path) -o gccDebug/alg2layer/PruneTimedPlan.o
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -MM alg2layer/PruneTimedPlan.cpp $(Debug_Include_Path) > gccDebug/alg2layer/PruneTimedPlan.d

# Compiles file alg1time/Alg1Time.cpp for the Debug configuration...
-include gccDebug/alg1time/Alg1Time.d
gccDebug/alg1time/Alg1Time.o: alg1time/Alg1Time.cpp
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -c alg1time/Alg1Time.cpp $(Debug_Include_Path) -o gccDebug/alg1time/Alg1Time.o
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -MM alg1time/Alg1Time.cpp $(Debug_Include_Path) > gccDebug/alg1time/Alg1Time.d

# Compiles file alg1time/ETGraphUsage.cpp for the Debug configuration...
-include gccDebug/alg1time/ETGraphUsage.d
gccDebug/alg1time/ETGraphUsage.o: alg1time/ETGraphUsage.cpp
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -c alg1time/ETGraphUsage.cpp $(Debug_Include_Path) -o gccDebug/alg1time/ETGraphUsage.o
	$(CPP_COMPILER) $(Debug_Preprocessor_Definitions) $(Debug_Compiler_Flags) -MM alg1time/ETGraphUsage.cpp $(Debug_Include_Path) > gccDebug/alg1time/ETGraphUsage.d


###### 32Bit x86 ==> Builds the Release configuration...
.PHONY: Release
Release: create_folders gccRelease/main.o gccRelease/utils.o gccRelease/val/DebugWriteController.o gccRelease/val/pddl+.o gccRelease/val/ptree.o gccRelease/SatTimePrecosat.o gccRelease/sattime/SatTime.o gccRelease/sattime/SatTimeMinisat.o gccRelease/sattime/SatTimeZchaff.o gccRelease/satlayer/SatLayer.o gccRelease/satlayer/SatLayerMinisat.o gccRelease/satlayer/SatLayerPrecosat.o gccRelease/parser/ParserClasses.o gccRelease/graph/ETGraph.o gccRelease/graph/ITGraph.o gccRelease/alg2layer/Alg2Layer.o gccRelease/alg2layer/EventPlanOrders.o gccRelease/alg2layer/FindTimedPlan.o gccRelease/alg2layer/FSMSpecific.o gccRelease/alg2layer/FSM_General.o gccRelease/alg2layer/ITGraphUsage.o gccRelease/alg2layer/NegativeCycle.o gccRelease/alg2layer/PrintTimedPlan.o gccRelease/alg2layer/PruneTimedPlan.o gccRelease/alg1time/Alg1Time.o gccRelease/alg1time/ETGraphUsage.o 
	g++ gccRelease/main.o gccRelease/utils.o gccRelease/val/DebugWriteController.o gccRelease/val/pddl+.o gccRelease/val/ptree.o gccRelease/SatTimePrecosat.o gccRelease/sattime/SatTime.o gccRelease/sattime/SatTimeMinisat.o gccRelease/sattime/SatTimeZchaff.o gccRelease/satlayer/SatLayer.o gccRelease/satlayer/SatLayerMinisat.o gccRelease/satlayer/SatLayerPrecosat.o gccRelease/parser/ParserClasses.o gccRelease/graph/ETGraph.o gccRelease/graph/ITGraph.o gccRelease/alg2layer/Alg2Layer.o gccRelease/alg2layer/EventPlanOrders.o gccRelease/alg2layer/FindTimedPlan.o gccRelease/alg2layer/FSMSpecific.o gccRelease/alg2layer/FSM_General.o gccRelease/alg2layer/ITGraphUsage.o gccRelease/alg2layer/NegativeCycle.o gccRelease/alg2layer/PrintTimedPlan.o gccRelease/alg2layer/PruneTimedPlan.o gccRelease/alg1time/Alg1Time.o gccRelease/alg1time/ETGraphUsage.o  $(Release_Library_Path) $(Release_Libraries) -Wl,-rpath,./ -o ../gccRelease/tsat.exe

# Compiles file main.cpp for the Release configuration...
-include gccRelease/main.d
gccRelease/main.o: main.cpp
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -c main.cpp $(Release_Include_Path) -o gccRelease/main.o
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -MM main.cpp $(Release_Include_Path) > gccRelease/main.d

# Compiles file utils.cpp for the Release configuration...
-include gccRelease/utils.d
gccRelease/utils.o: utils.cpp
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -c utils.cpp $(Release_Include_Path) -o gccRelease/utils.o
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -MM utils.cpp $(Release_Include_Path) > gccRelease/utils.d

# Compiles file val/DebugWriteController.cpp for the Release configuration...
-include gccRelease/val/DebugWriteController.d
gccRelease/val/DebugWriteController.o: val/DebugWriteController.cpp
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -c val/DebugWriteController.cpp $(Release_Include_Path) -o gccRelease/val/DebugWriteController.o
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -MM val/DebugWriteController.cpp $(Release_Include_Path) > gccRelease/val/DebugWriteController.d

# Compiles file val/pddl+.cpp for the Release configuration...
-include gccRelease/val/pddl+.d
gccRelease/val/pddl+.o: val/pddl+.cpp
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -c val/pddl+.cpp $(Release_Include_Path) -o gccRelease/val/pddl+.o
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -MM val/pddl+.cpp $(Release_Include_Path) > gccRelease/val/pddl+.d

# Compiles file val/ptree.cpp for the Release configuration...
-include gccRelease/val/ptree.d
gccRelease/val/ptree.o: val/ptree.cpp
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -c val/ptree.cpp $(Release_Include_Path) -o gccRelease/val/ptree.o
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -MM val/ptree.cpp $(Release_Include_Path) > gccRelease/val/ptree.d

# Compiles file SatTimePrecosat.cpp for the Release configuration...
-include gccRelease/SatTimePrecosat.d
gccRelease/SatTimePrecosat.o: SatTimePrecosat.cpp
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -c SatTimePrecosat.cpp $(Release_Include_Path) -o gccRelease/SatTimePrecosat.o
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -MM SatTimePrecosat.cpp $(Release_Include_Path) > gccRelease/SatTimePrecosat.d

# Compiles file sattime/SatTime.cpp for the Release configuration...
-include gccRelease/sattime/SatTime.d
gccRelease/sattime/SatTime.o: sattime/SatTime.cpp
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -c sattime/SatTime.cpp $(Release_Include_Path) -o gccRelease/sattime/SatTime.o
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -MM sattime/SatTime.cpp $(Release_Include_Path) > gccRelease/sattime/SatTime.d

# Compiles file sattime/SatTimeMinisat.cpp for the Release configuration...
-include gccRelease/sattime/SatTimeMinisat.d
gccRelease/sattime/SatTimeMinisat.o: sattime/SatTimeMinisat.cpp
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -c sattime/SatTimeMinisat.cpp $(Release_Include_Path) -o gccRelease/sattime/SatTimeMinisat.o
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -MM sattime/SatTimeMinisat.cpp $(Release_Include_Path) > gccRelease/sattime/SatTimeMinisat.d

# Compiles file sattime/SatTimeZchaff.cpp for the Release configuration...
-include gccRelease/sattime/SatTimeZchaff.d
gccRelease/sattime/SatTimeZchaff.o: sattime/SatTimeZchaff.cpp
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -c sattime/SatTimeZchaff.cpp $(Release_Include_Path) -o gccRelease/sattime/SatTimeZchaff.o
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -MM sattime/SatTimeZchaff.cpp $(Release_Include_Path) > gccRelease/sattime/SatTimeZchaff.d

# Compiles file satlayer/SatLayer.cpp for the Release configuration...
-include gccRelease/satlayer/SatLayer.d
gccRelease/satlayer/SatLayer.o: satlayer/SatLayer.cpp
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -c satlayer/SatLayer.cpp $(Release_Include_Path) -o gccRelease/satlayer/SatLayer.o
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -MM satlayer/SatLayer.cpp $(Release_Include_Path) > gccRelease/satlayer/SatLayer.d

# Compiles file satlayer/SatLayerMinisat.cpp for the Release configuration...
-include gccRelease/satlayer/SatLayerMinisat.d
gccRelease/satlayer/SatLayerMinisat.o: satlayer/SatLayerMinisat.cpp
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -c satlayer/SatLayerMinisat.cpp $(Release_Include_Path) -o gccRelease/satlayer/SatLayerMinisat.o
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -MM satlayer/SatLayerMinisat.cpp $(Release_Include_Path) > gccRelease/satlayer/SatLayerMinisat.d

# Compiles file satlayer/SatLayerPrecosat.cpp for the Release configuration...
-include gccRelease/satlayer/SatLayerPrecosat.d
gccRelease/satlayer/SatLayerPrecosat.o: satlayer/SatLayerPrecosat.cpp
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -c satlayer/SatLayerPrecosat.cpp $(Release_Include_Path) -o gccRelease/satlayer/SatLayerPrecosat.o
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -MM satlayer/SatLayerPrecosat.cpp $(Release_Include_Path) > gccRelease/satlayer/SatLayerPrecosat.d

# Compiles file parser/ParserClasses.cpp for the Release configuration...
-include gccRelease/parser/ParserClasses.d
gccRelease/parser/ParserClasses.o: parser/ParserClasses.cpp
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -c parser/ParserClasses.cpp $(Release_Include_Path) -o gccRelease/parser/ParserClasses.o
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -MM parser/ParserClasses.cpp $(Release_Include_Path) > gccRelease/parser/ParserClasses.d

# Compiles file graph/ETGraph.cpp for the Release configuration...
-include gccRelease/graph/ETGraph.d
gccRelease/graph/ETGraph.o: graph/ETGraph.cpp
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -c graph/ETGraph.cpp $(Release_Include_Path) -o gccRelease/graph/ETGraph.o
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -MM graph/ETGraph.cpp $(Release_Include_Path) > gccRelease/graph/ETGraph.d

# Compiles file graph/ITGraph.cpp for the Release configuration...
-include gccRelease/graph/ITGraph.d
gccRelease/graph/ITGraph.o: graph/ITGraph.cpp
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -c graph/ITGraph.cpp $(Release_Include_Path) -o gccRelease/graph/ITGraph.o
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -MM graph/ITGraph.cpp $(Release_Include_Path) > gccRelease/graph/ITGraph.d

# Compiles file alg2layer/Alg2Layer.cpp for the Release configuration...
-include gccRelease/alg2layer/Alg2Layer.d
gccRelease/alg2layer/Alg2Layer.o: alg2layer/Alg2Layer.cpp
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -c alg2layer/Alg2Layer.cpp $(Release_Include_Path) -o gccRelease/alg2layer/Alg2Layer.o
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -MM alg2layer/Alg2Layer.cpp $(Release_Include_Path) > gccRelease/alg2layer/Alg2Layer.d

# Compiles file alg2layer/EventPlanOrders.cpp for the Release configuration...
-include gccRelease/alg2layer/EventPlanOrders.d
gccRelease/alg2layer/EventPlanOrders.o: alg2layer/EventPlanOrders.cpp
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -c alg2layer/EventPlanOrders.cpp $(Release_Include_Path) -o gccRelease/alg2layer/EventPlanOrders.o
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -MM alg2layer/EventPlanOrders.cpp $(Release_Include_Path) > gccRelease/alg2layer/EventPlanOrders.d

# Compiles file alg2layer/FindTimedPlan.cpp for the Release configuration...
-include gccRelease/alg2layer/FindTimedPlan.d
gccRelease/alg2layer/FindTimedPlan.o: alg2layer/FindTimedPlan.cpp
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -c alg2layer/FindTimedPlan.cpp $(Release_Include_Path) -o gccRelease/alg2layer/FindTimedPlan.o
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -MM alg2layer/FindTimedPlan.cpp $(Release_Include_Path) > gccRelease/alg2layer/FindTimedPlan.d

# Compiles file alg2layer/FSMSpecific.cpp for the Release configuration...
-include gccRelease/alg2layer/FSMSpecific.d
gccRelease/alg2layer/FSMSpecific.o: alg2layer/FSMSpecific.cpp
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -c alg2layer/FSMSpecific.cpp $(Release_Include_Path) -o gccRelease/alg2layer/FSMSpecific.o
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -MM alg2layer/FSMSpecific.cpp $(Release_Include_Path) > gccRelease/alg2layer/FSMSpecific.d

# Compiles file alg2layer/FSM_General.cpp for the Release configuration...
-include gccRelease/alg2layer/FSM_General.d
gccRelease/alg2layer/FSM_General.o: alg2layer/FSM_General.cpp
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -c alg2layer/FSM_General.cpp $(Release_Include_Path) -o gccRelease/alg2layer/FSM_General.o
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -MM alg2layer/FSM_General.cpp $(Release_Include_Path) > gccRelease/alg2layer/FSM_General.d

# Compiles file alg2layer/ITGraphUsage.cpp for the Release configuration...
-include gccRelease/alg2layer/ITGraphUsage.d
gccRelease/alg2layer/ITGraphUsage.o: alg2layer/ITGraphUsage.cpp
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -c alg2layer/ITGraphUsage.cpp $(Release_Include_Path) -o gccRelease/alg2layer/ITGraphUsage.o
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -MM alg2layer/ITGraphUsage.cpp $(Release_Include_Path) > gccRelease/alg2layer/ITGraphUsage.d

# Compiles file alg2layer/NegativeCycle.cpp for the Release configuration...
-include gccRelease/alg2layer/NegativeCycle.d
gccRelease/alg2layer/NegativeCycle.o: alg2layer/NegativeCycle.cpp
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -c alg2layer/NegativeCycle.cpp $(Release_Include_Path) -o gccRelease/alg2layer/NegativeCycle.o
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -MM alg2layer/NegativeCycle.cpp $(Release_Include_Path) > gccRelease/alg2layer/NegativeCycle.d

# Compiles file alg2layer/PrintTimedPlan.cpp for the Release configuration...
-include gccRelease/alg2layer/PrintTimedPlan.d
gccRelease/alg2layer/PrintTimedPlan.o: alg2layer/PrintTimedPlan.cpp
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -c alg2layer/PrintTimedPlan.cpp $(Release_Include_Path) -o gccRelease/alg2layer/PrintTimedPlan.o
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -MM alg2layer/PrintTimedPlan.cpp $(Release_Include_Path) > gccRelease/alg2layer/PrintTimedPlan.d

# Compiles file alg2layer/PruneTimedPlan.cpp for the Release configuration...
-include gccRelease/alg2layer/PruneTimedPlan.d
gccRelease/alg2layer/PruneTimedPlan.o: alg2layer/PruneTimedPlan.cpp
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -c alg2layer/PruneTimedPlan.cpp $(Release_Include_Path) -o gccRelease/alg2layer/PruneTimedPlan.o
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -MM alg2layer/PruneTimedPlan.cpp $(Release_Include_Path) > gccRelease/alg2layer/PruneTimedPlan.d

# Compiles file alg1time/Alg1Time.cpp for the Release configuration...
-include gccRelease/alg1time/Alg1Time.d
gccRelease/alg1time/Alg1Time.o: alg1time/Alg1Time.cpp
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -c alg1time/Alg1Time.cpp $(Release_Include_Path) -o gccRelease/alg1time/Alg1Time.o
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -MM alg1time/Alg1Time.cpp $(Release_Include_Path) > gccRelease/alg1time/Alg1Time.d

# Compiles file alg1time/ETGraphUsage.cpp for the Release configuration...
-include gccRelease/alg1time/ETGraphUsage.d
gccRelease/alg1time/ETGraphUsage.o: alg1time/ETGraphUsage.cpp
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -c alg1time/ETGraphUsage.cpp $(Release_Include_Path) -o gccRelease/alg1time/ETGraphUsage.o
	$(CPP_COMPILER) $(Release_Preprocessor_Definitions) $(Release_Compiler_Flags) -MM alg1time/ETGraphUsage.cpp $(Release_Include_Path) > gccRelease/alg1time/ETGraphUsage.d

# Creates the intermediate and output folders for each configuration...
.PHONY: create_folders
create_folders:
	mkdir -p ../gccDebug
	mkdir -p ../gccRelease
	mkdir -p gccDebug
	mkdir -p gccDebug/alg1time
	mkdir -p gccDebug/alg2layer
	mkdir -p gccDebug/graph
	mkdir -p gccDebug/parser
	mkdir -p gccDebug/satlayer
	mkdir -p gccDebug/sattime
	mkdir -p gccDebug/val
	mkdir -p gccRelease
	mkdir -p gccRelease/alg1time
	mkdir -p gccRelease/alg2layer
	mkdir -p gccRelease/graph
	mkdir -p gccRelease/parser
	mkdir -p gccRelease/satlayer
	mkdir -p gccRelease/sattime
	mkdir -p gccRelease/val

# Cleans intermediate and output files (objects, libraries, executables)...
.PHONY: clean
clean:
	rm -fr gccDebug
	rm -fr ../gccDebug
	rm -fr gccRelease
	rm -fr ../gccRelease

