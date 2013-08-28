open_brackets = []

brackets = "{{[{{{{}}{{}}}[]}[][{}][({[(({{[][()()]}}{[{{{}}}]}))][()]{[[{((()))({}(())[][])}][]()]}{()[()]}]})][]]}{{}[]}}"

for index in range(len(brackets)):
    bracket = brackets[index]
    if bracket in "{[(":
        open_brackets.append(bracket)
    elif (open_brackets[-1] == "{" and bracket == "}") or \
        (open_brackets[-1] == "[" and bracket == "]") or \
        (open_brackets[-1] == "(" and bracket == ")"):
        open_brackets.pop()
    else:
        print("Problem at: %d" % index)
        break
