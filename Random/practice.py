import io

f = io.open("photo.jpg", "rb", buffering=0)

print(f.read())