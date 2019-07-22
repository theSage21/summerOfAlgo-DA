class Solution:
    def complexNumberMultiply(self,a:str,b:str)-> str:
        a = a.replace('i','j')
        b= b.replace('i','j')
        if '+-' in a:
            a=a.replace('+','')
        if "+-" in b:
            b=b.replace('+',"")
        a = complex(a)
        b = complex(b)
        real = int((a.real*b.real) + (a.imag * b.imag * -1))
        imaginary = int((a.real * b.imag) + (a.imag * b.real))
        result = str(real) +"+"+str(imaginary)+"i"
        return result
