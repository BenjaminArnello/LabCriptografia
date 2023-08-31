from scapy.all import *
from collections import Counter
import string
from termcolor import colored

# Definir el set de probabilidades por letra en español
letter_probabilities = {
    'a': 0.125, 'b': 0.022, 'c': 0.045, 'd': 0.050, 'e': 0.127, 'f': 0.010, 'g': 0.015,
    'h': 0.007, 'i': 0.060, 'j': 0.003, 'k': 0.0004, 'l': 0.050, 'm': 0.031, 'n': 0.067,
    'ñ': 0.003, 'o': 0.086, 'p': 0.022, 'q': 0.008, 'r': 0.068, 's': 0.079, 't': 0.046,
    'u': 0.030, 'v': 0.010, 'w': 0.001, 'x': 0.002, 'y': 0.010, 'z': 0.005
}

def decrypt_cesar(message, shift):
    decrypted = ''
    for char in message:
        if char.isalpha():
            shifted_index = (ord(char.lower()) - ord('a') - shift) % 26
            decrypted += chr(shifted_index + ord('a'))
        else:
            decrypted += char
    return decrypted

def main():
    # Obtener el nombre del archivo pcapng como argumento
    import sys
    if len(sys.argv) != 2:
        print("Usage: python script.py <pcapng_file>")
        return
    pcap_file = sys.argv[1]

    packets = rdpcap(pcap_file)
    extracted_chars = []

    for packet in packets:
        if ICMP in packet:
            icmp_packet = packet[ICMP]
            if Raw in icmp_packet:
                payload = icmp_packet[Raw].load
                if payload:
                    first_byte = payload[0]
                    extracted_chars.append(chr(first_byte))

    extracted_message = ''.join(extracted_chars)
    print("Extracted Message:", extracted_message)

    best_decrypted_message = ""
    best_score = 0

    for shift in range(1, 27):
        decrypted_message = decrypt_cesar(extracted_message, shift)
        score = sum(letter_probabilities.get(char, 0) for char in decrypted_message)
        if score > best_score:
            best_score = score
            best_decrypted_message = decrypted_message

    print("\nDecryption Attempts:")

    for shift in range(1, 27):
        decrypted_message = decrypt_cesar(extracted_message, shift)
        score = sum(letter_probabilities.get(char, 0) for char in decrypted_message)
        if decrypted_message == best_decrypted_message:
            print(colored(f"Shift {shift:2}: {decrypted_message}", "green"))
        else:
            print(f"Shift {shift:2}: {decrypted_message}")

if __name__ == "__main__":
    main()




