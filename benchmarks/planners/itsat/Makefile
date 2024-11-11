# Builds all the projects in the solution...
.PHONY: all_projects
all_projects: zchaff minisat precosat tsat

# Builds project 'zchaff'...
.PHONY: zchaff
zchaff: 
	make --directory="zchaff/" --file=zchaff.makefile

# Builds project 'tsat'...
.PHONY: tsat
tsat: 
	make --directory="tsat/" --file=tsat.makefile

# Builds project 'minisat'...
.PHONY: minisat
minisat: 
	make --directory="minisat/" --file=minisat.makefile

# Builds project 'precosat'...
.PHONY: precosat
precosat: 
	make --directory="precosat/" --file=precosat.makefile

# Cleans all projects...
.PHONY: clean
clean:
	make --directory="zchaff/" --file=zchaff.makefile clean
	make --directory="tsat/" --file=tsat.makefile clean
	make --directory="minisat/" --file=minisat.makefile clean
	make --directory="precosat/" --file=precosat.makefile clean

.PHONY: install
install:
	sudo cp -f gccRelease/tsat.exe /usr/bin/tsat
	sudo chmod +x /usr/bin/tsat


