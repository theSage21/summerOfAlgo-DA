class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        a_real = a.split('+')[0]
        a_imag = a.split('+')[1].replace('i','')
        b_real = b.split('+')[0]
        b_imag = b.split('+')[1].replace('i','')
        return str((int(a_real)*int(b_real)) - (int(a_imag)*int(b_imag))) + "+" + str((int(a_real)*int(b_imag)) + (int(b_real)*int(a_imag))) +  "i"