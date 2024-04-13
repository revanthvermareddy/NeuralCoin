"""
Simple Neural Coin Block for understanding the blockchain
"""

import hashlib
from typing import List


class NeuralCoinBlock:
    
    def __init__(self, previous_block_hash: str, transaction_list: List[str]) -> None:
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list
        
        self.block_data = "-".join(transaction_list) + "-" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()


t1 = "Revanth sent 10 NC to Ivan"
t2 = "Anna sent 2.1 NC to Mike"
t3 = "Chris sent 3.5 NC to Rob"
t4 = "Jane sent 4 NC to John"
t5 = "Kaizen sent 5 NC to Kennedy"
t6 = "Aron sent 3.8 NC to William"


initial_block = NeuralCoinBlock("Initial String", [t1, t2])

print(initial_block.block_data)
print(initial_block.block_hash)

second_block = NeuralCoinBlock(initial_block.block_hash, [t3, t4])

print(second_block.block_data)
print(second_block.block_hash)


third_block = NeuralCoinBlock(second_block.block_hash, [t5, t6])

print(third_block.block_data)
print(third_block.block_hash)
