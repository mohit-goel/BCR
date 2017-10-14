import nacl.encoding
import nacl.signing
import nacl.exceptions
import pickle
class Crypto:
    
    
    def getSignedKey(self):
        signing_key = nacl.signing.SigningKey.generate()
        verify_key = signing_key.verify_key
        verify_key_hex = verify_key.encode(encoder=nacl.encoding.HexEncoder)
        sign_key_hex = signing_key.encode(encoder=nacl.encoding.HexEncoder)
        return (sign_key_hex,verify_key_hex)
    
    def sign(self,privateHex,content):
        signingKey = nacl.signing.SigningKey(privateHex, encoder=nacl.encoding.HexEncoder)
        return signingKey.sign(content)
        
    
    def isSignatureVerified(self,verify_key_hex,signed):
        verify_key = nacl.signing.VerifyKey(verify_key_hex, encoder=nacl.encoding.HexEncoder)
        
        # Check the validity of a message's signature
        # Will raise nacl.exceptions.BadSignatureError if the signature check fails
        try:
            verify_key.verify(signed)
        except:
            return False
        
        return True
    
    if __name__ == "__main__":
        signing_key = nacl.signing.SigningKey.generate()
        orderSt = ",".join([str(1),'put',str(3)])
        print(orderSt)
        
        #signing_key2 = nacl.signing.SigningKey.generate()

# Sign a message with the signing key
        signedOrderStatement = signing_key.sign(orderSt.encode())
        
        serializedOrderProof = pickle.dumps(signedOrderStatement)
        
        orderProof = pickle.loads(serializedOrderProof)
        

# Obtain the verify key for a given signing key
        verify_key = signing_key.verify_key

# Serialize the verify key to send it to a third party
        verify_key_hex = verify_key.encode(encoder=nacl.encoding.HexEncoder)

        #orderSt = slot,operationName,operationId
        #hexencoder = nacl.encoding.HexEncoder()
        verify_key = nacl.signing.VerifyKey(verify_key_hex, encoder=nacl.encoding.HexEncoder)

# Check the validity of a message's signature
# Will raise nacl.exceptions.BadSignatureError if the signature check fails
        print('hbefdhuvbh')
        verify_key.verify(orderProof)
        print('hbefdhuhvgrbvhhhhvbh')
            
    
    
        