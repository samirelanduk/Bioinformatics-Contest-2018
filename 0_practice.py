with open("input.txt") as f:
    lines = [line.rstrip() for line in f]

problems = list(zip(lines[1:-1:2], lines[2::2]))

outputlines = []
for problem in problems:
    line = []
    sequence, subsequence = problem
    length = len(subsequence)
    for index in range(len(sequence) - len(subsequence)):
        if sequence[index:index + length] == subsequence:
            line.append(index + 1)
    outputlines.append(" ".join([str(index) for index in line]) + "\n")

with open("output.txt", "w") as f:
    f.writelines(outputlines)