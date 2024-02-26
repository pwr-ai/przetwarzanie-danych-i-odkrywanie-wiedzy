FROM ubuntu:20.04

RUN apt-get update
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install tzdata
RUN apt-get install -y \
    git \
    wget \
    tmux \
    htop \
    vim \
    less \
    gcc \
    software-properties-common \
    && add-apt-repository ppa:deadsnakes/ppa && apt update

RUN apt-get install -y --no-install-recommends \
        python3.8 \
        python3.8-dev \
        python3.8-distutils

RUN wget https://bootstrap.pypa.io/get-pip.py &&  \
	 python3.8 get-pip.py && \
	 ln -s /usr/bin/python3.8 /usr/local/bin/python3

RUN apt-get install -y zsh && \
    chsh -s /bin/zsh && \
    zsh -c "$(wget https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"

ADD . lab5-example/
WORKDIR /lab5-example
RUN pip install -r requirements.txt
RUN git remote set-url origin https://github.com/pwr-ai/przetwarzanie-danych-i-odkrywanie-wiedzy

CMD mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root s3://data --host 0.0.0.0