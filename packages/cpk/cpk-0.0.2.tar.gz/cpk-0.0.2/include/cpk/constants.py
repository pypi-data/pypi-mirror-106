DEBUG = False

CANONICAL_ARCH = {
    "arm": "arm32v7",
    "arm32v7": "arm32v7",
    "armv7l": "arm32v7",
    "armhf": "arm32v7",
    "x64": "amd64",
    "x86_64": "amd64",
    "amd64": "amd64",
    "Intel 64": "amd64",
    "arm64": "arm64v8",
    "arm64v8": "arm64v8",
    "armv8": "arm64v8",
    "aarch64": "arm64v8",
}

BUILD_COMPATIBILITY_MAP = {
    "arm32v7": ["arm32v7"],
    "arm64v8": ["arm32v7", "arm64v8"],
    "amd64": ["amd64"]
}

CONTAINER_LABEL_DOMAIN = "cpk.label"

DOCKERHUB_API_URL = {
    "token": "https://auth.docker.io/token?scope=repository:{image}:pull&service=registry.docker.io",
    "digest": "https://registry-1.docker.io/v2/{image}/manifests/{tag}",
    "inspect": "https://registry-1.docker.io/v2/{image}/blobs/{digest}",
}
