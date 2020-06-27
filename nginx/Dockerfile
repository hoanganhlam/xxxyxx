FROM nginx:latest
RUN rm /etc/nginx/conf.d/default.conf
COPY ./conf.d/local.conf /etc/nginx/conf.d/local.conf
ENTRYPOINT ["nginx", "-g", "daemon off;"]