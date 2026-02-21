# verification.py: Basic hashing for prediction integrity
import hashlib

def hash_prediction(pred):
    return hashlib.sha256(str(pred).encode()).hexdigest()