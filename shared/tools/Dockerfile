# Stage 1: Build phase (with all dependencies)
FROM python:3.12-alpine AS build

# Define build arguments that can be passed during the build
ARG RUN_NUMBER
ARG MATRIX_VERSION
ARG MATRIX_TYPE

# Set environment variables inside the Docker image using the passed arguments
ENV RUN_NUMBER=$RUN_NUMBER
ENV MATRIX_VERSION=$MATRIX_VERSION
ENV MATRIX_TYPE=$MATRIX_TYPE

# Install dependencies needed for building the tool (e.g., tar, Python, etc.)
RUN apk add --no-cache tar musl-dev bash git python3-dev py3-pip build-base \
    && git clone https://github.com/Coldhost/yolks \
    && cd yolks/shared/tools \
    && pip install -r requirements.txt --break\
    && chmod +x build.sh \
    && ./build.sh \
    && mkdir -p ghcr_tools \
    && ls dist/tools \
    && mv dist/tools ghcr_tools/tools \
    && chmod +x ghcr_tools/tools \
    && ./ghcr_tools/tools version \
    && tar -czf ghcr_tools.tar.gz -C ghcr_tools tools \
    && mv ghcr_tools.tar.gz /


# Stage 2: Build phase (with all dependencies)
FROM python:3.8-alpine3.10 AS build-legacy

# Define build arguments that can be passed during the build
ARG RUN_NUMBER
ARG MATRIX_VERSION
ARG MATRIX_TYPE

# Set environment variables inside the Docker image using the passed arguments
ENV RUN_NUMBER=$RUN_NUMBER
ENV MATRIX_VERSION=$MATRIX_VERSION
ENV MATRIX_TYPE=$MATRIX_TYPE

# Install dependencies needed for building the tool (e.g., tar, Python, etc.)
RUN apk add --no-cache tar musl-dev bash git python3-dev py3-pip build-base \
    && git clone https://github.com/Coldhost/yolks \
    && cd yolks/shared/tools \
    && pip install --upgrade pip setuptools wheel \
    && pip install -r --use-pep517 requirements.txt \
    && chmod +x build.sh \
    && ./build.sh \
    && mkdir -p ghcr_tools \
    && ls dist/tools \
    && mv dist/tools ghcr_tools/tools \
    && chmod +x ghcr_tools/tools \
    && ./ghcr_tools/tools version \
    && tar -czf ghcr_tools_legacy.tar.gz -C ghcr_tools tools \
    && mv ghcr_tools_legacy.tar.gz /

# Stage 3: Final runtime phase (minimal image)
FROM busybox:1.35-uclibc

# Only copy the tarball from the build stage (no dependencies, no source code)
COPY --from=build /ghcr_tools.tar.gz /ghcr_tools.tar.gz
COPY --from=build-legacy /ghcr_tools_legacy.tar.gz /ghcr_tools_legacy.tar.gz

# Set the tarball as the entrypoint
ENTRYPOINT ["cat", "/ghcr_tools.tar.gz"]