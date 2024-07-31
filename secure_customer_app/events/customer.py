from secure_customer_app.secure_customer_app.utils.utility import encrypt_message

def before_save(doc, method):
    # Extract the necessary fields
    customer_name = doc.customer_name
    customer_group = doc.customer_group
    customer_territory = doc.territory
    
    # Encrypt the combined fields
    encrypted_token = encrypt_message(doc.name, customer_name, customer_group, customer_territory)
    
    # Save the encrypted token in a custom field
    doc.custom_token = encrypted_token
