from web3 import Web3
import os

# Connect to Ethereum network (using Infura or other service)
infura_url = os.getenv('INFURA_URL')  # Add your Infura project URL or use a local node
w3 = Web3(Web3.HTTPProvider(infura_url))

# Check if connected to Ethereum
if not w3.isConnected():
    raise Exception("Failed to connect to the Ethereum network")

# Function to get wallet balance (ETH)
def get_balance(address):
    """
    Get the balance of an Ethereum address.
    :param address: Ethereum address (string)
    :return: Balance in Ether (float)
    """
    balance_wei = w3.eth.get_balance(address)
    balance_ether = w3.fromWei(balance_wei, 'ether')  # Convert Wei to Ether
    return balance_ether

# Function to send a transaction (ETH)
def send_transaction(from_address, private_key, to_address, amount_in_ether):
    """
    Send a transaction from one Ethereum address to another.
    :param from_address: Address sending the transaction (string)
    :param private_key: Private key of the sender (string)
    :param to_address: Address receiving the transaction (string)
    :param amount_in_ether: Amount of Ether to send (float)
    :return: Transaction hash (string)
    """
    # Prepare the transaction
    nonce = w3.eth.getTransactionCount(from_address)  # Get the number of transactions sent
    gas_price = w3.eth.gas_price  # Get the current gas price
    gas_limit = 21000  # Standard gas limit for a simple transfer

    # Create transaction dictionary
    transaction = {
        'to': to_address,
        'value': w3.toWei(amount_in_ether, 'ether'),  # Convert Ether to Wei
        'gas': gas_limit,
        'gasPrice': gas_price,
        'nonce': nonce,
        'chainId': 1  # 1 for mainnet, use the correct chain ID for the network you're on
    }

    # Sign the transaction
    signed_txn = w3.eth.account.sign_transaction(transaction, private_key)

    # Send the transaction
    txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)

    return txn_hash.hex()

# Function to check if a transaction was successful
def check_transaction_status(txn_hash):
    """
    Check the status of a transaction.
    :param txn_hash: Transaction hash (string)
    :return: Transaction receipt
    """
    receipt = w3.eth.getTransactionReceipt(txn_hash)
    if receipt is None:
        return "Pending"
    elif receipt['status'] == 1:
        return "Success"
    else:
        return "Failed"

# Example usage
if __name__ == '__main__':
    # Sample Ethereum address (replace with actual addresses)
    from_address = "0xYourAddressHere"
    to_address = "0xRecipientAddressHere"
    private_key = "your_private_key_here"  # Be careful with private keys!
    
    # Get balance
    balance = get_balance(from_address)
    print(f"Balance of {from_address}: {balance} ETH")
    
    # Send a transaction (uncomment to execute)
    # txn_hash = send_transaction(from_address, private_key, to_address, 0.01)
    # print(f"Transaction sent! Hash: {txn_hash}")

    # Check the status of a transaction (if you have a txn_hash)
    # status = check_transaction_status(txn_hash)
    # print(f"Transaction Status: {status}")
