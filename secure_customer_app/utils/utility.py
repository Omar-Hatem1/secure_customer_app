import frappe
import subprocess
import os
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
import base64

def generate_keys(doc_name):
    app_path = frappe.get_app_path('secure_customer_app')
    dir_name = doc_name.replace(' ', '_').lower()
    path = f'{app_path}/keys'
    dir_path = f"{path}/{dir_name}"
    
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    
    # Generate private key
    subprocess.run(['openssl', 'ecparam', '-name', 'secp256k1', '-genkey', '-noout', '-out', 'PrivateKey.pem'], cwd=dir_path)

    # Generate public key from private key
    subprocess.run(['openssl', 'ec', '-in', 'PrivateKey.pem', '-pubout', '-out', 'publickey.pem'], cwd=dir_path)

    return f'{dir_path}/publickey.pem', f'{dir_path}/PrivateKey.pem'

def encrypt_message(doc_name, customer_name, customer_group, customer_territory):
    public_key_path, private_key_path = generate_keys(doc_name)
    
    # Load public key
    with open(public_key_path, "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read()
        )
    
    # Combine fields into a single string
    message = f"{customer_name}|{customer_group}|{customer_territory}"
    
    # Encrypt the message
    encrypted_message = public_key.encrypt(
        message.encode('utf-8'),
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
    )
    
    # Encode the encrypted message as base64 for storage
    encrypted_token = base64.b64encode(encrypted_message).decode('utf-8')
    
    return encrypted_token