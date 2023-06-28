#Here are things that probably never change so they will be cached
FROM --platform=linux/amd64 ubuntu:18.04

RUN apt-get update
ENV NODE_VERSION=12.22.12
RUN apt-get install -y curl
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
ENV NVM_DIR=/root/.nvm
RUN . "$NVM_DIR/nvm.sh" && nvm install ${NODE_VERSION}
RUN . "$NVM_DIR/nvm.sh" && nvm use v${NODE_VERSION}
RUN . "$NVM_DIR/nvm.sh" && nvm alias default v${NODE_VERSION}
ENV PATH="/root/.nvm/versions/node/v${NODE_VERSION}/bin/:${PATH}"
RUN node --version
RUN npm --version


RUN npm install
#ENV PATH "$PATH:/project/experiments/libs"

# Install python 3.7
RUN apt-get install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get install python3.7 -y

# Make python 3.7 the default
RUN echo "alias python=python3.7" >> ~/.bashrc
RUN export PATH=${PATH}:/usr/bin/python3.7
RUN /bin/bash -c "source ~/.bashrc"

# Install pip
RUN apt-get install python3-pip -y
RUN python3.7 -m pip install --upgrade pip


ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"

RUN apt-get install -y wget && rm -rf /var/lib/apt/lists/*

RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh 
RUN mkdir /root/.conda 
RUN bash Miniconda3-latest-Linux-x86_64.sh -b 
RUN rm -f Miniconda3-latest-Linux-x86_64.sh 
RUN conda --version

WORKDIR /project
COPY environment.yml environment.yml
RUN conda env create -f environment.yml

RUN add-apt-repository ppa:sri-csl/formal-methods
RUN apt-get install -y yices2
RUN which yices
RUN apt-get install -y swig
COPY benchmarks/libs benchmarks/libs
RUN which yices
WORKDIR /project/benchmarks/libs/yicespy
RUN apt-get install -y libpython3.7-dev
RUN pip install pysmt
RUN pysmt-install --yices

WORKDIR /project
SHELL ["conda", "run", "-n", "patty", "/bin/bash", "-c"]

COPY . .


RUN chmod +x exes/*

#Here are things that changes a lot


#Execution
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "patty", "./exes/run.sh"]
