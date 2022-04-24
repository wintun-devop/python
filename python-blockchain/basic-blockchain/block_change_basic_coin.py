import hashlib

#create basic blockchain class
class BasicBlockchain:
    def __init__(self,previous_block_hash,transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list
        
        self.block_data="-".join(transaction_list)+"-"+previous_block_hash
        self.block_hash=hashlib.sha256(self.block_data.encode()).hexdigest()

#sample tranasaction list
t1="Yuki send 3 BB to Mike."
t2="Tena send 5 BB to Yoshida."
t3="Yoshida send 6 BB to Mike."
t4="Yuki send 3 BB to Miki."
t5="Miki send 4 BB to Hana."
t6="Yuki send 3 BB to Hayashi."

#create initial block by using basic blockchain pattern
initial_block=BasicBlockchain("initial_string",[t1,t2])
print(initial_block.block_data)
print(initial_block.block_hash)
#create second block by using basic blockchain pattern
second_block=BasicBlockchain(initial_block.block_hash,[t3,t4])
print(second_block.block_data)
print(second_block.block_hash)
##create third block by using basic blockchain pattern
thrid_block=BasicBlockchain(second_block.block_hash,[t5,t6])
print(thrid_block.block_data)
print(thrid_block.block_hash)
