# ============================================================
# YONG-NIAN-V1 — Alpine Dockerfile
# ============================================================
FROM alpine:3.19

LABEL maintainer="Ian Carter Kulani" \
      description="YONG-NIAN-V1 Penetration Testing Platform" \
      version="1.0.0"

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    LANG=C.UTF-8

# ------------------------------------------------------------
# System + Network tools
# ------------------------------------------------------------
RUN apk add --no-cache \
    python3 \
    py3-pip \
    py3-virtualenv \
    bash \
    curl \
    wget \
    ca-certificates \
    openssl \
    nmap \
    nmap-scripts \
    netcat-openbsd \
    traceroute \
    mtr \
    bind-tools \
    whois \
    openssh-client \
    openssh \
    git \
    tcpdump \
    iputils \
    libcap \
    && rm -rf /var/cache/apk/*

# ------------------------------------------------------------
# Build dependencies (needed to compile cryptography, pillow,
# numpy, matplotlib, pynput, scapy, etc.)
# ------------------------------------------------------------
RUN apk add --no-cache --virtual .build-deps \
    build-base \
    musl-dev \
    linux-headers \
    libffi-dev \
    openssl-dev \
    cargo \
    rust \
    python3-dev \
    jpeg-dev \
    zlib-dev \
    freetype-dev \
    libpng-dev \
    tiff-dev \
    openblas-dev \
    gfortran \
    py3-numpy-dev \
    && rm -rf /var/cache/apk/*

# ------------------------------------------------------------
# Pre-install heavy compiled wheels from Alpine repos
# (faster + smaller than pip-compiling on musl)
# ------------------------------------------------------------
RUN apk add --no-cache \
    py3-numpy \
    py3-matplotlib \
    py3-pillow \
    py3-cryptography \
    py3-requests \
    py3-yaml

# ------------------------------------------------------------
# Install Python dependencies via pip
# ------------------------------------------------------------
WORKDIR /app
COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --break-system-packages -r requirements.txt || \
    pip install --no-cache-dir -r requirements.txt

# ------------------------------------------------------------
# Copy the application
# ------------------------------------------------------------
COPY yong_nian_v1.py /app/yong_nian_v1.py
COPY setup.py /app/setup.py

# Optional CLI shims
RUN chmod +x /app/yong_nian_v1.py && \
    ln -sf /app/yong_nian_v1.py /usr/local/bin/yong-nian && \
    ln -sf /app/yong_nian_v1.py /usr/local/bin/yongnian

# ------------------------------------------------------------
# Runtime directories
# ------------------------------------------------------------
RUN mkdir -p /app/.yong_nian_v1 /app/yong_nian_reports

VOLUME ["/app/.yong_nian_v1", "/app/yong_nian_reports"]

# Web dashboard port
EXPOSE 5000

# ------------------------------------------------------------
# Healthcheck
# ------------------------------------------------------------
HEALTHCHECK --interval=30s --timeout=10s --start-period=20s --retries=3 \
    CMD python3 -c "import yong_nian_v1" || exit 1

# ------------------------------------------------------------
# Entrypoint
# ------------------------------------------------------------
ENTRYPOINT ["python3", "/app/yong_nian_v1.py"]
CMD []
