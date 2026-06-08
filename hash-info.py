#!/usr/bin/env python3
# encoding: utf-8
# ============================================================
#   Hash Info - Advanced Hash Identifier
#   By Prasad  |  V2.0
# ============================================================

import sys
import os
import re
import argparse
from builtins import input

version = "2.0"

# ──────────────────────────────────────────────
#  ANSI Color Codes
# ──────────────────────────────────────────────
class C:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    DIM     = "\033[2m"
    RED     = "\033[91m"
    GREEN   = "\033[92m"
    YELLOW  = "\033[93m"
    BLUE    = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN    = "\033[96m"
    WHITE   = "\033[97m"
    GRAY    = "\033[90m"

# Disable colors if output is piped / redirected
if not sys.stdout.isatty():
    for attr in vars(C):
        if not attr.startswith("_"):
            setattr(C, attr, "")

# ──────────────────────────────────────────────
#  Logo
# ──────────────────────────────────────────────
logo = f"""
{C.CYAN}{C.BOLD}
  ██╗  ██╗ █████╗ ███████╗██╗  ██╗    ██╗███╗   ██╗███████╗ ██████╗
  ██║  ██║██╔══██╗██╔════╝██║  ██║    ██║████╗  ██║██╔════╝██╔═══██╗
  ███████║███████║███████╗███████║    ██║██╔██╗ ██║█████╗  ██║   ██║
  ██╔══██║██╔══██║╚════██║██╔══██║    ██║██║╚██╗██║██╔══╝  ██║   ██║
  ██║  ██║██║  ██║███████║██║  ██║    ██║██║ ╚████║██║     ╚██████╔╝
  ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝
{C.RESET}{C.GRAY}  Advanced Hash Identifier  |  v{version}  |  By Prasad{C.RESET}
  {C.DIM}{'─' * 62}{C.RESET}
"""

# ──────────────────────────────────────────────
#  Algorithm Database
# ──────────────────────────────────────────────
algorithms = {
    "102020": "ADLER-32",
    "102040": "CRC-32",
    "102060": "CRC-32B",
    "101020": "CRC-16",
    "101040": "CRC-16-CCITT",
    "104020": "DES (Unix)",
    "101060": "FCS-16",
    "103040": "GHash-32-3",
    "103020": "GHash-32-5",
    "115060": "GOST R 34.11-94",
    "109100": "Haval-160",
    "109200": "Haval-160 (HMAC)",
    "110040": "Haval-192",
    "110080": "Haval-192 (HMAC)",
    "114040": "Haval-224",
    "114080": "Haval-224 (HMAC)",
    "115040": "Haval-256",
    "115140": "Haval-256 (HMAC)",
    "107080": "Lineage II C4",
    "106025": "Domain Cached Credentials (MD4)",
    "102080": "XOR-32",
    "105060": "MD5 (Half)",
    "105040": "MD5 (Middle)",
    "105020": "MySQL v3",
    "107040": "MD5 (phpBB3)",
    "107060": "MD5 (Unix)",
    "107020": "MD5 (Wordpress)",
    "108020": "MD5 (APR)",
    "106160": "Haval-128",
    "106165": "Haval-128 (HMAC)",
    "106060": "MD2",
    "106120": "MD2 (HMAC)",
    "106040": "MD4",
    "106100": "MD4 (HMAC)",
    "106020": "MD5",
    "106080": "MD5 (HMAC)",
    "106140": "MD5 HMAC (Wordpress)",
    "106029": "NTLM",
    "106027": "RAdmin v2.x",
    "106180": "RipeMD-128",
    "106185": "RipeMD-128 (HMAC)",
    "106200": "SNEFRU-128",
    "106205": "SNEFRU-128 (HMAC)",
    "106220": "Tiger-128",
    "106225": "Tiger-128 (HMAC)",
    "106240": "md5($pass.$salt)",
    "106260": "md5($salt.'-'.md5($pass))",
    "106280": "md5($salt.$pass)",
    "106300": "md5($salt.$pass.$salt)",
    "106320": "md5($salt.$pass.$username)",
    "106340": "md5($salt.md5($pass))",
    "106360": "md5($salt.md5($pass).$salt)",
    "106380": "md5($salt.md5($pass.$salt))",
    "106400": "md5($salt.md5($salt.$pass))",
    "106420": "md5($salt.md5(md5($pass).$salt))",
    "106440": "md5($username.0.$pass)",
    "106460": "md5($username.LF.$pass)",
    "106480": "md5($username.md5($pass).$salt)",
    "106500": "md5(md5($pass))",
    "106520": "md5(md5($pass).$salt)",
    "106540": "md5(md5($pass).md5($salt))",
    "106560": "md5(md5($salt).$pass)",
    "106580": "md5(md5($salt).md5($pass))",
    "106600": "md5(md5($username.$pass).$salt)",
    "106620": "md5(md5(md5($pass)))",
    "106640": "md5(md5(md5(md5($pass))))",
    "106660": "md5(md5(md5(md5(md5($pass)))))",
    "106680": "md5(sha1($pass))",
    "106700": "md5(sha1(md5($pass)))",
    "106720": "md5(sha1(md5(sha1($pass))))",
    "106740": "md5(strtoupper(md5($pass)))",
    "109040": "MySQL5 — SHA-1(SHA-1($pass))",
    "109060": "MySQL 160bit — SHA-1(SHA-1($pass))",
    "109180": "RipeMD-160 (HMAC)",
    "109120": "RipeMD-160",
    "109020": "SHA-1",
    "109140": "SHA-1 (HMAC)",
    "109220": "SHA-1 (MaNGOS)",
    "109240": "SHA-1 (MaNGOS2)",
    "109080": "Tiger-160",
    "109160": "Tiger-160 (HMAC)",
    "109260": "sha1($pass.$salt)",
    "109280": "sha1($salt.$pass)",
    "109300": "sha1($salt.md5($pass))",
    "109320": "sha1($salt.md5($pass).$salt)",
    "109340": "sha1($salt.sha1($pass))",
    "109360": "sha1($salt.sha1($salt.sha1($pass)))",
    "109380": "sha1($username.$pass)",
    "109400": "sha1($username.$pass.$salt)",
    "1094202": "sha1(md5($pass))",
    "109440": "sha1(md5($pass).$salt)",
    "109460": "sha1(md5(sha1($pass)))",
    "109480": "sha1(sha1($pass))",
    "109500": "sha1(sha1($pass).$salt)",
    "109520": "sha1(sha1($pass).substr($pass,0,3))",
    "109540": "sha1(sha1($salt.$pass))",
    "109560": "sha1(sha1(sha1($pass)))",
    "109580": "sha1(strtolower($username).$pass)",
    "110020": "Tiger-192",
    "110060": "Tiger-192 (HMAC)",
    "112020": "md5($pass.$salt) — Joomla v1",
    "113020": "SHA-1 (Django)",
    "114020": "SHA-224",
    "114060": "SHA-224 (HMAC)",
    "115080": "RipeMD-256",
    "115160": "RipeMD-256 (HMAC)",
    "115100": "SNEFRU-256",
    "115180": "SNEFRU-256 (HMAC)",
    "115200": "SHA-256(md5($pass))",
    "115220": "SHA-256(sha1($pass))",
    "115020": "SHA-256",
    "115120": "SHA-256 (HMAC)",
    "116020": "md5($pass.$salt) — Joomla v2",
    "116040": "SAM — LM_hash:NT_hash",
    "117020": "SHA-256 (Django)",
    "118020": "RipeMD-320",
    "118040": "RipeMD-320 (HMAC)",
    "119020": "SHA-384",
    "119040": "SHA-384 (HMAC)",
    "120020": "SHA-256 (crypt $6$)",
    "121020": "SHA-384 (Django)",
    "122020": "SHA-512",
    "122060": "SHA-512 (HMAC)",
    "122040": "Whirlpool",
    "122080": "Whirlpool (HMAC)",
}

# ──────────────────────────────────────────────
#  Hash Bit-length hints  (for display)
# ──────────────────────────────────────────────
HASH_BITS = {
    "MD5": 128, "SHA-1": 160, "SHA-224": 224,
    "SHA-256": 256, "SHA-384": 384, "SHA-512": 512,
    "CRC-32": 32, "CRC-16": 16, "NTLM": 128,
    "RipeMD-128": 128, "RipeMD-160": 160,
    "RipeMD-256": 256, "RipeMD-320": 320,
    "Whirlpool": 512, "Tiger-128": 128,
    "Tiger-160": 160, "Tiger-192": 192,
}

# ──────────────────────────────────────────────
#  Detection Functions
# ──────────────────────────────────────────────
jerar = []

def _check(h, example, code, extra=True):
    """Generic check: length + alnum (or custom extra condition)."""
    if len(h) == len(example) and extra:
        jerar.append(code)

def CRC16(h):
    _check(h, '4607', "101020",
           h.isalpha() == False and h.isalnum() == True)
def CRC16CCITT(h):
    _check(h, '3d08', "101040",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def FCS16(h):
    _check(h, '0e5b', "101060",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def CRC32(h):
    _check(h, 'b33fd057', "102040",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def ADLER32(h):
    _check(h, '0607cb42', "102020",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def CRC32B(h):
    _check(h, 'b764a0d9', "102060",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def XOR32(h):
    _check(h, '0000003f', "102080",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def GHash323(h):
    _check(h, '80000000', "103040",
           h.isdigit() == True and h.isalpha() == False and h.isalnum() == True)
def GHash325(h):
    _check(h, '85318985', "103020",
           h.isdigit() == True and h.isalpha() == False and h.isalnum() == True)
def DESUnix(h):
    _check(h, 'ZiY8YtDKXJwYQ', "104020",
           h.isdigit() == False and h.isalpha() == False)
def MD5Half(h):
    _check(h, 'ae11fd697ec92c7c', "105060",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def MD5Middle(h):
    _check(h, '7ec92c7c98de3fac', "105040",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def MySQL(h):
    _check(h, '63cea4673fd25f46', "105020",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def DomainCachedCredentials(h):
    _check(h, 'f42005ec1afe77967cbc83dce1b4d714', "106025",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def Haval128(h):
    _check(h, 'd6e3ec49aa0f138a619f27609022df10', "106160",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def Haval128HMAC(h):
    _check(h, '3ce8b0ffd75bc240fc7d967729cd6637', "106165",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def MD2(h):
    _check(h, '08bbef4754d98806c373f2cd7d9a43c4', "106060",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def MD2HMAC(h):
    _check(h, '4b61b72ead2b0eb0fa3b8a56556a6dca', "106120",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def MD4(h):
    _check(h, 'a2acde400e61410e79dacbdfc3413151', "106040",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def MD4HMAC(h):
    _check(h, '6be20b66f2211fe937294c1c95d1cd4f', "106100",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def MD5(h):
    _check(h, 'ae11fd697ec92c7c98de3fac23aba525', "106020",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def MD5HMAC(h):
    _check(h, 'd57e43d2c7e397bf788f66541d6fdef9', "106080",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def MD5HMACWordpress(h):
    _check(h, '3f47886719268dfa83468630948228f6', "106140",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def NTLM(h):
    _check(h, 'cc348bace876ea440a28ddaeb9fd3550', "106029",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def RAdminv2x(h):
    _check(h, 'baea31c728cbf0cd548476aa687add4b', "106027",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def RipeMD128(h):
    _check(h, '4985351cd74aff0abc5a75a0c8a54115', "106180",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def RipeMD128HMAC(h):
    _check(h, 'ae1995b931cf4cbcf1ac6fbf1a83d1d3', "106185",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def SNEFRU128(h):
    _check(h, '4fb58702b617ac4f7ca87ec77b93da8a', "106200",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def SNEFRU128HMAC(h):
    _check(h, '59b2b9dcc7a9a7d089cecf1b83520350', "106205",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def Tiger128(h):
    _check(h, 'c086184486ec6388ff81ec9f23528727', "106220",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def Tiger128HMAC(h):
    _check(h, 'c87032009e7c4b2ea27eb6f99723454b', "106225",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def md5passsalt(h):
    _check(h, '5634cc3b922578434d6e9342ff5913f7', "106240",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def md5saltmd5pass(h):
    _check(h, '245c5763b95ba42d4b02d44bbcd916f1', "106260",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def md5saltpass(h):
    _check(h, '22cc5ce1a1ef747cd3fa06106c148dfa', "106280",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def md5saltpasssalt(h):
    _check(h, '469e9cdcaff745460595a7a386c4db0c', "106300",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def md5saltpassusername(h):
    _check(h, '9ae20f88189f6e3a62711608ddb6f5fd', "106320",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def md5saltmd5pass2(h):
    _check(h, 'aca2a052962b2564027ee62933d2382f', "106340",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def md5saltmd5passsalt(h):
    _check(h, 'de0237dc03a8efdf6552fbe7788b2fdd', "106360",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def md5saltmd5passsalt2(h):
    _check(h, '5b8b12ca69d3e7b2a3e2308e7bef3e6f', "106380",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def md5saltmd5saltpass(h):
    _check(h, 'd8f3b3f004d387086aae24326b575b23', "106400",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def md5saltmd5md5passsalt(h):
    _check(h, '81f181454e23319779b03d74d062b1a2', "106420",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def md5username0pass(h):
    _check(h, 'e44a60f8f2106492ae16581c91edb3ba', "106440",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def md5usernameLFpass(h):
    _check(h, '654741780db415732eaee12b1b909119', "106460",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def md5usernamemd5passsalt(h):
    _check(h, '954ac5505fd1843bbb97d1b2cda0b98f', "106480",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def md5md5pass(h):
    _check(h, 'a96103d267d024583d5565436e52dfb3', "106500",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def md5md5passsalt(h):
    _check(h, '5848c73c2482d3c2c7b6af134ed8dd89', "106520",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def md5md5passmd5salt(h):
    _check(h, '8dc71ef37197b2edba02d48c30217b32', "106540",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def md5md5saltpass(h):
    _check(h, '9032fabd905e273b9ceb1e124631bd67', "106560",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def md5md5saltmd5pass(h):
    _check(h, '8966f37dbb4aca377a71a9d3d09cd1ac', "106580",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def md5md5usernamepasssalt(h):
    _check(h, '4319a3befce729b34c3105dbc29d0c40', "106600",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def md5md5md5pass(h):
    _check(h, 'ea086739755920e732d0f4d8c1b6ad8d', "106620",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def md5md5md5md5pass(h):
    _check(h, '02528c1f2ed8ac7d83fe76f3cf1c133f', "106640",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def md5md5md5md5md5pass(h):
    _check(h, '4548d2c062933dff53928fd4ae427fc0', "106660",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def md5sha1pass(h):
    _check(h, 'cb4ebaaedfd536d965c452d9569a6b1e', "106680",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def md5sha1md5pass(h):
    _check(h, '099b8a59795e07c334a696a10c0ebce0', "106700",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def md5sha1md5sha1pass(h):
    _check(h, '06e4af76833da7cc138d90602ef80070', "106720",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def md5strtouppermd5pass(h):
    _check(h, '519de146f1a658ab5e5e2aa9b7d2eec8', "106740",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def LineageIIC4(h):
    _check(h, '0x49a57f66bd3d5ba6abda5579c264a0e4', "107080",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True and h[0:2] == '0x')
def MD5phpBB3(h):
    _check(h, '$H$9kyOtE8CDqMJ44yfn9PFz2E.L2oVzL1', "107040",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == False and h[0:3] == '$H$')
def MD5Unix(h):
    _check(h, '$1$cTuJH0Ju$1J8rI.mJReeMvpKUZbSlY/', "107060",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == False and h[0:3] == '$1$')
def MD5Wordpress(h):
    _check(h, '$P$BiTOhOj3ukMgCci2juN0HRbCdDRqeh.', "107020",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == False and h[0:3] == '$P$')
def MD5APR(h):
    _check(h, '$apr1$qAUKoKlG$3LuCncByN76eLxZAh/Ldr1', "108020",
           h.isdigit() == False and h.isalpha() == False and h[0:4] == '$apr')
def Haval160(h):
    _check(h, 'a106e921284dd69dad06192a4411ec32fce83dbb', "109100",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def Haval160HMAC(h):
    _check(h, '29206f83edc1d6c3f680ff11276ec20642881243', "109200",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def MySQL5(h):
    _check(h, '9bb2fb57063821c762cc009f7584ddae9da431ff', "109040",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def MySQL160bit(h):
    _check(h, '*2470c0c06dee42fd1618bb99005adca2ec9d1e19', "109060",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == False and h[0:1] == '*')
def RipeMD160(h):
    _check(h, 'dc65552812c66997ea7320ddfb51f5625d74721b', "109120",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def RipeMD160HMAC(h):
    _check(h, 'ca28af47653b4f21e96c1235984cb50229331359', "109180",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def SHA1(h):
    _check(h, '4a1d4dbc1e193ec3ab2e9213876ceb8f4db72333', "109020",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def SHA1HMAC(h):
    _check(h, '6f5daac3fee96ba1382a09b1ba326ca73dccf9e7', "109140",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def SHA1MaNGOS(h):
    _check(h, 'a2c0cdb6d1ebd1b9f85c6e25e0f8732e88f02f96', "109220",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def SHA1MaNGOS2(h):
    _check(h, '644a29679136e09d0bd99dfd9e8c5be84108b5fd', "109240",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def Tiger160(h):
    _check(h, 'c086184486ec6388ff81ec9f235287270429b225', "109080",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def Tiger160HMAC(h):
    _check(h, '6603161719da5e56e1866e4f61f79496334e6a10', "109160",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def sha1passsalt(h):
    _check(h, 'f006a1863663c21c541c8d600355abfeeaadb5e4', "109260",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def sha1saltpass(h):
    _check(h, '299c3d65a0dcab1fc38421783d64d0ecf4113448', "109280",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def sha1saltmd5pass(h):
    _check(h, '860465ede0625deebb4fbbedcb0db9dc65faec30', "109300",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def sha1saltmd5passsalt(h):
    _check(h, '6716d047c98c25a9c2cc54ee6134c73e6315a0ff', "109320",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def sha1saltsha1pass(h):
    _check(h, '58714327f9407097c64032a2fd5bff3a260cb85f', "109340",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def sha1saltsha1saltsha1pass(h):
    _check(h, 'cc600a2903130c945aa178396910135cc7f93c63', "109360",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def sha1usernamepass(h):
    _check(h, '3de3d8093bf04b8eb5f595bc2da3f37358522c9f', "109380",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def sha1usernamepasssalt(h):
    _check(h, '00025111b3c4d0ac1635558ce2393f77e94770c5', "109400",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def sha1md5pass(h):
    _check(h, 'fa960056c0dea57de94776d3759fb555a15cae87', "1094202",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def sha1md5passsalt(h):
    _check(h, '1dad2b71432d83312e61d25aeb627593295bcc9a', "109440",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def sha1md5sha1pass(h):
    _check(h, '8bceaeed74c17571c15cdb9494e992db3c263695', "109460",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def sha1sha1pass(h):
    _check(h, '3109b810188fcde0900f9907d2ebcaa10277d10e', "109480",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def sha1sha1passsalt(h):
    _check(h, '780d43fa11693b61875321b6b54905ee488d7760', "109500",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def sha1sha1passsubstrpass03(h):
    _check(h, '5ed6bc680b59c580db4a38df307bd4621759324e', "109520",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def sha1sha1saltpass(h):
    _check(h, '70506bac605485b4143ca114cbd4a3580d76a413', "109540",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def sha1sha1sha1pass(h):
    _check(h, '3328ee2a3b4bf41805bd6aab8e894a992fa91549', "109560",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def sha1strtolowerusernamepass(h):
    _check(h, '79f575543061e158c2da3799f999eb7c95261f07', "109580",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def Haval192(h):
    _check(h, 'cd3a90a3bebd3fa6b6797eba5dab8441f16a7dfa96c6e641', "110040",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def Haval192HMAC(h):
    _check(h, '39b4d8ecf70534e2fd86bb04a877d01dbf9387e640366029', "110080",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def Tiger192(h):
    _check(h, 'c086184486ec6388ff81ec9f235287270429b2253b248a70', "110020",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def Tiger192HMAC(h):
    _check(h, '8e914bb64353d4d29ab680e693272d0bd38023afa3943a41', "110060",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def MD5passsaltjoomla1(h):
    _check(h, '35d1c0d69a2df62be2df13b087343dc9:BeKMviAfcXeTPTlX', "112020",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == False and h[32:33] == ':')
def SHA1Django(h):
    _check(h, 'sha1$Prasad$299c3d65a0dcab1fc38421783d64d0ecf4113448', "113020",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == False and h[0:5] == 'sha1$')
def Haval224(h):
    _check(h, 'f65d3c0ef6c56f4c74ea884815414c24dbf0195635b550f47eac651a', "114040",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def Haval224HMAC(h):
    _check(h, 'f10de2518a9f7aed5cf09b455112114d18487f0c894e349c3c76a681', "114080",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def SHA224(h):
    _check(h, 'e301f414993d5ec2bd1d780688d37fe41512f8b57f6923d054ef8e59', "114020",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def SHA224HMAC(h):
    _check(h, 'c15ff86a859892b5e95cdfd50af17d05268824a6c9caaa54e4bf1514', "114060",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def SHA256(h):
    _check(h, '2c740d20dab7f14ec30510a11f8fd78b82bc3a711abe8a993acdb323e78e6d5e', "115020",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def SHA256HMAC(h):
    _check(h, 'd3dd251b7668b8b6c12e639c681e88f2c9b81105ef41caccb25fcde7673a1132', "115120",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def Haval256(h):
    _check(h, '7169ecae19a5cd729f6e9574228b8b3c91699175324e6222dec569d4281d4a4a', "115040",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def Haval256HMAC(h):
    _check(h, '6aa856a2cfd349fb4ee781749d2d92a1ba2d38866e337a4a1db907654d4d4d7a', "115140",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def GOSTR341194(h):
    _check(h, 'ab709d384cce5fda0793becd3da0cb6a926c86a8f3460efb471adddee1c63793', "115060",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def RipeMD256(h):
    _check(h, '5fcbe06df20ce8ee16e92542e591bdea706fbdc2442aecbf42c223f4461a12af', "115080",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def RipeMD256HMAC(h):
    _check(h, '43227322be1b8d743e004c628e0042184f1288f27c13155412f08beeee0e54bf', "115160",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def SNEFRU256(h):
    _check(h, '3a654de48e8d6b669258b2d33fe6fb179356083eed6ff67e27c5ebfa4d9732bb', "115100",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def SNEFRU256HMAC(h):
    _check(h, '4e9418436e301a488f675c9508a2d518d8f8f99e966136f2dd7e308b194d74f9', "115180",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def SHA256md5pass(h):
    _check(h, 'b419557099cfa18a86d1d693e2b3b3e979e7a5aba361d9c4ec585a1a70c7bde4', "115200",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def SHA256sha1pass(h):
    _check(h, 'afbed6e0c79338dbfe0000efe6b8e74e3b7121fe73c383ae22f5b505cb39c886', "115220",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def MD5passsaltjoomla2(h):
    _check(h, 'fb33e01e4f8787dc8beb93dac4107209:fxJUXVjYRafVauT77Cze8XwFrWaeAYB2', "116020",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == False and h[32:33] == ':')
def SAM(h):
    _check(h, '4318B176C3D8E3DEAAD3B435B51404EE:B7C899154197E8A2A33121D76A240AB5', "116040",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == False
           and h.islower() == False and h[32:33] == ':')
def SHA256Django(h):
    _check(h, 'sha256$Prasad$9e1a08aa28a22dfff722fad7517bae68a55444bb5e2f909d340767cec9acf2c3', "117020",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == False and h[0:6] == 'sha256')
def RipeMD320(h):
    _check(h, 'b4f7c8993a389eac4f421b9b3b2bfb3a241d05949324a8dab1286069a18de69aaf5ecc3c2009d8ef', "118020",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def RipeMD320HMAC(h):
    _check(h, '244516688f8ad7dd625836c0d0bfc3a888854f7c0161f01de81351f61e98807dcd55b39ffe5d7a78', "118040",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def SHA384(h):
    _check(h, '3b21c44f8d830fa55ee9328a7713c6aad548fe6d7a4a438723a0da67c48c485220081a2fbc3e8c17fd9bd65f8d4b4e6b', "119020",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def SHA384HMAC(h):
    _check(h, 'bef0dd791e814d28b4115eb6924a10beb53da47d463171fe8e63f68207521a4171219bb91d0580bca37b0f96fddeeb8b', "119040",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def SHA256s(h):
    _check(h, '$6$g4TpUQzk$OmsZBJFwvy6MwZckPvVYfDnwsgktm2CckOlNJGy9HNwHSuHFvywGIuwkJ6Bjn3kKbB6zoyEjIYNMpHWBNxJ6g.', "120020",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == False and h[0:3] == '$6$')
def SHA384Django(h):
    _check(h, 'sha384$Prasad$88cfd5bc332a4af9f09aa33a1593f24eddc01de00b84395765193c3887f4deac46dc723ac14ddeb4d3a9b958816b7bba', "121020",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == False and h[0:6] == 'sha384')
def SHA512(h):
    _check(h, 'ea8e6f0935b34e2e6573b89c0856c81b831ef2cadfdee9f44eb9aa0955155ba5e8dd97f85c73f030666846773c91404fb0e12fb38936c56f8cf38a33ac89a24e', "122020",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def SHA512HMAC(h):
    _check(h, 'dd0ada8693250b31d9f44f3ec2d4a106003a6ce67eaa92e384b356d1b4ef6d66a818d47c1f3a2c6e8a9a9b9bdbd28d485e06161ccd0f528c8bbb5541c3fef36f', "122060",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def Whirlpool(h):
    _check(h, '76df96157e632410998ad7f823d82930f79a96578acc8ac5ce1bfc34346cf64b4610aefa8a549da3f0c1da36dad314927cebf8ca6f3fcd0649d363c5a370dddb', "122040",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)
def WhirlpoolHMAC(h):
    _check(h, '77996016cf6111e97d6ad31484bab1bf7de7b7ee64aebbc243e650a75a2f9256cef104e504d3cf29405888fca5a231fcac85d36cd614b1d52fce850b53ddf7f9', "122080",
           h.isdigit() == False and h.isalpha() == False and h.isalnum() == True)


ALL_CHECKS = [
    ADLER32, CRC16, CRC16CCITT, CRC32, CRC32B, DESUnix, DomainCachedCredentials,
    FCS16, GHash323, GHash325, GOSTR341194, Haval128, Haval128HMAC,
    Haval160, Haval160HMAC, Haval192, Haval192HMAC, Haval224, Haval224HMAC,
    Haval256, Haval256HMAC, LineageIIC4, MD2, MD2HMAC, MD4, MD4HMAC,
    MD5, MD5APR, MD5HMAC, MD5HMACWordpress, MD5phpBB3, MD5Unix, MD5Wordpress,
    MD5Half, MD5Middle, MD5passsaltjoomla1, MD5passsaltjoomla2,
    MySQL, MySQL5, MySQL160bit, NTLM, RAdminv2x,
    RipeMD128, RipeMD128HMAC, RipeMD160, RipeMD160HMAC,
    RipeMD256, RipeMD256HMAC, RipeMD320, RipeMD320HMAC,
    SAM, SHA1, SHA1Django, SHA1HMAC, SHA1MaNGOS, SHA1MaNGOS2,
    SHA224, SHA224HMAC, SHA256, SHA256s, SHA256Django, SHA256HMAC,
    SHA256md5pass, SHA256sha1pass, SHA384, SHA384Django, SHA384HMAC,
    SHA512, SHA512HMAC, SNEFRU128, SNEFRU128HMAC, SNEFRU256, SNEFRU256HMAC,
    Tiger128, Tiger128HMAC, Tiger160, Tiger160HMAC, Tiger192, Tiger192HMAC,
    Whirlpool, WhirlpoolHMAC, XOR32,
    md5passsalt, md5saltmd5pass, md5saltpass, md5saltpasssalt, md5saltpassusername,
    md5saltmd5pass2, md5saltmd5passsalt, md5saltmd5passsalt2, md5saltmd5saltpass,
    md5saltmd5md5passsalt, md5username0pass, md5usernameLFpass,
    md5usernamemd5passsalt, md5md5pass, md5md5passsalt, md5md5passmd5salt,
    md5md5saltpass, md5md5saltmd5pass, md5md5usernamepasssalt,
    md5md5md5pass, md5md5md5md5pass, md5md5md5md5md5pass,
    md5sha1pass, md5sha1md5pass, md5sha1md5sha1pass, md5strtouppermd5pass,
    sha1passsalt, sha1saltpass, sha1saltmd5pass, sha1saltmd5passsalt,
    sha1saltsha1pass, sha1saltsha1saltsha1pass, sha1usernamepass,
    sha1usernamepasssalt, sha1md5pass, sha1md5passsalt, sha1md5sha1pass,
    sha1sha1pass, sha1sha1passsalt, sha1sha1passsubstrpass03,
    sha1sha1saltpass, sha1sha1sha1pass, sha1strtolowerusernamepass,
]

# ──────────────────────────────────────────────
#  Helper: validate & clean hash input
# ──────────────────────────────────────────────
def sanitize(h):
    """Strip whitespace; return None if empty."""
    h = h.strip()
    return h if h else None

def is_valid_hash_chars(h):
    """Rough sanity check — reject obviously non-hash strings."""
    return len(h) >= 4

def get_hash_length_bits(h):
    """Estimate likely bit-size from hex length."""
    # Only meaningful for pure hex hashes
    if re.fullmatch(r'[0-9a-fA-F]+', h):
        return len(h) * 4
    return None

# ──────────────────────────────────────────────
#  Core identification
# ──────────────────────────────────────────────
def identify(h):
    """Run all detectors and return sorted list of matching algo codes."""
    global jerar
    jerar = []
    for fn in ALL_CHECKS:
        fn(h)
    jerar.sort()
    return jerar

# ──────────────────────────────────────────────
#  Output helpers
# ──────────────────────────────────────────────
def print_results(h, results):
    bits = get_hash_length_bits(h)
    bit_info = f"{C.GRAY}  [{bits} bits]{C.RESET}" if bits else ""

    print(f"\n{C.CYAN}  Hash  :{C.RESET} {C.WHITE}{h}{C.RESET}{bit_info}")
    print(f"{C.CYAN}  Length:{C.RESET} {len(h)} characters\n")

    if not results:
        print(f"  {C.RED}✗  No matching algorithm found.{C.RESET}")
        print(f"  {C.GRAY}  The hash may be custom, truncated, or salted.{C.RESET}\n")
        return

    names = [algorithms[r] for r in results if r in algorithms]

    if len(names) <= 2:
        print(f"  {C.GREEN}{C.BOLD}✔  Most Likely:{C.RESET}")
        for n in names:
            print(f"     {C.GREEN}[+]{C.RESET} {C.WHITE}{n}{C.RESET}")
    else:
        print(f"  {C.GREEN}{C.BOLD}✔  Most Likely:{C.RESET}")
        for n in names[:2]:
            print(f"     {C.GREEN}[+]{C.RESET} {C.WHITE}{n}{C.RESET}")
        print(f"\n  {C.YELLOW}  Also Possible:{C.RESET}")
        for n in names[2:]:
            print(f"     {C.YELLOW}[-]{C.RESET} {C.DIM}{n}{C.RESET}")
    print()

def separator(label=""):
    width = 62
    if label:
        pad = (width - len(label) - 2) // 2
        print(f"\n{C.GRAY}  {'─'*pad} {C.CYAN}{label}{C.RESET}{C.GRAY} {'─'*pad}{C.RESET}")
    else:
        print(f"  {C.GRAY}{'─'*width}{C.RESET}")

# ──────────────────────────────────────────────
#  Batch mode: read hashes from file
# ──────────────────────────────────────────────
def batch_mode(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            lines = [l.strip() for l in f if l.strip() and not l.startswith('#')]
    except FileNotFoundError:
        print(f"\n  {C.RED}Error: File '{filepath}' not found.{C.RESET}\n")
        sys.exit(1)

    print(logo)
    print(f"  {C.CYAN}Batch mode:{C.RESET} processing {C.WHITE}{len(lines)}{C.RESET} hashes from {C.WHITE}{filepath}{C.RESET}\n")

    for i, h in enumerate(lines, 1):
        separator(f"Hash #{i}")
        results = identify(h)
        print_results(h, results)

# ──────────────────────────────────────────────
#  Interactive / single-hash mode
# ──────────────────────────────────────────────
def interactive_mode(first_hash=None):
    print(logo)
    first = first_hash

    while True:
        try:
            separator()
            if first:
                h = first
                first = None
            else:
                h = input(f"  {C.CYAN}HASH:{C.RESET} ").strip()

            if not h:
                print(f"  {C.YELLOW}  (empty input, try again){C.RESET}")
                continue
            if h.lower() in ('exit', 'quit', 'q'):
                raise KeyboardInterrupt

            if not is_valid_hash_chars(h):
                print(f"  {C.RED}  Input too short to be a valid hash.{C.RESET}")
                continue

            results = identify(h)
            print_results(h, results)

        except KeyboardInterrupt:
            print(f"\n\n  {C.CYAN}Goodbye!{C.RESET}\n")
            sys.exit(0)

# ──────────────────────────────────────────────
#  Entry point
# ──────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(
        prog="hash-info",
        description=f"Hash Info v{version} — Advanced Hash Identifier by Prasad",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="Examples:\n"
               "  python hash-info.py\n"
               "  python hash-info.py 5f4dcc3b5aa765d61d8327deb882cf99\n"
               "  python hash-info.py --file hashes.txt\n"
               "  python hash-info.py --no-color 5f4dcc3b5aa765d61d8327deb882cf99",
    )
    parser.add_argument("hash", nargs="?", help="Hash string to identify")
    parser.add_argument("-f", "--file", metavar="FILE",
                        help="File containing one hash per line")
    parser.add_argument("--no-color", action="store_true",
                        help="Disable colored output")
    parser.add_argument("-v", "--version", action="version",
                        version=f"Hash Info v{version} by Prasad")

    args = parser.parse_args()

    if args.no_color:
        for attr in vars(C):
            if not attr.startswith("_"):
                setattr(C, attr, "")

    if args.file:
        batch_mode(args.file)
    else:
        interactive_mode(first_hash=args.hash)


if __name__ == "__main__":
    main()
