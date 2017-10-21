import nacl.encoding
import nacl.signing
import nacl.exceptions
import pickle
import nacl.hash
from nacl.bindings.utils import sodium_memcmp
class Crypto:
    
    def __init__(self):
        self.HASHER = nacl.hash.sha256
   
    
    
    
    def getSignedKey(self):
        signing_key = nacl.signing.SigningKey.generate()
        verify_key = signing_key.verify_key
        #verify_key_hex = verify_key.encode(encoder=nacl.encoding.HexEncoder)
        #sign_key_hex = signing_key.encode(encoder=nacl.encoding.HexEncoder)
        return (signing_key,verify_key)
    
    def sign(self,privateKey,content):
        #signingKey = nacl.signing.SigningKey(privateHex, encoder=nacl.encoding.HexEncoder)
        serializedContent = pickle.dumps(content)
        return privateKey.sign(serializedContent)
        
    def eq_chk(self,dgs0,dgs1):
        if sodium_memcmp(dgs0, dgs1):
            return True
        return False
    
    def isSignatureVerified(self,verify_key,signedStatement):
        #verify_key = nacl.signing.VerifyKey(verify_key_hex, encoder=nacl.encoding.HexEncoder)
        
        # Check the validity of a message's signature
        # Will raise nacl.exceptions.BadSignatureError if the signature check fails
        message = None
        try:
            message = verify_key.verify(signedStatement)
            return pickle.loads(message)
        except:
            return message
        
    def getHash(self,content):
        serializedContent = pickle.dumps(content)
        digest = self.HASHER(serializedContent, encoder=nacl.encoding.HexEncoder)
        return digest
    
    def verifyHashes(self,content,digest):
        contentDigest = self.getHash(content)
        return self.eq_chk(contentDigest,digest)
        
        