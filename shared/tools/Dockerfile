# Stage 1: Build phase (with all dependencies)
FROM alpine:latest as build

# Install dependencies needed for building the tool (e.g., tar, Python, etc.)
RUN apk add --no-cache tar python3 git py3-pip build-base \
    && git clone https://github.com/Coldhost/yolks \
    && cd yolks/shared/tools \
    && pip install -r requirements.txt \
    && chmod +x build.sh \
    && ./build.sh \
    && VERSION=v${{ github.run_number }}-${{ matrix.version }}-${{ matrix.type }} \
    && mkdir -p ghcr_tools \
    && mv dist/tools ghcr_tools/tools \
    && chmod +x ghcr_tools/tools \
    && tar -czf ghcr_tools.tar.gz -C ghcr_tools tools

# Stage 2: Final runtime phase (minimal image)
FROM busybox:1.35-uclibc

# Only copy the tarball from the build stage (no dependencies, no source code)
COPY --from=build /ghcr_tools.tar.gz /ghcr_tools.tar.gz

# Set the tarball as the entrypoint
ENTRYPOINT ["cat", "/ghcr_tools.tar.gz"]