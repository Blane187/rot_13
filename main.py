import codecs

url = "your teks"
encoded_url = codecs.encode(url, 'rot_13')

print("Encoded URL:", encoded_url)
