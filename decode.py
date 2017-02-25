import sys

def read_byte(byte_stream):
    bs = byte_stream.read(1)
    if len(bs) == 0:
        # EOF
        return None
    else:
        return bs[0]

def decoded(byte_stream):
    while True:
        b = read_byte(byte_stream)
        if b == None:
            break
        elif b == 0x83:
            b2 = read_byte(byte_stream)
            yield bytes([b2 ^ 0x20])
        else:
            yield bytes([b])

for bs in decoded(sys.stdin.buffer):
    sys.stdout.buffer.write(bs)
