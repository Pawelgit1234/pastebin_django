import hashlib


def generate_hash(input_string: str) -> str:
	input_bytes = input_string.encode('utf-8')
	hash_object = hashlib.sha256(input_bytes)
	return hash_object.hexdigest()