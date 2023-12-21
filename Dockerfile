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

RUN apt-get install -y cmake coinor-libcbc-dev coinor-libclp-dev coinor-libcoinutils-dev libbz2-dev
RUN ./run-cmake-debug
RUN ./build-debugging
RUN ls -la

COPY . .
#Authorizations
RUN chmod +x exes/*

# RUN itsat -alg time files/temporal/floortile/domain.pddl files/temporal/floortile/instances/p442-1.pddl plan.txt
# RUN more plan.txt.1

# RUN planutils run optic 


#Execution
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "patty", "./exes/run.sh"]