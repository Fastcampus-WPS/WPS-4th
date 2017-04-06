import argparse
import os
import subprocess
import sys

# Const
MODE_BASE = 'base'
MODE_DEBUG = 'debug'
MODE_PRODUCTION = 'production'
IMAGE_BASE = 'front-base'
IMAGE_DEBUG = 'front-debug'
IMAGE_PRODUCTION = 'front'
MAINTAINER = 'dev@azelf.com'
DOCKERFILE_BASE = 'Dockerfile.base'
DOCKERFILE_DEBUG = 'Dockerfile.debug'
DOCKERFILE_PRODUCTION = 'Dockerfile'

# ArgumentParser
parser = argparse.ArgumentParser(description='Build command')
parser.add_argument('-m', '--mode', type=str, default=MODE_DEBUG)
args = parser.parse_args()

# Paths
ROOT_DIR = os.path.dirname(__file__)
CONF_DIR = os.path.join(ROOT_DIR, '.conf')
CONF_DOCKER_DIR = os.path.join(CONF_DIR, 'docker')

# Docker conf files
dockerfile_template = open(os.path.join(CONF_DOCKER_DIR, '00_template.docker')).read()
dockerfile_base = open(os.path.join(CONF_DOCKER_DIR, '01_base.docker')).read()
dockerfile_extra = open(os.path.join(CONF_DOCKER_DIR, '02_extra.docker')).read()

if args.mode == MODE_BASE:
    dockerfile = dockerfile_template.format(
        from_image='ubuntu:16.04',
        maintainer=MAINTAINER,
        base=dockerfile_base,
        extra=''
    )
    filename = DOCKERFILE_BASE
    imagename = IMAGE_BASE
elif args.mode == MODE_DEBUG:
    dockerfile = dockerfile_template.format(
        from_image=IMAGE_BASE,
        maintainer=MAINTAINER,
        base='',
        extra=dockerfile_extra
    )
    filename = DOCKERFILE_DEBUG
    imagename = IMAGE_DEBUG
elif args.mode == MODE_PRODUCTION:
    dockerfile = dockerfile_template.format(
        from_image='ubuntu:16.04',
        maintainer=MAINTAINER,
        base=dockerfile_base,
        extra=dockerfile_extra
    )
    filename = DOCKERFILE_PRODUCTION
    imagename = IMAGE_PRODUCTION
else:
    sys.exit('Mode invalid')

with open(os.path.join(ROOT_DIR, filename), 'wt') as f:
    f.write(dockerfile)

build_command = 'docker build . -t {imagename} -f {filename}'.format(
    imagename=imagename,
    filename=filename
)
print('Docker build command: {}'.format(build_command))
subprocess.run(build_command, shell=True)
