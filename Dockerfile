#Here are things that probably never change so they will be cached
FROM 775013819650.dkr.ecr.eu-south-1.amazonaws.com/patty:stable

WORKDIR /project
RUN pip install tarjan prettytable
RUN rm -rf *

# Install itsat
COPY /benchmarks/planners/itsat /var/itsat
WORKDIR /var/itsat
RUN ./build
RUN chmod +x /var/springroll/springroll
ENV PATH /var/springroll/:${PATH}

# Copying
COPY . .

#Authorizations
RUN chmod +x exes/*


#Execution
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "patty", "./exes/run.sh"]