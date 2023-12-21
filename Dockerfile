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


WORKDIR /project
COPY . .
#Authorizations
RUN chmod +x exes/*

# RUN itsat -alg time files/temporal/floortile/domain.pddl files/temporal/floortile/instances/p442-1.pddl plan.txt
# RUN more plan.txt.1

RUN tfd files/temporal/parking/domain.pddl files/temporal/parking/instances/p15-9-3.pddl plan.txt


#Execution
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "patty", "./exes/run.sh"]