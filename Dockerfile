FROM mhart/alpine-node:6.9.2

RUN apk add --no-cache make gcc g++ python git bash
COPY package.json /src/package.json
WORKDIR /src
RUN npm install

COPY . .

EXPOSE 8545

CMD ["/bin/bash", "/src/run.sh"]
