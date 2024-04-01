import hashlib

def image_to_byte(image):
    with open(image, "rb") as f:
        return f.read()

akatsuki_hash = hashlib.sha256(image_to_byte("../images/akatsuki.jpg"))
itachi_hash = hashlib.sha256(image_to_byte("../images/itachi_sacrifice.jpg"))
print(akatsuki_hash.hexdigest())
print(itachi_hash.hexdigest())