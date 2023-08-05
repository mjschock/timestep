FROM node:16-bullseye-slim

ENV YARN_CACHE_FOLDER=/cache/yarn

WORKDIR /app

# install dependencies
COPY package.json yarn.lock ./
RUN --mount=type=cache,target=/cache/yarn \
  yarn install

# copy app source
COPY . ./

CMD ["yarn", "dev"]
