import sys


def read_dat(file_name):
    new_data = []
    with open(file_name, "r") as f:
        data = f.read().splitlines()
        for i in data:
            if i.startswith("add") or i.startswith("mul"):
                operation = i[0:3]
                data = i[4:]
                new_data.append((operation, data))
    return new_data


def inp_to_list(data):
    result = []
    for datas in data:
        operation = datas[0].upper()
        str_data = datas[1]
        split_str_data = str_data.split(" ")
        a_result = convert_str_list(split_str_data[0])
        b_result = convert_str_list(split_str_data[1])
        result.append((operation, a_result, b_result))
    return result


def convert_str_list(s):
    result = []
    xs = s.split(",")
    for x in xs:
        ys = x.split(":")
        result.append((int(ys[0]), int(ys[1])))
    return result


def add_polys(xs):
    result_addition = {}
    operation, poly1, poly2 = xs

    for coeff, exponent in poly1:
        result_addition[exponent] = coeff

    for coeff, exponent in poly2:
        if exponent in result_addition:
            result_addition[exponent] = result_addition[exponent] + coeff
        else:
            result_addition[exponent] = coeff

    return dict_to_list_result(result_addition)


def mul_poly(xs):
    exponent = 0
    coeff = 0
    result_multiplication = {}
    operation, poly1, poly2 = xs
    for coeff_1, exponent_1 in poly1:
        for coeff_2, exponent_2 in poly2:
            exponent = exponent_1 + exponent_2
            coeff = coeff_1 * coeff_2
            if exponent in result_multiplication:
                result_multiplication[exponent] = result_multiplication[exponent] + coeff
            else:
                result_multiplication[exponent] = coeff

    return dict_to_list_result(result_multiplication)


def dict_to_list_result(d):
    poly_list = [(coefficient, exponent) for exponent, coefficient in d.items()]
    poly_list.sort(key=lambda x: x[1], reverse=True)
    return poly_list


def list_to_str(xs):
    length = len(xs)
    formatted_str = ""
    for i, (coeff, exponent) in enumerate(xs):
        formatted_str += f'{coeff}:{exponent}'
        if i < length - 1:
            formatted_str += ','
    return formatted_str


def list_to_poly(input_list):
    polynomial_expression = ""

    for coeff, exp in input_list:
        if coeff == 0:
            continue
        term = ""

        # Handle coefficient
        if coeff != 1:
            if coeff == -1:
                term += "-"
            else:
                term += str(coeff)

        if exp == 0:
            term += ''
        elif exp == 1:
            term += "x"
        else:
            term += f"x^{exp}"

        if polynomial_expression:
            if coeff > 0:
                polynomial_expression += " + " + term
            else:
                polynomial_expression += " " + term
        else:
            polynomial_expression += term

    return polynomial_expression


def write_func(data):
    f = open("poly_answers.dat", "w")
    for lines in data:
        f.write(f"{lines}\n")
    f.close()


def main():
    file_name = sys.argv[1:]
    file_name_new = file_name[0]
    result_list = []
    dat = read_dat(file_name_new)

    xs = inp_to_list(dat)

    for i in xs:
        operation, poly1, poly2 = i
        if operation == 'ADD':
            result = add_polys(i)
            answer = list_to_str(result)
            result_list.append(answer)
            poly_answer_expression = list_to_poly(result)
            poly_1_expression = list_to_poly(poly1)
            poly_2_expression = list_to_poly(poly2)
            print(f'({poly_1_expression}) + ({poly_2_expression}) = {poly_answer_expression}')
            print()
        else:
            result = mul_poly(i)
            answer = list_to_str(result)
            result_list.append(answer)
            poly_answer_expression = list_to_poly(result)
            poly_1_expression = list_to_poly(poly1)
            poly_2_expression = list_to_poly(poly2)
            print(f'({poly_1_expression}) * ({poly_2_expression}) = {poly_answer_expression}')
            print()
    write_func(result_list)


if __name__ == '__main__':
    main()
