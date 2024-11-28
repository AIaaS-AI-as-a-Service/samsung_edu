# Use a base image with CUDA 12.2.2 and cuDNN 8
FROM ultralytics/yolov5:latest

RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    python3 \
    python3-pip \
    git \
    wget \
    curl \
    openssh-server \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y libc6

# Python 환경 설정
RUN pip3 install --upgrade pip

# 작업 디렉토리 설정
WORKDIR /workspace

RUN git config --global --add safe.directory /workspace

# Python 패키지 설치
COPY requirements.txt /workspace/
RUN pip3 install -r requirements.txt

# Jupyter 및 기타 필요 패키지 설치
RUN pip3 install jupyter

# Code Server 수동 설치 (이전 버전, 예: 3.12.0)
RUN curl -fsSL https://github.com/coder/code-server/releases/download/v3.12.0/code-server-3.12.0-linux-amd64.tar.gz -o code-server.tar.gz && \
    tar -xzf code-server.tar.gz && \
    mv code-server-3.12.0-linux-amd64 /usr/local/code-server && \
    ln -s /usr/local/code-server/bin/code-server /usr/bin/code-server && \
    rm code-server.tar.gz

# PATH에 code-server 추가
ENV PATH="/usr/local/code-server/bin:${PATH}"

# 필요한 VS Code 확장 프로그램 설치
RUN /usr/local/code-server/bin/code-server --install-extension ms-python.python
RUN /usr/local/code-server/bin/code-server --install-extension ms-toolsai.jupyter
