import os

excuse = "Sorry I missed a spot — I was charging! It's the oldest robot vacuum excuse in the book, and honestly I'm surprised you fell for it."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w") as f:
    f.write(excuse)