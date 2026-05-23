# Hash Info

> Advanced Hash Identifier detect 100+ hash algorithms instantly from the command line.

---

## Features

- Identifies **100+ hash algorithms** — MD5, SHA family, NTLM, Whirlpool, Tiger, RipeMD, Haval, and more
- **Color-coded output** for quick reading
- **Batch mode** — process a whole file of hashes at once
- Single hash via CLI argument or interactive prompt
- Shows hash **bit-length** automatically
- `--no-color` flag for clean piped/logged output
- Lightweight — zero dependencies, pure Python 3

---

## Usage

```bash
# Interactive mode
python hash-info.py

# Single hash
python hash-info.py 5f4dcc3b5aa765d61d8327deb882cf99

# Batch mode (one hash per line)
python hash-info.py --file hashes.txt

# No color output (for piping/logging)
python hash-info.py --no-color 5f4dcc3b5aa765d61d8327deb882cf99

# Help
python hash-info.py --help
```

---

## Example Output

```
  Hash  : 5f4dcc3b5aa765d61d8327deb882cf99  [128 bits]
  Length: 32 characters

  ✔  Most Likely:
     [+] MD5
     [+] Domain Cached Credentials (MD4)

     Also Possible:
     [-] NTLM
     [-] MD4
     [-] RipeMD-128
     ...
```

---

## Supported Algorithms

| Category     | Algorithms                                              |
|--------------|---------------------------------------------------------|
| MD family    | MD2, MD4, MD5, MD5-HMAC, MD5 variants                  |
| SHA family   | SHA-1, SHA-224, SHA-256, SHA-384, SHA-512 + HMAC        |
| RipeMD       | RipeMD-128, 160, 256, 320 + HMAC                        |
| Tiger        | Tiger-128, 160, 192 + HMAC                              |
| Haval        | Haval-128, 160, 192, 224, 256 + HMAC                    |
| CRC / Checksum | CRC-16, CRC-32, ADLER-32, FCS-16, XOR-32              |
| Other        | NTLM, Whirlpool, GOST, SNEFRU, DES, SAM, MySQL, bcrypt |
| CMS / Framework | Joomla, Wordpress, phpBB3, Django, MaNGOS            |

---

## Installation

No installation needed. Just clone and run:

```bash
git clone https://github.com/laxdip/hash-info.git
cd hash-info
python hash-info.py
```

Requires **Python 3.x** — no external libraries.

---

## Author

**Prasad**

---

## License

MIT License
