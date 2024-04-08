<h1 align="center">rot_13</h1>
<div align="center">


Rot_13 is a simple Python script that encodes a given text using the ROT-13 cipher. ROT-13 is a Caesar cipher, where each letter in the plaintext is shifted 13 places down the alphabet.

### Installation

To use this script, you need to have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

Clone the repository:

```
git clone https://github.com/Blane187/rot_13.git
```

### Usage

1. Navigate to the directory where you cloned the repository.
2. Open a terminal or command prompt.
3. Run the script with Python:

```
python rot_13.py
```

### Example

```python
import codecs

url = "your text"
encoded_url = codecs.encode(url, 'rot_13')

print("Encoded URL:", encoded_url)
```

Replace `"your text"` with the text you want to encode. The script will output the encoded text.

### Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or create a pull request.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

>Please leave star if this code helpfull 👍🏻
