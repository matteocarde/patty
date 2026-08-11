# 2012 (C) Jussi Rintanen, jrintanen.jr@gmail.com

# --------------------------------------------------------------------
# Planner variant
# --------------------------------------------------------------------

# Madagascar with the planning heuristic as default (Mp)
VERSION = -DMPDOWNLOAD
EXECUTABLE = madagascar

# Madagascar C with the planning heuristic as default (MpC)
# VERSION = -DCMPDOWNLOAD
# EXECUTABLE = MpC

# Madagascar with VSIDS as default (M)
# VERSION = -DVSIDS
# EXECUTABLE = M


# --------------------------------------------------------------------
# Toolchain
# --------------------------------------------------------------------

# On macOS, "gcc" is usually Apple Clang.
CC = clang

PARSERGENERATOR = bison
LEXERGENERATOR = flex

PARSERC = parser.tab.c
PARSERH = parser.tab.h
PARSER = parser


# --------------------------------------------------------------------
# Target architecture
# --------------------------------------------------------------------

# Madagascar uses x86 SSE intrinsics, so build an x86_64 binary and run
# it through Rosetta on Apple Silicon.
ARCHFLAGS = -arch x86_64


# --------------------------------------------------------------------
# Configuration
# --------------------------------------------------------------------

CONFIGURATION = \
	-DLBD \
	-DREPRTHREE \
	-DWEIGHTS

# Optional features:
# CONFIGURATION += -DFUIP
# CONFIGURATION += -DMULTICORE
# CONFIGURATION += -DSPREAD
# CONFIGURATION += -DCOSTS
# CONFIGURATION += -DCFMA
# CONFIGURATION += -DCP3

# OpenMP is disabled by default.
# FEATURES = -fopenmp
# LINKFEATURES = -fopenmp


# --------------------------------------------------------------------
# Compiler and linker flags
# --------------------------------------------------------------------

# The source relies on several pre-C99 behaviours.
CSTANDARD = -std=gnu89

# Conservative optimization settings supported by Apple Clang.
OPTIMIZATION = -O3 -funroll-loops

# Keep debugging symbols, but disable old gprof instrumentation.
DEBUGFLAGS = -g

# -w disables warnings. Keep it temporarily because this is legacy code.
# Remove -w later if you want to clean up all warnings.
WARNINGFLAGS = -w -Wno-error=int-conversion -Wno-error=incompatible-function-pointer-types

CFLAGS = \
	$(ARCHFLAGS) \
	$(VERSION) \
	$(FEATURES) \
	$(CONFIGURATION) \
	$(CSTANDARD) \
	$(OPTIMIZATION) \
	$(DEBUGFLAGS) \
	$(WARNINGFLAGS) 

# macOS does not support the Linux-style fully static linking expected by
# the original Makefile, so do not use -static.
LDFLAGS = $(ARCHFLAGS)

LDLIBS = -lm


# --------------------------------------------------------------------
# Sources
# --------------------------------------------------------------------

OBJ = \
	$(PARSER).tab.o \
	main.o \
	asyntax.o \
	lex.yy.o \
	tables.o \
	operators.o \
	invariants.o \
	intsets.o \
	cleanup.o \
	translate2sat.o \
	scc.o \
	clausesets.o \
	printplan.o \
	clausedb.o \
	dimacsinput.o \
	ground.o

HDR = \
	main.h \
	asyntax.h \
	tables.h \
	operators.h \
	invariants.h \
	intsets.h \
	cleanup.h \
	scc.h \
	translate2sat.h \
	ordintsets.h \
	clausedb.h \
	interface.h \
	printplan.h \
	dimacsinput.h


# --------------------------------------------------------------------
# Targets
# --------------------------------------------------------------------

.PHONY: all clean tar date

all: $(EXECUTABLE)

$(EXECUTABLE): date lex.yy.c $(PARSERC) $(OBJ)
	$(CC) $(LDFLAGS) $(LINKFEATURES) $(OBJ) $(LDLIBS) -o $@

clausesets.o: heuristics2.c varvals.c learn2.c
ground.o: Cground.c
main.o: zPRINTDATE

%.o: %.c Makefile $(HDR)
	$(CC) $(CFLAGS) -c $< -o $@

date:
	./makedate

$(PARSERC) $(PARSERH): parser.y
	$(PARSERGENERATOR) -d parser.y

lex.yy.c: lexer.lex $(PARSERH)
	$(LEXERGENERATOR) lexer.lex

clean:
	rm -f $(OBJ) $(PARSERC) $(PARSERH) lex.yy.c $(EXECUTABLE)

tar:
	tar cvf MADAGASCAR.TAR \
		README plan build \
		asyntax.c asyntax.h \
		clausedb.c clausedb.h \
		clausesets.c clausesets.h \
		cleanup.c cleanup.h \
		dimacs.h dimacsinput.c dimacsinput.h \
		ground.c Cground.c \
		heuristics2.c interface.h \
		intsets.c intsets.h \
		invariants.c invariants.h \
		lexer.lex main.c main.h \
		makedate Makefile \
		operators.c operators.h \
		ordintsets.c ordintsets.h \
		parser.y \
		printplan.c printplan.h \
		scc.c scc.h \
		tables.c tables.h \
		translate2sat.c translate2sat.h \
		varvals.c learn2.c shortcuts.c \
		zPOSTF zPREF KISSATSOLVE