import hashlib

# 4f1d9991f5acc0ca119f9d443620b77f9d6b33703e51011c16baf57afb285fc6

published_hash = "4f1d9991f5acc0ca119f9d443620b77f9d6b33703e51011c16baf57afb285fc6"

filename ="colorama-0.4.6-py2.py3-none-any.whl"

with open(filename, "rb") as downloaded_file:
    data = downloaded_file.read()
    sha = hashlib.sha256(data).hexdigest()
    print(sha)
    if sha == published_hash:
        print("Legit")
    else:
        print("Counterfeit")
