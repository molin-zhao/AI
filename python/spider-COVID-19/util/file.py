# write to file
def write_to_file(path, content):
    with open (path, 'w', encoding = 'utf-8') as f:
        f.write(content + '\n')