import socket
import re
from collections import Counter

def count_words(filepath):
    """Counts the total number of words in a file."""
    with open(filepath, 'r') as f:
        text = f.read()
    words = text.split()
    return len(words)

def count_words_handle_contractions(filepath):
    """Counts words, handling contractions by splitting them."""
    with open(filepath, 'r') as f:
        text = f.read()
    # Replace contractions with expanded forms
    text = re.sub(r"(\w+)'m", r"\1 am", text)
    text = re.sub(r"(\w+)'re", r"\1 are", text)
    text = re.sub(r"(\w+)'s", r"\1 is", text) #this one needs to be carfully done, because it could also mean possesion
    text = re.sub(r"(\w+)'ve", r"\1 have", text)
    text = re.sub(r"(\w+)'ll", r"\1 will", text)
    text = re.sub(r"(\w+)'d", r"\1 would", text) #could be had
    text = re.sub(r"can't", r"can not", text)
    text = re.sub(r"won't", r"will not", text)
    text = re.sub(r"n't", r" not", text) # handles general "not" contractions like don't, shouldn't, wouldn't

    words = text.split()
    return len(words)

def top_3_words(filepath, handle_contractions=False):
    """Finds the top 3 most frequent words in a file."""
    with open(filepath, 'r') as f:
        text = f.read()

    if handle_contractions:
        text = re.sub(r"(\w+)'m", r"\1 am", text)
        text = re.sub(r"(\w+)'re", r"\1 are", text)
        text = re.sub(r"(\w+)'s", r"\1 is", text)
        text = re.sub(r"(\w+)'ve", r"\1 have", text)
        text = re.sub(r"(\w+)'ll", r"\1 will", text)
        text = re.sub(r"(\w+)'d", r"\1 would", text)
        text = re.sub(r"can't", r"can not", text)
        text = re.sub(r"won't", r"will not", text)
        text = re.sub(r"n't", r" not", text)

    words = text.lower().split()  # Convert to lowercase for case-insensitivity
    # Remove punctuation from words.  Important for accurate counting.
    words = [word.strip('.,"?!:;()[]{}') for word in words]
    word_counts = Counter(words)
    return word_counts.most_common(3)


def get_ip_address():
    """Gets the IP address of the machine."""
    try:
        # Get the hostname
        hostname = socket.gethostname()
        # Get the IP address
        ip_address = socket.gethostbyname(hostname)
        return ip_address
    except Exception as e:
        return f"Error getting IP address: {e}"

def main():
    """Main function to perform all tasks."""
    if1_path = "/home/data/IF-1.txt"
    always_path = "/home/data/AlwaysRememberUsThisWay-1.txt"
    output_path = "/home/data/output/result.txt"

    # Create the output directory if it doesn't exist (good practice)
    import os
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # a. Count words in each file
    if1_count = count_words(if1_path)
    always_count = count_words_handle_contractions(always_path)

    # b. Calculate grand total
    grand_total = if1_count + always_count

    # c. Top 3 words in IF-1.txt
    if1_top3 = top_3_words(if1_path)

    # d. Top 3 words in AlwaysRememberUsThisWay-1.txt (handling contractions)
    always_top3 = top_3_words(always_path, handle_contractions=True)

    # e. Get IP address
    ip_address = get_ip_address()

    # f. Write results to file
    with open(output_path, 'w') as f:
        f.write(f"Total words in IF-1.txt: {if1_count}\n")
        f.write(f"Total words in AlwaysRememberUsThisWay-1.txt: {always_count}\n")
        f.write(f"Grand total words: {grand_total}\n")
        f.write(f"Top 3 words in IF-1.txt: {if1_top3}\n")
        f.write(f"Top 3 words in AlwaysRememberUsThisWay-1.txt (with contractions handled): {always_top3}\n")
        f.write(f"IP Address: {ip_address}\n")

    # Print the contents of the result file to the console
    with open(output_path, 'r') as f:
        print(f.read())

if __name__ == "__main__":
    main()