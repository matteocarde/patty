#Here are things that probably never change so they will be cached
FROM --platform=linux/amd64 ubuntu:18.04

RUN ls

RUN apt-get update
# Install Node
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
ENV PATH "$PATH:/project/experiments/libs"

# Install python 3.8
RUN apt-get install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get install python3.8 -y

# Make python 3.8 the default
RUN echo "alias python=python3.8" >> ~/.bashrc
RUN export PATH=${PATH}:/usr/bin/python3.8
RUN /bin/bash -c "source ~/.bashrc"

# Install pip
RUN apt-get install python3-pip -y
RUN python3.8 -m pip install --upgrade pip

# Install conda
ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"

RUN apt-get install -y wget && rm -rf /var/lib/apt/lists/*

RUN wget https://repo.anaconda.com/miniconda/Miniconda3-py311_25.7.0-2-Linux-x86_64.sh
RUN mkdir /root/.conda
RUN bash Miniconda3-py311_25.7.0-2-Linux-x86_64.sh -b
RUN rm -f Miniconda3-py311_25.7.0-2-Linux-x86_64.sh
RUN conda --version
RUN conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/main
RUN conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/r

WORKDIR /project

# Create environment
RUN conda create --name patty
SHELL ["conda", "run", "--no-capture-output", "-n", "patty", "/bin/bash", "-c"]

# Create conda env
COPY environment.yml environment.yml
RUN conda env update --file environment.yml

# Install patty
COPY /benchmarks/planners/patty /var/patty
ENV PATH /var/patty/:${PATH}
RUN chmod +x /var/patty/patty
RUN conda env export

RUN apt-get update
RUN apt-get install time -y
RUN pip install boto3 numpy networkx tarjan prettytable graphlib-backport pyeda
RUN pip install --pre unified-planning

WORKDIR /project
# Copying

#Install local pyeda
WORKDIR /
#COPY src/ src/
COPY libs/pyeda libs/pyeda
WORKDIR libs/pyeda
RUN rm -rf dist
RUN rm -rf build
RUN rm -rf pyeda
RUN mv pyeda_linux pyeda
RUN python3.8 setup.py install
RUN rm -rf pyeda
RUN mv build/lib.linux-x86_64-cpython-38/pyeda/ pyeda/

#Install madagascar
COPY /benchmarks/planners/madagascar /var/madagascar
ENV PATH /var/madagascar/:${PATH}

#Install PySAT
RUN pip install 'python-sat[aiger,approxmc,cryptosat,pblib]'

WORKDIR /project
COPY . .
#Authorizations
RUN chmod +x exes/*

WORKDIR /
RUN rm -rf project/libs/pyeda
RUN mv libs/pyeda project/libs/pyeda

WORKDIR /project

#Execution
ENTRYPOINT ["conda", "run", "--live-stream", "-n", "patty", "./exes/run.sh"]
