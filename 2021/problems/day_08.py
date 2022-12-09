INPUT_PREFIX = "c:/Users/ctyna/code/advent_of_code_2022/2021/inputs"
input_path = f"{INPUT_PREFIX}/day_08.txt"

f_in = open(input_path)

### PART ONE
tot = 0
while True:
    try: 
        line = next(f_in).strip()
    except StopIteration:
        break
    _, vals = line.split('|')
    vals = vals.strip().split()
    for v in vals:
        if len(v) in (2, 3, 4, 7):
            tot += 1
        else:
            pass
print(tot)

### PART TWO
def solve(digits):
    digit_dict = {}
    for v in digits:
        if len(v) == 2:
            digit_dict[1] = v
        if len(v) == 3:
            digit_dict[7] = v
        if len(v) == 4:
            digit_dict[4] = v
        if len(v) == 7:
            digit_dict[8] = v
    
    for v in digits:
        if len(v) == 5:
            ### Must be 2, 3 or 5
            missing_digits_one, missing_digits_four = 0, 0
            for v_elem in v:
                if v_elem not in digit_dict[1]:
                    missing_digits_one += 1
                if v_elem not in digit_dict[4]:
                    missing_digits_four += 1
            
            if missing_digits_one == 3:
                digit_dict[3] = v
            elif missing_digits_four == 3:
                digit_dict[2] = v
            elif missing_digits_four == 2:
                digit_dict[5] = v

    for v in digits:
        if len(v) == 6:
            ### Must be 0, 6 or 9
            missing_nine = 0
            for v_elem in digit_dict[3]:
                if v_elem not in v:
                    missing_nine += 1
            for v_elem in digit_dict[4]:
                if v_elem not in v:
                    missing_nine += 1
            
            if missing_nine == 0:
                digit_dict[9] = v
                continue
            
            missing_six = 0
            for v_elem in digit_dict[5]:
                if v_elem not in v:
                    missing_six += 1
            
            if missing_six == 0:
                digit_dict[6] = v
            elif missing_six == 1:
                digit_dict[0] = v
            else:
                raise Exception
    return digit_dict

tot = 0
f_in = open(input_path)

def val(value, d):
    for k, v in d.items():
        if v == value:
            return k

while True:
    try: 
        line = next(f_in).strip()
    except StopIteration:
        break
    digits, vals = line.split('|')
    digits = digits.strip().split()
    digit_dict = solve(digits)
    vals = vals.strip().split()
    for k, v in digit_dict.items():
        digit_dict[k] = sorted(v)
    for idx, v in enumerate(vals):
        vals[idx] = sorted(v)
        
    num = 1000*val(vals[0], digit_dict) + 100*val(vals[1], digit_dict) 
    num += 10*val(vals[2], digit_dict) + val(vals[3], digit_dict)
    tot += num

print(tot)