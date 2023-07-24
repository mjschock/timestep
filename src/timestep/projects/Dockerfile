FROM caddy:2.6.4-builder as builder

RUN xcaddy build \
    --with github.com/greenpau/caddy-security

FROM caddy:2.6.4

COPY --from=builder /usr/bin/caddy /usr/bin/caddy

COPY ./Caddyfile /etc/caddy/Caddyfile
COPY www /srv/www
