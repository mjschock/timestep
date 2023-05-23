FROM node:18.16.0

# ENV YARN_CACHE_FOLDER=/cache/yarn

WORKDIR /app

# install dependencies
# COPY package.json yarn.lock ./
COPY package.json package-lock.json ./
# RUN --mount=type=cache,target=/cache/yarn \
#   yarn install
RUN npm install

# copy app source
COPY . ./

# CMD ["yarn", "dev"]
CMD ["npm", "run", "dev"]
