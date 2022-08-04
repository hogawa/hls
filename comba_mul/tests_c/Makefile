CC      = gcc
CFLAGS  = -std=c99 -Wall -O3

# OBJS    = comba256x256.o
OBJS    = comba320x320.o
# DEFINES = -DCOMBA256x256
DEFINES = -DCOMBA320X320

%.o: %.c
	$(CC) $(DEFINES) $(CFLAGS) -c $^ -o $(@F)

all: test

test: $(OBJS) test.o
	$(CC) $(DEFINES) $(OBJS) test.o -o test

clean:
	rm -rf *.o test
