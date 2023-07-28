# Team 1 -- Numeric Fast Downward

## Compile

Install CPLEX Optimization Studio 22.1.1 in `/opt/ibm/ILOG/CPLEX_Studio2211`.
Then, run the script with the root privilege.

```bash
./compile
```

## Run

### Optimal LNP

```bash
./run-opt-lnp-1 domain.pddl problem.pddl plan
```

```bash
./run-opt-lnp-2 domain.pddl problem.pddl plan
```

### Optimal SNP

```bash
./run-opt-snp-1 domain.pddl problem.pddl plan
```

```bash
./run-opt-snp-2 domain.pddl problem.pddl plan
```

### Satisficing/Agile LNP

```bash
./run-sat-lnp-1 domain.pddl problem.pddl plan
```

### Satisficing/Agile SNP

```bash
./run-sat-snp-1 domain.pddl problem.pddl plan
```

```bash
./run-sat-snp-2 domain.pddl problem.pddl plan
```
