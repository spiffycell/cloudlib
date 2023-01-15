FROM alpine:3.17

# copy requirements.txt into the image
COPY requirements.txt /opt/app/

# install the build-deps, &c. as virtual
# this will make it so they're only used to install
# the requirements.txt libraries
# and are easily deleted after the requirements.txt
# libraries are installed
RUN apk add --no-cache --virtual build-deps \
	py3-pip \
	&& \
	pip3 install --no-cache --no-cache-dir --user --requirement /opt/app/requirements.txt \
	&& \
	apk del --no-cache build-deps

# copy rest of the contents into the image
COPY . /opt/app/
