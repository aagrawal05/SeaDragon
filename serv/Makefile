CC=g++
CFLAGS=-std=c++11 -I/opt/homebrew/include -L/opt/homebrew/lib -pthread
TLSFLAGS=-lboost_system -lssl -lcrypto
SOURCES=server.cpp
EXECUTABLE=server

all: $(EXECUTABLE)

tls: $(EXECUTABLE)_tls

$(EXECUTABLE): $(SOURCES)
	$(CC) $(CFLAGS) -o $(EXECUTABLE) $(SOURCES)

$(EXECUTABLE)_tls: $(SOURCES)
	$(CC) $(CFLAGS) $(TLSFLAGS) $(SOURCES) -o $(EXECUTABLE)_tls

clean:
	rm -f $(EXECUTABLE)

