FROM node:16-bullseye-slim

# ENV YARN_CACHE_FOLDER=/cache/yarn
# ENV NPM_CACHE_FOLDER="$(npm config get cache)"
ENV NPM_CACHE_FOLDER=/root/.npm

WORKDIR /app

# install dependencies
COPY www/package.json www/package-lock.json ./
# RUN --mount=type=cache,target=/cache/yarn \
#   yarn install
RUN --mount=type=cache,target=/root/.npm \
  npm install

# copy app source
COPY www/ ./

# CMD ["yarn", "dev"]
CMD ["npm", "run", "dev"]
