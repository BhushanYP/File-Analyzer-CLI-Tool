import re
import string
from collections import Counter

# list of common words
STOP_WORDS = {
    "the", "is", "in", "and", "to", "of", "a", "an", "on", "at", "for", "with", "by", "this", "that", "it", "as", "was", "were", "be", "been", "being"
}

def process_text(text):
    # convert to lowercase
    text = text.lower()

    # remove punctuation
    text = re.sub(f"[{string.punctuation}]", "", text)

    # split the text into words
    words = text.split()

    return words

def analyze_file(file_path):
    # Open the file and read its content
    with open(file_path, 'r') as file:
        text = file.read()

    # Process text to get words
    words = process_text(text)

    # Calculate total number of words
    total_words = len(words)

    # Remove stop words for word frequency analysis
    # [expression for item in iterable if condition]
    filtered_words = [word for word in words if word not in STOP_WORDS]

    # Get the top 5 most frequent words
    word_counts = Counter(filtered_words)
    top_5_words = word_counts.most_common(5)

    # Calculate average word length
    if total_words > 0:
        average_word_length = sum(len(word) for word in words) / total_words
    else:
        average_word_length = 0

    # Count the number of sentences by using ".", "!", "?"
    sentences = re.split(r'[.!?]', text)
    # Filter out empty sentences
    num_sentences = len([sentence for sentence in sentences if sentence.strip()])

    # Create the summary report
    report = {
        "Total words": total_words,
        "Top 5 most frequent words": top_5_words,
        "Average word length": round(average_word_length, 2),
        "Number of sentences": num_sentences
    }

    return report

# Printing report on console
def print_report(report):
    print("Text Analysis Report")
    print("--------------------")
    print(f"Total number of words: {report['Total words']}")
    print(f"Top 5 most frequent words:")
    for word, freq in report['Top 5 most frequent words']:
        print(f"  - {word}: {freq} times")
    print(f"Average word length: {report['Average word length']} characters")
    print(f"Number of sentences: {report['Number of sentences']}")

if __name__ == "__main__":
    import argparse

    # Set up argument parser
    parser = argparse.ArgumentParser(description="Analyze a text file and provide a summary report.")
    parser.add_argument("file", help="Path to the .txt file to analyze")

    # Parse arguments
    args = parser.parse_args()

    try:
        # Analyze the file and generate the report
        report = analyze_file(args.file)
        # Print the report
        print_report(report)
    except FileNotFoundError:
        print(f"Error: The file '{args.file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")