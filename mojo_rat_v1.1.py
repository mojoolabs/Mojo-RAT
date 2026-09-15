import os, base64, zlib, sys, hashlib, hmac
from colorama import Fore, Style, init
init(autoreset=True)

# -------- Screen clear --------
os.system("cls" if os.name == "nt" else "clear")

# -------- SAME SECRET used in encryptor.py --------
SECRET = b"secret!"

# -------- Paste your BLOB here --------
BLOB = "C/muaDgb+jWXPs0HvyMUTNIaTvqy2GvdsNTh9fuIewTv1nF/5EEldx+ruEn0xGDr/pyUaUYStCCKFp5XUo/oVtzX59NMdQYGEgQDAp8UE4rd2q4LAd9W/7ZZvS3GD7dzUPyaGe48rTsl7orcNRgAYQKlE/bDXyhOa8VLH/uiVsUe7QZAAmfowVBpLG2hRSIVYLkps7rGu8+nqOR8wn6AsRXQQacLC1Sq8aDqCz/tJBHb0grsT5E42p0zYlC8thbXdzpmY4BDJZWojUkH75XikhVaFAJfir66ktaymgMRCN2dYnjIZqTSosRuaGWcwbSYaYNu9VdCHwzyvnTIz79cT3jpIv8f/aWcgf6MMVztm/cx2Vn1fTDQM5wkx+Rwc+3yzLRIapZfiTwci4Cjbow3XFxEamTfSojHM4yGjDNC9IqTb3rPq4guN7fsCGKvh0JxLzPhz1rDOcMrvFsSdCzpkU5Jrlt+UYXZ5AljMRp+HDRr1bp1DU3HpIEz2YuOoMgpbVD5gyDvHiPQmZr+/xQ2v6TNjo/2dCI0ZI+LO6Zk4K0FxoniopyHio0AVXLwAV59G/UCKN43sndeIzq+qgkmlOWA5Jp73/ZlhMbJlwqm4GlYWQvwRls5g4IPZsB/wnI8piEWLyPwRj2WbGcBD+A4ueSgu0o7FBsJ965hxGXP6QWFvF6HBEDbH2HxByLxZyhqO99omqR0GKNH6SFRIr02RMQOW7sYb0HNx7+NCRq5bO5Hq9OQP/5Szd4KPVvEtF+WZjz3ydbHZYL3O+YYX9XrZgm7g0peWWlsTIfHbASK830fzr+tMEhk4eR5gmXox08cNqDy/vI4OWlBplBkXd8IoFIsnhs7a5tEoW1iUJRorur2PSqJd1mLaUiQRfk8558BPecK8N6+j3nOghlqxByW+V/WBMLbcT8q0qy3JXQRYULpJ2w5pUXZ+ZVEpHaobJIdBB9x31Xp8MFasp9Af9NNQWixZja5jsni7zfrorTQpjDW349yV1/ctoW9srdMJQPvmO1dCDuXpAXcY8JvhLipzCb8KiZUHx02O7wJ14+seMSEvKGJ4iTqB1GSKqXcBmv4LGbGvz3REv58o/hqTVjszM7jp5a4EV4CdAluFk26ZAdRIRQZXQEvOP09R+6SVwNh0snf+YBHG6tV0mFvauXlQB+Qx0IuKip3MfSmyOv1cbWW4+EdutmH7/ejfVdqWS7kXKzb2LVq4ECRY9MY6yR6A3dmqex16ZxhRkzqfBjk70EM3ej0YMOFy8KnhD2Vi9nYLtPfJ/Z+PwmGCbDkCbqxU3nxEzG6dZM4WcADdrAP3IZ0XAyUaXcMcOuDKXf94gx7v4ISSCKpYg/ocHA08P/69/OFs63TcVZllnUNXjRAZFBcBAGsQEkF9A8aKqIKJNXa1lJY4MDy1zC8cHe+nctrUKsim6Z8JnHBo8yKD5wJeelgCM+yNNVYDcHOyRv8RgpsbTtbvP7bQUG6m9+mF7SqjhWU5AaZgDNuFV9cU3tQYFNFjJnOPI3Fa5iaoilJPXNMZzwMolYGFHQ5oJUyCSDsXslGgaUAUKUIl780SKAmOEczWTN7TkuDqYCUWeCZQDfHo3WpaPkejNMPTl8B7L2y1fSIZlgSSEY5wlws5+EoQIjkJrJOtGgSu5NvI4e3Tuv++11t6HRhaSE7eTmPQjjkk9H8srtih26pmnJfl7u7HW4RO+229g6k60pP9WvRPKz/m+KUcRMJkpy6JLHxDzAA3+sSVj6cYZusVhy3EUCRzGF2m8YJcqsn43XcQXfaiQFsJfgMSqPOy0lQz8X8WmaVxI8L2D6m2RNxYrvnR6DYysg7srqu+Ak/vto6QRS12nmTZOmX66/VbtO1mtQSjYDf4NF92QMgSvA4eWjX16ro/eZ523uWV3FXZAMFB5H4tFoUtZV4+sUfTtUH2l3B/I54rd0f9Z4wPv7QVrtbd0mN+Jja/WOrHYBiTIyPt6Ad3lQ2WZSNWiNaWqsuXXAbYvw1XY+QbelKv+ujtzl+F47BbdYHCJR44LxnKRJlAoNi3XYJGIpsLxSncaii8pnewRvUhP3NktZDxm1KWfihaGBdzWfYnzmpYVmdDwU5Gjvw3f9WSGBd2TPbUov13YsbBT+gR77Oiz9GRHwt5WWxWLmqjSngs4CgpPGU4kINZPTOEl9ngghUWkCNMObPkTNLYwHJhljM30CQEfKx2yEL65eQ0FxMaUl1ltLFYCdVAboHjU1T1NHaH3QNw+k1f2B/9b+pRUlTs2+YGLR9Z9HqtPVaPGbW6Wu46KIc27VcxtTQz0TuYn3NCuZeBzX7GFtZgSRsk+VqyPGP4qGBWTqdfHKjlNNN3QDlJWDKC0hl4K0nEaQw7Ncy2EY26ibh+EbA6sryR9ZiXKZmQr9wLTbQuLMLmEktQtoFwIS+sQCbRlqd3Cl7aqAqZa0BVvhdCPdIjMojg3vnA68wFbQ/QM7uJT2A2o+33O2hv7kaOzgLcXIVqd+wMLs/mBsNZkyZG111bu4BD8lQsiRC62OVtGZCKL5zUEv5CaQHzpRsUrQ83oZ99rmqcP7WWnbZwCs72610f5qVFfB5ncVElH5PVbbNseB9il5i0H2j/rUhWuT2eRelsYTw2obL7/I9uKqu5BwELMZ8gbzSyXWulVm0UhGzbXddXsXvIddh4hNvPDA/jvVoTM3YZRA0KQxRDgbes8zzKAAZMj2bCbosoJ/O0BJv7IgZquHovB1J2R9VPKgCOHgEaz6ytWGfJKZVMfoFFrXaZ4ifM0doSBRMexQBWDgWcuD8HSZpJ0use9r4d9o8kRG8PA+kCABxlFtaN01ROnNsfjOh6k0Is3fc7SWqMIbYj4M5x0yBGckyY9ZJpx5jQQHr3q2WCKl0VoxxA1x5HJeOYIUDATZxzddYKuoTQlvHx7Fk6k9QpwzpD2qprQTFicUtIkerXw8t40xZazbf9E9lPjO33vUV8un9RypKEozjpX7u7Wa/SzXTDqIrIk9NNuR0wI7IqUww5x5D86JKKbAplcbALuqoB2Pb1mq8ReTxTs9AcLbKfOxJ+PLwqE3MqNeBm0aaOTXg4fCDkh6W9wM0n3zLqVyvUV3fK7jvYvYshlYXVUDOXscmz83unCfpiqBPhbYR3lFiE+ar93IvUo1JWWFathF9GvbycQjC4WW6ErThB19S/IPPSGLFH3RxIHQqVFzgM2Iyk612QDkrLQOY5M51J2K9SSYF7qKjrL58fSQ+8ZL8GMJxmEMOv3u7lEiurRxWrRS4QsGbMBE5zOUGonSZvs4gpOK68h71ATkDoLLJIX9kl2GyUIKwyPoVU1GciD4t71jgBcU6ue80zVapD6xMsRnkstacZmNufxYoGXbNzylXkqAnysGpydxmjhkDoLRVb4jPds2JMx0ngTtMZBCU8MO1FRCbMihxRs4eGPuLkLEV3/rRAEP+ZL8GZ53oPS45f+/bRe3J7/gRUSQ5jjDMLAvjMY9wWOkSGfvxaMT6YLxrQ2aM5JDGTsaiUQNpWH1jHBpeDv1IRnJbY0zky9iJjdKaJoWJIj0RW2IQ8C8B9hrcRJlIQxxaDg94jytouLLDW8E8k56IVccnE+rt1U3LQ1GM/CY9L9CPRc2Zxg+cAwvdPtzf4NkEbqVrzIbFBTkQlcEdjRS0SNjEF7sP9fc/yT6qLdHkdjSpNYDyGtO1UdIU8+0iyIGAUZDOJBE255S/G+RT4bYZSIznIMeZfMniWMk+IkeqZgnlGZ24n5Z7aIQ4bnNWYrdhq42N1SYmfKWrMDaj+/r8gQVS3ithkeTLEBvmiC8iXYrvMTNhmWt3nLbOSvNcnanYJeiUyHI+U6RjSPp4P8yQH8cXyma5Mtr9RJubqNitjWWqhDNy"   # your encrypted payload blob (same as before)

def xor_bytes(data: bytes, key: bytes) -> bytes:
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

def decrypt(b64s: str) -> str:
    raw = base64.b64decode(b64s.encode())
    plain = zlib.decompress(xor_bytes(raw, SECRET))
    return plain.decode("utf-8")

# -------- Encrypted License Key --------

VALID_KEY_HASH = "6e8bfe8bdf364b9aa18e25f75eca7672345764b5650d3fdfa12813722e3ca1e8"

def check_license(user_input: str) -> bool:
    # timing-safe compare
    hashed = hashlib.sha256(user_input.encode()).hexdigest()
    return hmac.compare_digest(hashed, VALID_KEY_HASH)

# -------- Colorful banner + license prompt --------
print(Fore.CYAN + Style.BRIGHT + "===========================")
print(Fore.GREEN + Style.BRIGHT + "        🔐 LICENSE CHECK")
print(Fore.CYAN + Style.BRIGHT + "===========================")

key = input(Fore.YELLOW + "Enter your license key: ").strip()
if not check_license(key):
    print(Fore.RED + "❌ Invalid license key!")
    sys.exit(1)

print(Fore.GREEN + "✅ License accepted!\n")

# -------- Decrypt & run payload --------
code = decrypt(BLOB)
ns = {}
exec(code, ns)      # payload must define run()
ns["run"]()         # execute payload
