"""
Simple Miner Script to understand the miner process
"""

import hashlib

NONCE_LIMIT = 1000000000000
zeroes_count = 4

def mine(block_number, transactions, previous_hash):
    for nonce in range(NONCE_LIMIT):
        base_text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = hashlib.sha256(base_text.encode()).hexdigest()
        if new_hash.startswith('0' * zeroes_count):
            print(f'Found Hash with nonce: {nonce}')
            return new_hash
    return -1


if __name__ == '__main__':
    block_number = 1
    transactions = "7676266q366dh3778"
    previous_hash = "hdi2g8fg834g888"
    new_hash = mine(block_number, transactions, previous_hash)
    
    # testing
    nonce_found = 75853
    base_text = str(block_number) + transactions + previous_hash + str(nonce_found)
    new_hash = hashlib.sha256(base_text.encode()).hexdigest()
    print(f'new_hash: {new_hash}')
    
