import os
import sys
import re
import subprocess

from os.path import expanduser

READ_DIFF = 1
GENERATE_DIFF = 2
PRINT_HELP = 3

def usage():
    print("<diff file> <first directory> <second directory> <output root directory>")
    print("The order of the directories must match the order used to generate the diff file")
    exit(2)

def diff_usage():
    print("diff <u|n|e> <first directory> <second directory> <output root directory> <output file>")
    exit(2)

def read_diff_args(args):
    if len(args) < 4:
        diff_usage()
    if args[0] != 'u' and args[0] != 'n' and args[0] != 'e':
        diff_usage()

    return (GENERATE_DIFF, args[0], args[1], args[2], args[3], args[4])

def print_help():
    print("This tool is meant to generate a diff directory where each diff file is " +
          "put in a directory which represents its original file's relative path from the root.")
    print("It can either read an existing diff file created by 'diff -r' or generate " +
          "the directory diff file and then read it.")
    print("For more information check the manual page for 'diff'.")
    print("")
    print("Usage:")
    print("To read an existing file")
    print("<diff file> <first directory> <second directory> <output root directory>")
    print("To generate a diff file then generate the diff directory")
    print("diff <format> <first directory> <second directory> <output root directory> <output file>")
    print("Where the format can either be u, n, or e")
    print("The output file is a name relative to the output root directory")

def read_args(args):
    if len(args) < 4:
        if len(args) > 0 and (args[0] == '--help' or args[0] == '-h'):
            return (PRINT_HELP, '')

    if args[0] == 'diff':
        return read_diff_args(args[1:])
    return (READ_DIFF, args[0], args[1], args[2], args[3])

def main(args):
    action = read_args(args)

    if action[0] == PRINT_HELP:
        print_help()
    elif action[0] == READ_DIFF:
        read_diff(action[1], action[2], action[3], action[4])
    elif action[0] == GENERATE_DIFF:
        diff_file = generate_diff(action[1], action[2], action[3], action[4], action[5])
        read_diff(diff_file, action[2], action[3], action[4])

def read_diff(diff_file, first_root, second_root, output_root):
    """
    Reads a recursive directory diff file and calls extract_files()
    to take care of the rest.
    """
    diff_file = expanduser(diff_file)
    first_root = full_path(first_root)
    second_root = full_path(second_root)
    output_root = full_path(output_root)
    with open(diff_file) as f:
        extract_files(f.read(), first_root, second_root, output_root)

def generate_diff(format, first_root, second_root, output_root, output_file):
    """
    Generates a diff file of two directories, and stores the file in
    'output_root/output_file'.
    Uses 'diff' command to generate the files.
    """
    try:
        os.makedirs(output_root)
    except OSError as e:
        pass

    first_root = full_path(first_root)
    second_root = full_path(second_root)
    output_root = full_path(output_root)
    command = str.format('diff -Nr -%s %s %s > %s' %(format, first_root, second_root, output_root+output_file))
    subprocess.call(command, shell=True)
    return output_root + output_file

def full_path(dir):
    """
    Maps a path its full path and appends a '/' to the end, if not
    found.
    Example: '~/path' -> '/home/<user>/path/'
    """
    if dir[len(dir)-1] != '/':
        return expanduser(dir) + '/'
    else:
        return expanduser(dir)

def matched_lines(pattern, str):
    """
    Returns an iterator of lines in a string which match a pattern.
    """
    return re.compile(pattern, re.MULTILINE).finditer(str)

def extract_content(str, file_match, next_match=None):
    """
    Extracts the content of the diff of a single file, starting from
    after the match.
    """
    if next_match:
        return str[file_match.end()+1:next_match.start()] # need +1 since we want the first character after the match
    else:
        return str[file_match.end()+1:] # need +1 since we want the first character after the match

def extract_filenames(line):
    """
    Extracts the file names from a line which separates the diff of each
    file from the previous. It's basically the same recusrive diff command
    with the two absolute path files as arguments.
    """
    last = line.rindex(' ')
    before_last = line.rindex(' ', 0, last)
    return (line[before_last+1:last], line[last+1:])

def extract_directory(filename):
    """
    Extracts the longest directory from a file path.
    """
    return filename[:filename.rindex('/')+1]

def remove_root(root, filename):
    """
    Removes the root directory from an absolute file path to return
    only the relative path.
    """
    if filename.startswith(root):
        return filename[len(root):]
    raise ValueError(filename + " doesn't contain " + root + " as its root")

def validate_match(filenames):
    """
    Validates that a pair of relative file paths are the same.
    """
    return filenames[0] == filenames[1]

def process_file(output_dir, filename, content):
    """
    Creates a file relative to the output directory (and all intermediate
    directories) and writes the content to it.
    """
    file_path = output_dir + filename + '.diff'
    directory_path = extract_directory(file_path)
    try:
        os.makedirs(directory_path)
    except OSError as e:
        pass
    with open(file_path, 'w') as output_file:
        output_file.write(content)

def extract_files(str, first_root, second_root, output_dir):
    """
    Extracts individual files from the contents of a directory diff file, and
    writes each one to a file with the same relative path with output directory
    as its root.
    Note: The order of the root directories matter.
    """
    pattern = '(^diff.+$|^Binary\\sfiles\\s.+$)' # since we use MULTILINE flag '^' will match start of string or start of a line
    lines = list(matched_lines(pattern, str))
    index = 0
    for line in lines:
        if not line.group().startswith('Binary'):
            names = extract_filenames(line.group())
            shortend = (remove_root(first_root, names[0]), remove_root(second_root, names[1]))
            if validate_match(shortend):
                if index != len(lines)-1:
                    process_file(output_dir, shortend[0], extract_content(str, line, lines[index+1]))
                else:
                    process_file(output_dir, shortend[0], extract_content(str, line))
            else:
                print(shortend[0] + " doesn't match " + shortend[1])
        index += 1

main(sys.argv[1:])
