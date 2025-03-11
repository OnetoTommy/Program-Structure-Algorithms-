import heapq


# Define a class for Huffman Tree Nodes
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # Define how nodes are compared (needed for priority queue)
    def __lt__(self, other):
        return self.freq < other.freq


# Function to build Huffman Tree
def build_huffman_tree(frequencies):
    # Create a priority queue (min-heap)
    priority_queue = [HuffmanNode(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        # Extract two nodes with the smallest frequencies
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)

        # Create a new internal node with their combined frequency
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        # Push the new node back into the priority queue
        heapq.heappush(priority_queue, merged)

    # The final node is the root of the Huffman Tree
    return priority_queue[0]


# Function to generate Huffman Codes
def generate_huffman_codes(root, current_code="", code_map={}):
    if root is None:
        return

    # If it's a leaf node (i.e., has a character), store its code
    if root.char is not None:
        code_map[root.char] = current_code
        return

    # Recursive traversal for left and right with '0' and '1' respectively
    generate_huffman_codes(root.left, current_code + "0", code_map)
    generate_huffman_codes(root.right, current_code + "1", code_map)

    return code_map


# Function to encode text using Huffman Codes
def huffman_encoding(text):
    if not text:
        return "", None

    # Calculate frequency of each character
    frequency = {}
    for char in text:
        frequency[char] = frequency.get(char, 0) + 1

    # Build Huffman Tree
    huffman_tree_root = build_huffman_tree(frequency)

    # Generate Huffman Codes
    huffman_codes = generate_huffman_codes(huffman_tree_root)

    # Encode the text
    encoded_text = "".join(huffman_codes[char] for char in text)

    return encoded_text, huffman_tree_root


# Function to decode Huffman encoded text
def huffman_decoding(encoded_text, tree_root):
    if not encoded_text or not tree_root:
        return ""

    decoded_text = ""
    current_node = tree_root

    for bit in encoded_text:
        # Traverse left for '0', right for '1'
        current_node = current_node.left if bit == "0" else current_node.right

        # If it's a leaf node, append the character and reset
        if current_node.char is not None:
            decoded_text += current_node.char
            current_node = tree_root

    return decoded_text


# Example Usage
text = "huffman coding example"
encoded_text, tree_root = huffman_encoding(text)
decoded_text = huffman_decoding(encoded_text, tree_root)

# Output Results
print("Original Text:", text)
print("Encoded Text:", encoded_text)
print("Decoded Text:", decoded_text)
