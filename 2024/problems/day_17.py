INPUT_PREFIX = "c:/Users/ctyna/code/advent_of_code_2022/2024/inputs"
input_path = f"{INPUT_PREFIX}/day_17.txt"

f_in = open(input_path)
grid = []
A, B, C, program_str = None, None, None, None
for line in f_in.readlines():
    line = line.strip()
    if 'Register A:' in line:
        A = int(line.split(':')[1].strip())
    
    elif 'Register B:' in line:
        B = int(line.split(':')[1].strip())
        
    elif 'Register C:' in line:
        C = int(line.split(':')[1].strip())
    elif 'Program' in line:
        program = list(map(int, line.replace('Program: ', '').split(',')))
        program_str = line.replace('Program: ', '')

def run_iteration(A, program):
    N = len(program) // 2
    literal_operands = [program[2*idx] for idx in range(N)]
    combo_operands = [program[2*idx + 1] for idx in range(N)]
    idx = 0
    output_value = None

    while idx < N:
        lit_op = literal_operands[idx]
        comb_op = combo_operands[idx]
        if comb_op == 4:
            comb_op = A
        elif comb_op == 5:
            comb_op = B
        elif comb_op == 6:
            comb_op = C
        
        idx += 1

        if lit_op == 0:
            A = A // 2**comb_op
        elif lit_op == 1:
            B = B ^ comb_op
        elif lit_op == 2:
            B = comb_op % 8
        elif lit_op == 3:
            return (A, output_value)
        elif lit_op == 4:
            B = B ^ C
        elif lit_op == 5:
            output_value = comb_op % 8
        elif lit_op == 6:
            B = A // 2**comb_op
        elif lit_op == 7:
            C = A // 2**comb_op

    return

def get_outputs(A, program):
    outputs = []
    while A > 0:
        A, output_value = run_iteration(A, program)
        outputs.append(str(output_value))
    return outputs

print(",".join([v for v in get_outputs(A, program)]))

program_entries = program_str.split(',')
program_idx = 1
scaler = 2**3
q = [0]
best = None
while len(q) > 0:
    cur_A = q.pop()
    for i in range(0,8):
        new_A = scaler * cur_A + i 
        output_value = get_outputs(new_A, program)
        if output_value == program_entries[-len(output_value):]:
            q.append(new_A)
            if output_value == program_entries:
                if best is None:
                    best = new_A
                else:
                    best = min(new_A, best)

print(best)


    
     

