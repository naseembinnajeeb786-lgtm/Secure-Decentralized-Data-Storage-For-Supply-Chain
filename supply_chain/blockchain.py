import hashlib
import datetime

# ─────────────────────────────────────────
#  BLOCK CLASS  – one record in the chain
# ─────────────────────────────────────────
class Block:
    def __init__(self, index, data, previous_hash):
        self.index         = index
        self.timestamp     = str(datetime.datetime.now())
        self.data          = data
        self.previous_hash = previous_hash
        self.hash          = self.calculate_hash()   # auto-calculate on creation

    def calculate_hash(self):
        # Combine all fields → SHA-256 → 64-character fingerprint
        text = str(self.index) + self.timestamp + str(self.data) + self.previous_hash
        return hashlib.sha256(text.encode()).hexdigest()


# ─────────────────────────────────────────
#  BLOCKCHAIN CLASS  – manages all blocks
# ─────────────────────────────────────────
class Blockchain:
    def __init__(self):
        # First block is always the "Genesis" block
        self.chain = [Block(0, "Genesis Block - Supply Chain Start", "0")]

    def add_block(self, data):
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), data, previous_block.hash)
        self.chain.append(new_block)

    def is_valid(self):
        for i in range(1, len(self.chain)):
            curr = self.chain[i]
            prev = self.chain[i - 1]
            # Check 1: has this block's data been changed?
            if curr.hash != curr.calculate_hash():
                return False
            # Check 2: is this block properly linked to the previous one?
            if curr.previous_hash != prev.hash:
                return False
        return True


# ─────────────────────────────────────────
#  PRINT HELPER
# ─────────────────────────────────────────
def print_chain(chain):
    for block in chain:
        print(f"\n{'='*50}")
        print(f"  Block Number  : {block.index}")
        print(f"  Data          : {block.data}")
        print(f"  Timestamp     : {block.timestamp}")
        print(f"  Previous Hash : {block.previous_hash[:40]}...")
        print(f"  Current Hash  : {block.hash[:40]}...")
    print(f"\n{'='*50}")


# ─────────────────────────────────────────
#  MAIN PROGRAM
# ─────────────────────────────────────────

# Create the blockchain
sc_chain = Blockchain()

# Add supply chain events
sc_chain.add_block({"event": "Raw Materials Sourced",   "location": "Chennai",    "qty": 500})
sc_chain.add_block({"event": "Manufacturing Complete",  "location": "Coimbatore", "qty": 480})
sc_chain.add_block({"event": "Warehouse Stored",        "location": "Bangalore",  "qty": 480})
sc_chain.add_block({"event": "Delivered to Retailer",   "location": "Mumbai",     "qty": 475})

# Print the full chain
print("\n========== SUPPLY CHAIN BLOCKCHAIN ==========")
print_chain(sc_chain.chain)
print(f"\n✅ Is blockchain valid? {sc_chain.is_valid()}")


# ─────────────────────────────────────────
#  TAMPER DEMONSTRATION
# ─────────────────────────────────────────
print("\n\n========== TAMPERING WITH BLOCK 2 ==========")
print("Hacker changes qty from 480 → 200 in Block 2...")

sc_chain.chain[2].data = {"event": "Warehouse Stored", "location": "Bangalore", "qty": 200}

print(f"\n❌ Is blockchain valid after tampering? {sc_chain.is_valid()}")

print("\n--- Checking each block ---")
for i in range(1, len(sc_chain.chain)):
    curr = sc_chain.chain[i]
    prev = sc_chain.chain[i - 1]
    if curr.hash != curr.calculate_hash():
        print(f"  Block {curr.index}: HASH MISMATCH  ← data was tampered here!")
    elif curr.previous_hash != prev.hash:
        print(f"  Block {curr.index}: BROKEN LINK   ← chain broken because of above")
    else:
        print(f"  Block {curr.index}: OK")