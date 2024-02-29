import random

def gen(n):
    hash = random.getrandbits(n)
    return (bin(hash)[2:]).zfill(n)


def xor(a, b):

	result = []


	for i in range(1, len(b)):
		if a[i] == b[i]:
			result.append('0')
		else:
			result.append('1')

	return ''.join(result)

def flip_binary_digits(binary_string, flip_count):
  
  list_binary = list(binary_string)
  flipped_indices = random.sample(range(len(binary_string)), flip_count)
  for index in flipped_indices:
    if list_binary[index] == '0':
      list_binary[index] = '1'
    else:
      list_binary[index] = '0'
  return ''.join(list_binary)


def mod2div(dividend, divisor):

	pick = len(divisor)
	
	tmp = dividend[0: pick]

	while pick < len(dividend):

		if tmp[0] == '1':
			
			tmp = xor(divisor, tmp) + dividend[pick]

		else:

			tmp = xor('0'*pick, tmp) + dividend[pick]

		pick += 1

	if tmp[0] == '1':
		tmp = xor(divisor, tmp)
	else:
		tmp = xor('0'*pick, tmp)

	checkword = tmp
	return checkword


def encodeData(data, key):

	l_key = len(key)

	appended_data = data + '0'*(l_key-1)
	remainder = mod2div(appended_data, key)
	codeword = data + remainder
	return codeword, remainder





n = int(input("Enter n-bit: "))
data = gen(n)
key = input("Enter key value: ")
codeword, remainder = encodeData(data, key)
print("Original data: ",data)
print(f"{codeword} crc value and {remainder} remainder")


flip_count = int(input("Enter number of digits to flip: "))
error_st = flip_binary_digits(codeword, flip_count)

print("Fliped String: ",error_st)


new_crc,remi = encodeData(error_st, key)


print("At Recevier side")
rem = mod2div(error_st,key)
print(f"{new_crc} crc value and {rem} remainder")



