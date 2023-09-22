#Here are things that probably never change so they will be cached
FROM 775013819650.dkr.ecr.eu-south-1.amazonaws.com/patty:stable

WORKDIR /project
# Copying
COPY . .

#Authorizations
RUN chmod +x exes/*

#Execution
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "patty", "./exes/run.sh"]
