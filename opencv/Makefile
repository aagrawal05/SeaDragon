CC=g++
CFLAGS=-std=c++11 -I/opt/homebrew/include/opencv4 -L/opt/homebrew/lib -pthread
OPENCVFLAGS=-lopencv_core -lopencv_imgproc -lopencv_highgui -lopencv_videoio
TLSFLAGS=-lboost_system -lssl -lcrypto

SOURCES=vision.cpp
EXECUTABLE=vision

all: $(EXECUTABLE)

tls: $(EXECUTABLE)_tls

$(EXECUTABLE): $(SOURCES)
	$(CC) $(CFLAGS) -o $(EXECUTABLE) $(SOURCES) $(OPENCVFLAGS)

$(EXECUTABLE)_tls: $(SOURCES)
	$(CC) $(CFLAGS) $(SOURCES) -o $(EXECUTABLE)_tls $(TLSFLAGS) $(OPENCVFLAGS)

clean:
	rm -f $(EXECUTABLE) $(EXECUTABLE)_tls