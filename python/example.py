from g729a import *

# encoder
encoder = G729Aencoder() #create encoder
pcmData = bytearray(160) #160 byte of PCM sound (80 x 16-bit samples)
g729aData = encoder.process(pcmData) #returns 10 byte of g729a segment

# decoder
decoder = G729Adecoder() #create decoder
g729aData = bytearray(10) #10 byte of g729a segment
pcmData = decoder.process(g729aData) #returns 160 byte of PCM sound (80 x 16-bit samples)