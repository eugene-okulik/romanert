import argparse
import os
import sys


def read_logs(directory, text, date=None):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".log"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    for i, line in enumerate(lines):
                        if date and date not in line:
                            continue
                        if text in line:
                            context = search_word(line, text)
                            print(f"File: {file_path}\nLine: {i + 1}\nContext: {context}\n" + "-" * 50)


def search_word(line, search_text):
    words = line.split()
    context = []
    for i, word in enumerate(words):
        if search_text in word:
            start = max(0, i - 5)
            end = min(len(words), i + 6)
            context = words[start:end]
            break
    return ' '.join(context)


def main(args):
    parser = argparse.ArgumentParser(description="Analyze log files")
    parser.add_argument('logs_dir', type=str, help="Directory containing log files")
    parser.add_argument('--date', type=str, help='Date to search for in the log files, format YEAR-MM-DD')
    parser.add_argument('--text', type=str, help="Text to search for in the log files")

    parser_args = parser.parse_args(args)

    logs_dir = os.path.abspath(parser_args.logs_dir)

    if not os.path.isdir(logs_dir):
        print(f"The directory {logs_dir} does not exist.")
        sys.exit(1)

    read_logs(logs_dir, parser_args.text, parser_args.date)


if __name__ == "__main__":
    main(sys.argv[1:])
