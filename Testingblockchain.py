import hashlib
import datetime
#from flask import Flask

class JetkingBlockchain:

    def __init__(self, previous_block_hash, transaction_list):

        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = "\n".join(transaction_list) + "\n" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()
        self.block_timestamp = str(datetime.datetime.now())        

first_transaction = "\t\tBabu sends 5 BTC to Manoj"
second_transaction = "\t\tManoj sends 2 BTC to Shubankar Das"
print()
third_transaction = "\t\tShubankar Das sends 1.5 BTC to Albin Benny"
fourth_transaction = "\t\tAlbin Benny sends 3.5 BTC to Roushan"
print()
fifth_transaction = "\t\tRoushan sends 6 BTC to Babu"
sixth_transaction = "\t\tShaastri sends 10 BTC to Shubankar Das"

first_block_information = JetkingBlockchain("****************************Transactions List******************************",[first_transaction,second_transaction])
print("***************For the First Block in Blockchain we don't have any previous Block hash******************") 
print("**********************The data of the first Block is**************************\n",first_block_information.block_data)
print()
print("**********************The hash of the first Block data is**************************\n",first_block_information.block_hash)
print()
print("*****************The timestamp of the first block created is***************")
print("\t\t",first_block_information.block_timestamp)
print()
print("****************The Previous Block hash and the transactions of second block is*************\n")

second_block_information = JetkingBlockchain(first_block_information.block_hash, [third_transaction,fourth_transaction])
print()
print("**********************The data of the second Block is**************************\n",second_block_information.block_data)
print()
print("****************************Transactions List******************************\n")
print("**********************The hash of the second Block is**************************\n",second_block_information.block_hash)
print()
print("*******************The timestamp of the first block created is****************")
print("\t\t",second_block_information.block_timestamp)
print()
print("****************The Previous Block hash and the transactions of third block is*************\n")
third_block_information = JetkingBlockchain(second_block_information.block_hash, [fifth_transaction,sixth_transaction])
print()
print("**********************The data of the third Block is**************************\n",third_block_information.block_data)
print()
print("****************************Transactions List******************************\n")
print("**********************The hash of the third Block is**************************\n",third_block_information.block_hash)
print()
print("*******************The timestamp of the first block created is****************")
print("\t\t",third_block_information.block_timestamp)
print()