#Here are things that probably never change so they will be cached
FROM 775013819650.dkr.ecr.eu-south-1.amazonaws.com/patty:stable

WORKDIR /project
RUN pip install tarjan prettytable
RUN rm -rf *

# Install itsat
COPY /benchmarks/planners/itsat /var/itsat
WORKDIR /var/itsat
RUN ./build
RUN mv plan itsat
RUN chmod +x /var/itsat/itsat
ENV PATH /var/itsat/:${PATH}

# Install optic
COPY /benchmarks/planners/optic /var/optic
WORKDIR /var/optic

RUN apt-get install -y cmake coinor-libcbc-dev coinor-libclp-dev coinor-libcoinutils-dev libbz2-dev libgsl-dev
RUN export CFLAGS=-m32
RUN export CXXFLAGS=-m32
RUN export LDFLAGS=-m32
RUN ./run-cmake-debug
RUN ./build-debug
RUN ls -la debug/optic
RUN cp debug/optic/optic-clp optic
RUN chmod +x optic
ENV PATH /var/optic/:${PATH}

# Install tfd
COPY /benchmarks/planners/tfd /var/tfd
WORKDIR /var/tfd
RUN ./build
RUN chmod +x tfd
ENV PATH /var/tfd/:${PATH}

# Install lpg-td
COPY /benchmarks/planners/lpg-td /var/lpg-td
WORKDIR /var/lpg-td
RUN chmod +x lpg-td
ENV PATH /var/lpg-td/:${PATH}

# Install ANMLSMT
COPY /benchmarks/planners/anmlsmt /var/anmlsmt
WORKDIR /var/anmlsmt
RUN chmod +x anmlsmt
ENV PATH /var/anmlsmt/:${PATH}

# Install PyPy
COPY /benchmarks/planners/pypy /var/pypy
WORKDIR /var/pypy
RUN chmod +x pypy
ENV PATH /var/pypy/:${PATH}

WORKDIR /project
COPY . .
#Authorizations
RUN chmod +x exes/*

RUN anmlsmt solve -l 3 -a smt-incr -q mathsat files/temporal/bottles-all/anml/domain.anml files/temporal/bottles-all/anml/instances/problem_2.anml
#RUN anmlsmt solve -l 3 -a smt-incr -q mathsat -P files/temporal/parking/domain.pddl files/temporal/parking/instances/p6-6-6.pddl -O
#RUN itsat -alg layer files/temporal/parking/domain.pddl files/temporal/parking/instances/p6-6-6.pddl \*


#Execution
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "patty", "./exes/run.sh"]