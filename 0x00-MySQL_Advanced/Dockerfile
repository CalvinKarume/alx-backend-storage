FROM ubuntu:18.04

# Install Python 3.7
RUN apt-get update && \
    apt-get install -y python3.7 && \
    apt-get install -y python3-pip

# Install MySQL
RUN apt-get install -y mysql-server

# Expose MySQL port
EXPOSE 3306

# Start MySQL
CMD ["service", "mysql", "start"]

# Set up SSH (you might need to customize this part)
RUN apt-get install -y openssh-server
RUN mkdir /var/run/sshd
RUN echo 'root:root' | chpasswd
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN service ssh restart

