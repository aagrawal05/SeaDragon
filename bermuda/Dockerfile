FROM ros:humble

RUN apt update

ARG DEBIAN_FRONTEND=noninteractive
RUN apt install -y \
	ros-humble-turtlesim \
    lightdm

CMD ["startxfce4"]
