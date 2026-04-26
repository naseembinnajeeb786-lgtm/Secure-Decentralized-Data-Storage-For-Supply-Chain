# 🔗 Secure Decentralized Data Storage for Supply Chain

<div align="center">

![Python](https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python&logoColor=white)
![SHA-256](https://img.shields.io/badge/SHA--256-Hashing-green?style=for-the-badge&logo=hashnode&logoColor=white)
![Blockchain](https://img.shields.io/badge/Blockchain-Simulation-orange?style=for-the-badge)
![Cloud Computing](https://img.shields.io/badge/Cloud-Computing-lightblue?style=for-the-badge&logo=icloud&logoColor=white)
![IBM](https://img.shields.io/badge/IBM-TCS-blue?style=for-the-badge&logo=ibm&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

**A Python-based Blockchain Ledger Simulation for Supply Chain using SHA-256 Hashing**

*Demonstrating the Immutable Ledger concept — tamper one block and the entire chain breaks.*

</div>

---

## 👤 Author

| Field | Details |
|-------|---------|
| **Full Name** | KC Muhamed Naseem Bin Najeeb |
| **GitHub Username** | [naseembinnajeeb786-lgtm](https://github.com/naseembinnajeeb786-lgtm/Secure-Decentralized-Data-Storage-For-Supply-Chain) |
| **Project Type** | Individual Project |
| **Institution** | Yenepoya Deemed To Be University |
| **Programme** | BCA (AI, Cloud Computing & DevOps) with IBM & TCS |
| **Semester** | VI Semester |
| **Subject** | AI, Cloud Computing & DevOps |
| **Register Number** | 23BCAICD043 |
| **Project ID** | PRJN26-090 |
| **Project Name** | Secure Decentralized Data Storage for Supply Chain |

---

## 📌 Project Overview

This project simulates a **Blockchain Ledger** for a Supply Chain system using Python and SHA-256 cryptographic hashing. Each supply chain event — from raw material sourcing to final delivery — is stored as a block in a tamper-proof chain.

> **Core Concept:** Blockchain is a chain of hashes. Each block contains the hash of the previous block. If anyone changes a historical record, the hash breaks — and the entire chain becomes invalid. This proves the **Immutable Ledger** concept.

---

## 🧠 What This Project Does

```
Raw Materials  →  Manufacturing  →  Warehouse  →  Delivered to Retailer
   (Chennai)      (Coimbatore)     (Bangalore)         (Mumbai)
     Block 1         Block 2          Block 3            Block 4
```

1. **Builds** a blockchain with 5 blocks (Genesis + 4 supply chain events)
2. **Secures** each block with a SHA-256 cryptographic hash
3. **Links** each block to the previous block using its hash
4. **Validates** the entire chain using `is_valid()`
5. **Detects** tampering — change one block and the chain breaks instantly

---

## 🛠️ Tech Stack

| Technology | Version | Purpose |
|------------|---------|---------|
| Python | 3.14 | Core programming language |
| `hashlib` | Built-in | SHA-256 hashing algorithm |
| `datetime` | Built-in | Timestamps for each block |
| VS Code | Latest | Code editor and terminal |

> ✅ **Zero external dependencies** — no `pip install` required. Everything uses Python built-in libraries.

---

## 📁 Project Structure

```
supply_chain/
│
├── blockchain.py        # Main Python file — blockchain logic
├── index.html           # Project website (interactive demo)
├── README.md            # This file
│
└── .vscode/
    └── launch.json      # VS Code debug configuration
```

---

## 🚀 How to Run

### Prerequisites
- Python 3.10 or higher → [Download Python](https://python.org)
- VS Code → [Download VS Code](https://code.visualstudio.com)

### Steps

**1. Clone the repository**
```bash
git clone https://github.com/NaseemNajeeb/supply-chain-blockchain.git
cd supply-chain-blockchain
```

**2. Run the program**
```bash
python blockchain.py
```

**3. Open the website**
```
Double-click index.html — opens in your browser (no server needed)
```

---

## 💻 Code Structure

### Block Class
```python
class Block:
    def __init__(self, index, data, previous_hash):
        self.index         = index
        self.timestamp     = str(datetime.datetime.now())
        self.data          = data
        self.previous_hash = previous_hash
        self.hash          = self.calculate_hash()   # auto SHA-256

    def calculate_hash(self):
        text = str(self.index) + self.timestamp + str(self.data) + self.previous_hash
        return hashlib.sha256(text.encode()).hexdigest()
```

### Blockchain Class
```python
class Blockchain:
    def __init__(self):
        self.chain = [Block(0, "Genesis Block - Supply Chain Start", "0")]

    def add_block(self, data):
        prev = self.chain[-1]
        self.chain.append(Block(len(self.chain), data, prev.hash))

    def is_valid(self):
        for i in range(1, len(self.chain)):
            curr = self.chain[i]
            prev = self.chain[i - 1]
            if curr.hash != curr.calculate_hash(): return False
            if curr.previous_hash != prev.hash:    return False
        return True
```

---

## 📤 Program Output

### ✅ Before Tampering
```
========== SUPPLY CHAIN BLOCKCHAIN ==========

  Block Number  : 0
  Data          : Genesis Block - Supply Chain Start
  Previous Hash : 0...
  Current Hash  : 3a9f71cd82bb4e8af2c19d7e...

  Block Number  : 1
  Data          : {'event': 'Raw Materials Sourced', 'location': 'Chennai', 'qty': 500}
  Current Hash  : f7bc291e04d2aa918c3e56b1...

  Block Number  : 2
  Data          : {'event': 'Manufacturing Complete', 'location': 'Coimbatore', 'qty': 480}
  Current Hash  : 8dce55a20f3118b74a1f92e7...

  Block Number  : 3
  Data          : {'event': 'Warehouse Stored', 'location': 'Bangalore', 'qty': 480}
  Current Hash  : 2e41f8c7b0a99de37f5c28a1...

  Block Number  : 4
  Data          : {'event': 'Delivered to Retailer', 'location': 'Mumbai', 'qty': 475}
  Current Hash  : 9bc04e61d77f5a283e8d91c2...

✅ Is blockchain valid? True
```

### ❌ After Tampering Block 2
```
========== TAMPERING WITH BLOCK 2 ==========
Hacker changes qty from 480 → 200 in Block 2...

❌ Is blockchain valid after tampering? False

--- Checking each block ---
  Block 1: OK
  Block 2: HASH MISMATCH  ← data was tampered here!
  Block 3: BROKEN LINK   ← chain broken because of above
  Block 4: BROKEN LINK   ← chain broken because of above
```

---

## 🔐 How SHA-256 Hashing Works

```
Block Data + Timestamp + Index + Previous Hash
                    ↓
             SHA-256 Function
                    ↓
    64-character unique fingerprint
  (e.g., 3a9f71cd82bb4e8af2c19d7e3b50a1c2...)
```

**Key Properties:**
- Same input → always same output
- Change **one letter** → completely different hash
- Cannot be reversed — one-way function
- Used in **Bitcoin** and **Ethereum** blockchains

---

## 🔗 Blockchain Chain Diagram

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Block 0   │     │   Block 1   │     │   Block 2   │     │   Block 3   │     │   Block 4   │
│   Genesis   │────▶│ Raw Matrl.  │────▶│ Manufactur. │────▶│  Warehouse  │────▶│  Delivered  │
│             │     │   Chennai   │     │ Coimbatore  │     │  Bangalore  │     │   Mumbai    │
│prev: 0000   │     │prev: 3a9f.. │     │prev: f7bc.. │     │prev: 8dce.. │     │prev: 2e41.. │
│hash: 3a9f.. │     │hash: f7bc.. │     │hash: 8dce.. │     │hash: 2e41.. │     │hash: 9bc0.. │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
```

---

## 🌐 Project Website

The project includes an interactive website (`index.html`) with:

- 🔗 **Visual blockchain diagram** — all 5 blocks displayed with hashes
- 💻 **Live demo output** — before and after tampering side-by-side
- 📝 **Source code viewer** — 3 tabs: Block Class, Blockchain Class, Tamper Demo
- 🎨 **Dark tech theme** — professional IBM-inspired design

**To open:** Double-click `index.html` — no server or internet required.

---

## 📚 Key Concepts Demonstrated

| Concept | Description |
|---------|-------------|
| **Blockchain** | A chain of records where each block is cryptographically linked to the previous one |
| **SHA-256** | A one-way cryptographic hash function producing a unique 64-character fingerprint |
| **Immutable Ledger** | Once data is recorded, it cannot be changed without breaking the chain |
| **Tamper Detection** | `is_valid()` re-computes every hash and checks every link — detects any change |
| **Avalanche Effect** | Changing one character in input completely changes the SHA-256 output |
| **Genesis Block** | The first block — has no previous block so `previous_hash = "0"` |
| **Decentralized Trust** | Anyone can run `is_valid()` to verify the chain — no trusted third party needed |
| **Cloud Computing** | In production, each blockchain node would run on cloud infrastructure (IBM / AWS / Azure) |

---

## 📄 Documentation

| Document | Description |
|----------|-------------|
| `README.md` | This file — project overview and setup guide |
| `HLD_Blockchain_Supply_Chain_IBM.pdf` | High Level Design — IBM format |
| `LLD_Blockchain_Supply_Chain.pdf` | Low Level Design — detailed technical spec |
| `Blockchain_Supply_Chain_Project.pdf` | Complete project report |

---

## 🎓 Academic Details

```
Institution  :  Yenepoya Deemed To Be University
Programme    :  BCA (AI, Cloud Computing & DevOps) with IBM & TCS
Semester     :  VI Semester
Subject      :  Cloud Computing
Project Type :  Individual Project
Academic Year:  2025 – 2026
```

---

## 📜 License

```
MIT License

Copyright (c) 2026 KC Muhamed Naseem Bin Najeeb

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software.
```

---

## 🤝 Acknowledgements

- **Yenepoya Deemed To Be University** — for providing the academic framework
- **IBM & TCS** — for the industry-aligned Cloud Computing curriculum
- **Python Software Foundation** — for the hashlib and datetime libraries
- **Satoshi Nakamoto** — Bitcoin whitepaper, the original blockchain concept

---

<div align="center">

**Made with ❤️ by KC Muhamed Naseem Bin Najeeb**

*BCA (AI, Cloud Computing & DevOps) with IBM & TCS — VI Semester*

*Yenepoya Deemed To Be University*

⭐ **If you found this project helpful, please give it a star!** ⭐

</div>
