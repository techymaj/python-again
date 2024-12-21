import hashlib

m = hashlib.sha256()
name = "Majaliwa Mbuto Wilfried"

m.update(
    name.encode()
)

d = m.hexdigest()
print(f"Digest: {d}")

print()

print(sorted(hashlib.algorithms_available))
print(sorted(hashlib.algorithms_guaranteed))
