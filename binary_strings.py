#Generate all the binary strings with n bits. Assume A[0..n-1] is an array of sie n.
def appendAtFront(x, L):
    return [x + element for element in L]

def bitStrings(n):
    if n == 0: return []
    if n == 1: return['0','1']
    else:
        return (appendAtFront('0',bitStrings(n-1)+appendAtFront('1', bitStrings(n-1))))

bitStrings(4)