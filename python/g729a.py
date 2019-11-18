from typing import *
import ctypes

class G729Acoder:
    def __init__(
        self, 
        f_stateSize: Callable[[], int], 
        f_init: Callable[[Any], int], 
        f_process: Callable[[Any, Any, Any], int],
        inputSize: int,
        outputSize: int
    ) -> None:
        self._state = (ctypes.c_byte * f_stateSize())()
        if f_init(self._state) != 0:
            raise RuntimeError("G729 init state function " + f_init.__name__ + " returned error")
        self._f_process = f_process
        self.inputSize = inputSize
        self.outputSize = outputSize

    def process(self, input: bytearray) -> bytearray:
        if len(input) != self.inputSize:
            raise RuntimeError("G729: incorrect input size in process(). Expected: " + str(self.inputSize) +". Got: " + str(len(input)))
        inData = (ctypes.c_byte * len(input))(*input)
        outData = (ctypes.c_byte * self.outputSize)()
        if self._f_process(self._state, inData, outData) != 0:
            raise RuntimeError("G729 process function " + self._f_process.__name__ + " returned error")
        return bytearray(outData)

class G729Aencoder(G729Acoder):
    def __init__(self) -> None:
        g729aLib = ctypes.CDLL('./libg729a.so')
        super().__init__(
            g729aLib.G729A_Encoder_Get_Size,
            g729aLib.G729A_Encoder_Init,
            g729aLib.G729A_Encoder_Process,
            80*2,
            10
        )

class G729Adecoder(G729Acoder):
    def __init__(self) -> None:
        g729aLib = ctypes.CDLL('./libg729a.so')
        super().__init__(
            g729aLib.G729A_Decoder_Get_Size,
            g729aLib.G729A_Decoder_Init,
            g729aLib.G729A_Decoder_Process,
            10,
            80*2
        )


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4 or (sys.argv[1] != 'encode' and sys.argv[1] != 'decode'):
        print('Usage: ./' + sys.argv[0] + ' encode/decode in_file out_file')
        exit(0)

    coder = G729Aencoder() if sys.argv[1] == 'encode' else G729Adecoder() # type: G729Acoder
    
    with open(sys.argv[2], 'rb') as infile, open(sys.argv[3], 'wb') as outfile:
        while True:
            buff = infile.read(coder.inputSize)
            if len(buff) < coder.inputSize:
                break
            outfile.write(coder.process(bytearray(buff)))
    print('Done.')