# Base image
FROM golang:1.7-alpine

# Maintainer info
MAINTAINER Travis Rhoden <travis.rhoden@dell.com>

RUN apk add --no-cache git

# Get the project
RUN go get github.com/ghostplant/Hackathon_2018/game-controller

# Set working directory
WORKDIR /go/src/github.com/ghostplant/Hackathon_2018/game-controller

# Expose port
EXPOSE 8080

# Run Game Controller
CMD go run *.go
