open_brackets = []

brackets = "{{[{{{{}}{{}}}[]}[][{}][({[(({{[][()()]}}{[{{{}}}]}))][()]{[[{((()))({}(())[][])}][]()]}{()[()]}]})][]]}{{}[]}}"

bracket_matches = {
                    "{" : "}",
                    "[": "]",
                    "(": ")"
                }

for index in range(len(brackets)):
    bracket = brackets[index]
    if bracket in "{[(":
        open_brackets.append(bracket)
    elif bracket_matches[open_brackets[-1]] == bracket:
        open_brackets.pop()
    else:
        print("Problem at: %d" % index)
        break
