input = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''
output = ''

for char in input:
    if ord(char) in range(ord('a'), ord('z')+1):
        newchar = chr((ord(char) - ord('a') +2)%26 + ord('a'))
    else:
        newchar = char
    output = output + newchar
print output
