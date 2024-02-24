Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import hashlib
... import datetime
... 
... class Block:
...     def __init__(self, index, timestamp, data, previous_hash):
...         self.index = index
...         self.timestamp = timestamp
...         self.data = data
...         self.previous_hash = previous_hash
...         self.hash = self.calculate_hash()
... 
...     def calculate_hash(self):
...         hash_string = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)
...         return hashlib.sha256(hash_string.encode()).hexdigest()
... 
... class Blockchain:
...     def __init__(self):
...         self.chain = [self.create_genesis_block()]
... 
...     def create_genesis_block(self):
...         return Block(0, datetime.datetime.now(), "Genesis Block", "0")
... 
...     def get_latest_block(self):
...         return self.chain[-1]
... 
...     def add_block(self, new_block):
...         new_block.previous_hash = self.get_latest_block().hash
...         new_block.hash = new_block.calculate_hash()
...         self.chain.append(new_block)
... 
... def main():
...     fic_blockchain = Blockchain()
...     initial_tokens = 9_000_000_000  # 9 billion tokens
...     # Add initial tokens to the genesis block
...     fic_blockchain.chain[0].data = f"Initial Tokens: {initial_tokens} FIC"
... 
    # Example: Add a new block to the blockchain
    new_block_data = "Transaction data..."
    new_block = Block(fic_blockchain.get_latest_block().index + 1, datetime.datetime.now(), new_block_data, "")
    fic_blockchain.add_block(new_block)

if __name__ == "__main__":
    main()
