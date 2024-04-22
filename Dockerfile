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

# Install conda
ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"

RUN apt-get install -y wget && rm -rf /var/lib/apt/lists/*

RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
RUN mkdir /root/.conda
RUN bash Miniconda3-latest-Linux-x86_64.sh -b
RUN rm -f Miniconda3-latest-Linux-x86_64.sh
RUN conda --version

WORKDIR /project

# Create environment
RUN conda create --name patty
SHELL ["conda", "run", "--no-capture-output", "-n", "patty", "/bin/bash", "-c"]

# Install yices
RUN pip install pysmt
RUN add-apt-repository ppa:sri-csl/formal-methods
RUN apt-get install -y swig autoconf gperf libgmp-dev

# Install java
RUN apt-get install -y openjdk-8-jdk ant ca-certificates-java
RUN update-ca-certificates -f;

RUN add-apt-repository ppa:linuxuprising/java
ENV DEBIAN_FRONTEND noninteractive
ENV DEBIAN_FRONTEND teletype
RUN yes | apt-get install -y oracle-java17-installer --install-recommends

## Install CPLEX
#COPY benchmarks/planners/cplex/installer.bin /tmp/installer
#COPY benchmarks/planners/cplex/install.properties /tmp/install.properties
#WORKDIR /project/benchmarks/planners/cplex
#RUN ls -la
#
#ARG COSDIR=/opt/CPLEX
#ARG CPX_PYVERSION=3.7
#RUN chmod u+x /tmp/installer
#
#RUN /tmp/installer -f /tmp/install.properties
#RUN rm -f /tmp/installer /tmp/install.properties
#
#ENV PATH ${PATH}:${COSDIR}/cplex/bin/x86-64_linux
#ENV PATH ${PATH}:${COSDIR}/cpoptimizer/bin/x86-64_linux
#ENV PATH ${PATH}:${COSDIR}/opl/bin/x86-64_linux
#ENV LD_LIBRARY_PATH ${LD_LIBRARY_PATH}:${COSDIR}/cplex/bin/x86-64_linux
#ENV LD_LIBRARY_PATH ${LD_LIBRARY_PATH}:${COSDIR}/cpoptimizer/bin/x86-64_linux
#ENV LD_LIBRARY_PATH ${LD_LIBRARY_PATH}:${COSDIR}/opl/bin/x86-64_linux
#
#ENV DOWNWARD_CPLEX_ROOT=${COSDIR}/cplex
#ENV DOWNWARD_CONCERT_ROOT=${COSDIR}/concert
#
## Installing OSI
#WORKDIR /var
#RUN apt-get install zlib1g-dev
#RUN wget http://www.coin-or.org/download/source/Osi/Osi-0.107.9.tgz
#RUN tar zxvf Osi-0.107.9.tgz
#WORKDIR /var/Osi-0.107.9
#RUN ls -la
#RUN ./configure CC="gcc"  CFLAGS="-pthread -Wno-long-long" \
#  CXX="g++" CXXFLAGS="-pthread -Wno-long-long" \
#  LDFLAGS="-L$DOWNWARD_CPLEX_ROOT/lib/x86-64_linux/static_pic" \
#  --without-lapack --enable-static=no \
#  --prefix="$DOWNWARD_COIN_ROOT" \
#  --disable-bzlib \
#  --with-cplex-incdir=$DOWNWARD_CPLEX_ROOT/include/ilcplex \
#  --with-cplex-lib="-lcplex -lm -ldl"
#
#RUN make
#RUN make install
#WORKDIR /var
#RUN rm -rf Osi-0.107.9
#RUN rm Osi-0.107.9.tgz

# Install Springroll
COPY /benchmarks/planners/springroll-planner /var/springroll
ENV PATH /var/springroll/:${PATH}
WORKDIR /var/springroll
RUN ant dist
RUN ./install
RUN chmod +x /var/springroll/springroll

# Install Metric FF
COPY /benchmarks/planners/metric-ff /var/metric-ff
WORKDIR /var/metric-ff
RUN apt-get install -y bison flex
RUN make
ENV PATH /var/metric-ff/:${PATH}

# Install ENHSP
COPY /benchmarks/planners/enhsp /var/enhsp
ENV PATH /var/enhsp/:${PATH}
RUN chmod +x /var/enhsp/enhsp

# Install patty
COPY /benchmarks/planners/patty /var/patty
ENV PATH /var/patty/:${PATH}
RUN chmod +x /var/patty/patty
RUN apt-get install -y time
RUN conda env export

# Create conda env
COPY environment.yml environment.yml
RUN conda env update --file environment.yml

RUN pysmt-install --check
RUN pysmt-install --yices --confirm-agreement
RUN pysmt-install --check

# Install python 2.7
RUN apt-get install python2.7 -y
RUN which python2.7

# Install Numeric Fast Downward
RUN apt-get install -y cmake
COPY /benchmarks/planners/nfd /var/nfd
WORKDIR /var/nfd/src/search/bliss-0.73
RUN make
WORKDIR /var/nfd
RUN ./build.py release64
ENV PATH /var/nfd/:${PATH}
RUN chmod +x /var/nfd/nfd

# Install OMTPlan
RUN pip install networkx
RUN pip install numpy
COPY /benchmarks/planners/omtplan /var/omtplan
ENV PATH /var/omtplan/:${PATH}
RUN chmod +x /var/omtplan/omtplan

RUN pip install tarjan prettytable

WORKDIR /project
# Copying
COPY . .

#Authorizations
RUN chmod +x exes/*

#Execution
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "patty", "./exes/run.sh"]
