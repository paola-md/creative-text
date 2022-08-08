

# syntax=docker/dockerfile:1
FROM huggingface/transformers-pytorch-gpu
MAINTAINER Paola Mejia "pmejiado@gmail.com"
# Miniconda install copy-pasted from Miniconda's own Dockerfile reachable
# at: https://github.com/ContinuumIO/docker-images/blob/master/miniconda3/debian/Dockerfile

ENV PATH /opt/conda/bin:$PATH

RUN apt-get update --fix-missing && \
    apt-get install -y wget bzip2 ca-certificates libglib2.0-0 libxext6 libsm6 libxrender1 git mercurial subversion screen && \
    apt-get clean

RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh && \
    /opt/conda/bin/conda clean -tipsy && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate base" >> ~/.bashrc && \
    find /opt/conda/ -follow -type f -name '*.a' -delete && \
    find /opt/conda/ -follow -type f -name '*.js.map' -delete && \
    /opt/conda/bin/conda clean -afy

RUN apt-get update && \
    apt-get install -y sudo \
    build-essential curl nano \
    libcurl4-openssl-dev \
    libssl-dev wget \
    python3-pip \
    unzip \
    git-lfs \
    git && \
    pip3 install --upgrade pip

RUN apt-get install -y openssh-server

ENV SHELL=/bin/bash \
    NB_USER=mejia \
    NB_UID=223552 \
    NB_GROUP=DVET-unit \
    NB_GID=223552
ENV HOME=/home/$NB_USER

RUN groupadd $NB_GROUP -g $NB_GID
RUN useradd -m -s /bin/bash -N -u $NB_UID -g $NB_GID $NB_USER && \
    echo "${NB_USER}:${NB_USER}" | chpasswd && \
    usermod -aG sudo,adm,root ${NB_USER}
RUN chown -R ${NB_USER}:${NB_GROUP} ${HOME}

# The user gets passwordless sudo
RUN echo "${NB_USER}   ALL = NOPASSWD: ALL" > /etc/sudoers

# Project setup
ARG DEBIAN_FRONTEND=noninteractive

# File Structure
RUN mkdir creative_text/ && mkdir creative_text/creativity/ \
    && mkdir creative_text/creativity/models 


COPY creativity creative_text/creativity/

COPY requirements.txt creative_text/requirements.txt
WORKDIR /creative_text/
RUN pip3 install -r requirements.txt

EXPOSE 22
EXPOSE 8888
#CMD exec /bin/bash -c "trap : TERM INT; sleep infinity & wait"