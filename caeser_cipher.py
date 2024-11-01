def encode(string,k):
    encoded_string=""
    for i in input_string:
        letter=ord(i)
        letter+=k
        encoded_string+=chr(letter)
    return encoded_string

def decode(string,k):
    decoded_string=""
    for i in string:
        letter=ord(i)
        letter-=k
        decoded_string+=chr(letter)
    return decoded_string

input_string=input("Enter the string:");
k=int(input("Enter the k value:"))
encrypt=encode(input_string,k)
print("Encoded string:",encrypt)
decrypt=decode(encrypt,k)
print("Decoded string:",decrypt)
