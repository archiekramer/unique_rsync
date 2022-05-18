from ubuntu:focal
RUN apt-get update && apt-get install python3 python3-pip locales cron -yq
RUN locale-gen fr_FR.UTF-8
COPY ./default_locale /etc/default/locale
RUN chmod 0755 /etc/default/locale
ENV PYTHONIOENCODING=utf-8
ENV LC_ALL=fr_FR.UTF-8
ENV LANG=fr_FR.UTF-8
ENV LANGUAGE=fr_FR.UTF-8

# # Copy hello-cron file to the cron.d directory
# COPY cron /etc/cron.d/cron_it_abo
# # Give execution rights on the cron job
# RUN chmod 0644 /etc/cron.d/cron_it_abo
# # Apply cron job
# RUN crontab /etc/cron.d/cron_it_abo
# # Create the log file to be able to run tail
# RUN touch /var/log/cron.log
# # Run the command on container startup

# WORKDIR /etc/apache2/
# #COPY ports.conf . 
# COPY gestabogar.conf ./sites-enabled/
# RUN rm -rf /etc/apache2/sites-enabled/000-default.conf && a2enmod proxy proxy_http
# WORKDIR /var/www/InterfaceAbonnementGar/
# COPY requirements.txt . 
# RUN pip3 install --no-cache-dir -r requirements.txt
# ADD . .

# WORKDIR /var/www/InterfaceAbonnementGar/gar_ws_interface/
# #EXPOSE 8080
# EXPOSE 80
# CMD service apache2 start && cron && gunicorn --bind 0.0.0.0:8000 gar_ws_interface.wsgi

# # docker run -d -v ~/Temp:/usr/src/app/logs

