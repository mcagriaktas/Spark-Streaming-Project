FROM python:latest

# Install OpenJDK 17
RUN mkdir -p /usr/share/man/man1mkdir -p /usr/share/man/man1 && \
    apt-get update && \
    apt-get install -y openjdk-17-jdk && \
    rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH=$PATH:$JAVA_HOME/bin
RUN echo $JAVA_HOME

RUN apt-get update -y
RUN apt-get install -y libzbar-dev 
RUN apt-get install -y bash 
RUN apt-get install -y gcc 
RUN apt-get install -y git 
RUN apt-get install -y libc-dev 
RUN apt-get install -y curl wget vim nano   
RUN apt-get install -y iputils-ping telnet openssh-client net-tools
RUN apt-get install -y man 
RUN apt-get install -y unzip 
RUN apt-get install -y vim-tiny 
RUN apt-get install -y bc 
RUN apt-get install -y openssh-server 
RUN apt-get install -y thrift-compiler 
RUN apt-get install -y sudo
RUN apt-get install -y build-essential
RUN apt-get autoremove -y
RUN apt-get install -y dos2unix
RUN apt-get clean

RUN curl -o spark-3.5.1-bin-hadoop3.tgz https://dlcdn.apache.org/spark/spark-3.5.1/spark-3.5.1-bin-hadoop3.tgz && \
    tar -xzvf spark-3.5.1-bin-hadoop3.tgz && \
    mv spark-3.5.1-bin-hadoop3 /opt/spark && \
    rm -rf spark-3.5.1-bin-hadoop3.tgz

ENV SPARK_HOME=/opt/spark
ENV PATH=$PATH:$SPARK_HOME/bin
ENV PATH=$PATH:$SPARK_HOME/sbin
ENV PYTHONPATH=$SPARK_HOME/python3:$SPARK_HOME/python3/lib/py4j-0.10.7-src.zip:$PYTHONPATH
RUN mkdir -p /opt/spark/history
COPY spark-defaults.conf /opt/spark/conf/spark-defaults.conf

RUN mkdir -p /opt/submitfiles
RUN chmod 777 /opt/submitfiles

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
ADD spark-master.sh spark-worker.sh /
