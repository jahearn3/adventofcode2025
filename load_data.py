def load_data(filename):
    lines = []
    with open('data/' + filename, 'r') as f:
        for line in f.readlines():
            lines.append(line.strip('\n'))
    return lines
