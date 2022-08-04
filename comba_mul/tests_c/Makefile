CC      = gcc
CFLAGS  = -std=c99 -Wall -O3

# OBJS = comba256x256.o
OBJS = comba320x320.o
# OBJS = comba384x384.o
# OBJS = comba448x448.o
# OBJS = comba512x512.o
# DEFINES = -DCOMBA256X256
DEFINES = -DCOMBA320X320
# DEFINES = -DCOMBA384X384
# DEFINES = -DCOMBA448X448
# DEFINES = -DCOMBA512X512

%.o: %.c
	$(CC) $(DEFINES) $(CFLAGS) -c $^ -o $(@F)

all: test

test: $(OBJS) test.o
	$(CC) $(DEFINES) $(OBJS) test.o -o test

clean:
	rm -rf *.o test
