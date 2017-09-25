from Gelatin.util import compile, generate

# Parse your .gel file.
syntax = compile('cfwd-syntax.gel')

# Convert your input file to XML, YAML, and JSON.
print(generate(syntax, 'data.txt'))
#print(generate(syntax, 'input.txt', format='yaml'))
#print(generate(syntax, 'input.txt', format='json'))
