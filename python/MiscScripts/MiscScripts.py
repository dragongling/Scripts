import re
import math


def fib_indexes_program():
    count = int(input())
    for i in range(0, count):
        current = int(input())
        print(str(fib_index(current)) + ' ')


def read_list_by_count():
    input_list = []
    input()
    for i in input().split():
        input_list.append(float(i))
    return input_list


def smoothing_the_weather():
    temperatures = read_list_by_count()
    print(temperatures[0])
    for i in range(1, len(temperatures) - 1):
        print((temperatures[i - 1] + temperatures[i] + temperatures[i + 1]) / 3.0)
    print(temperatures[len(temperatures) - 1])


def is_palindrome(s):
    for i in range(0, len(s)):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True


def palindromes_program():
    count = int(input())
    for i in range(0, count):
        input_string = re.sub(r'[^\w]', '', input()).lower()
        print("y " if is_palindrome(input_string) else "n ")


def bicycle_race_program():
    count = int(input())
    for i in range(0, count):
        distance, speed1, speed2 = (float(s) for s in input().split())
        print(distance / (speed1 + speed2) * speed1, ' ')


def rotate_string_program():
    count = int(input())
    for i in range(0, count):
        rotation, input_string = input().split()
        rotation = int(rotation)
        print(input_string[rotation:] + input_string[:rotation], ' ')


def josephus_problem(n, k):
    soldiers = list(range(1, n + 1))
    z = 0
    while len(soldiers) != 1:
        end = len(soldiers)
        i = 0
        while i < end:
            if z == k - 1:
                soldiers.remove(soldiers[i])
                end -= 1
            else:
                i += 1
            z = (z + 1) % k
    return soldiers[0]


def josephus_problem_program():
    n, k = (int(s) for s in input().split())
    print(josephus_problem(n, k))


def pythagorean_theorem_program():
    count = int(input())
    for i in range(0, count):
        a, b, c = (int(s) for s in input().split())
        if a ** 2 + b ** 2 > c ** 2:
            print("a ")
        elif a ** 2 + b ** 2 == c ** 2:
            print("r ")
        else:
            print("o ")


def square_root_program():
    count = int(input())
    for i in range(0, count):
        number, accuracy = (int(s) for s in input().split())
        result = 1.0
        for j in range(0, accuracy):
            result = (result + number / result) / 2
        print(result, ' ')


def dice(num):
    return num % 6 + 1


def caesar_shift_program():
    count, k = (int(s) for s in input().split())
    for i in range(0, count):
        s = list(input())
        for j in range(0, len(s)):
            if (s[j] >= 'a') and (s[j] <= 'z'):
                s[j] = chr(ord(s[j]) - k)
                if s[j] < 'a':
                    s[j] = chr(ord(s[j]) + 26)
        print("".join(s), ' ')


def savings_calculator_program():
    count = int(input())
    for i in range(0, count):
        s, r, p = (int(s) for s in input().split())
        print(math.ceil(math.log(r / s) / math.log(1 + p / 100)))


def matching_words_program():
    l = input().split()
    l2 = list()
    for i in range(0, len(l)):
        if (l[i] in l[:i]) and not (l[i] in l2):
            l2.append(l[i])
    l2.sort()
    print(' '.join(l2))


#############################################################################

def normal_distribution(sigma, m, x):
    return math.exp(-(x - m) ** 2 / (2 * sigma ** 2)) / (sigma * math.sqrt(2 * math.pi))


# подсчёт середин интервалов:
def make_averages_from_intervals(intervals):
    return [(x + y) / 2 for (x, y) in zip(intervals[:-1], intervals[1:])]


# получение частот по массиву
def get_frequencies(values):
    return [n / sum([i for i in values]) for n in values]


# n-й момент
def moment(n, values, probabilities):
    return sum([x ** n * p for (x, p) in zip(values, probabilities)])


# n-й центральный момент
def central_moment(n, expected_value, values, probabilities):
    return moment(n, [(x - expected_value) for x in values], probabilities)


# среднее выборочное
def sample_mean(values, probabilities):
    return moment(1, values, probabilities)


def general(value, n):
    return value / n


# дисперсия
def variation(sample_mean_value, values, probabilities):
    return central_moment(2, sample_mean_value, values, probabilities)


# среднее квадратичное отклонение
def standard_deviation(dispersion):
    return math.sqrt(dispersion)


# асимметрия
def skewness(sample_mean_value, standard_deviation_value, values, probabilities):
    return central_moment(3, sample_mean_value, values, probabilities) / standard_deviation_value ** 3


# эксцесс
def general_excess(sample_mean_value, standard_deviation_value, values, probabilities, values_count):
    return general(central_moment(4, sample_mean_value, values, probabilities), values_count) \
           / standard_deviation_value ** 4 - 3


def make_interval_borders(x1, step, count):
    interval_borders = [x1]
    for i in range(1, count):
        interval_borders.append(interval_borders[i - 1] + step)
    return interval_borders


def read_int(string):
    print("введите " + string + ": ", end="")
    return int(input())


def probability_theory_homework():
    # interval_borders = [ 6, 16, 26, 36, 46, 56, 66, 76, 86 ]
    # counts = [ 8, 7, 16, 35, 15, 8, 6, 5 ]

    # концы интервалов:
    # interval_borders = [6, 10, 14, 18, 22, 26, 30, 34, 38, 42]
    # значения интервалов:
    # counts = [15, 26, 25, 30, 26, 21, 24, 20, 13]

    # ввод:
    x1 = read_int("x1")
    step = read_int("шаг")
    count = read_int("количество")
    counts = []
    for i in range(1, count):
        counts.append(read_int("n" + str(i)))

    interval_borders = make_interval_borders(x1, step, count)
    values = make_averages_from_intervals(interval_borders)
    frequencies = get_frequencies(counts)  # считаем частоты
    # n = sum(counts)  # число опытов
    # получаем необходимые параметры:
    values_sample_mean = sample_mean(values, frequencies)
    values_variation = variation(sample_mean, values, frequencies)
    values_standard_deviation = standard_deviation(variation)
    values_skewness = skewness(sample_mean, values_standard_deviation, values, frequencies)
    values_excess = central_moment(4, sample_mean, values, frequencies) / values_standard_deviation ** 4 - 3

    # вывод:
    print("средние значения: ", " ".join(str(x) for x in values))
    print("частоты: ", " ".join(str(x) for x in frequencies))
    print("выборочное среднее: ", values_sample_mean)
    print("дисперсия: ", values_variation)
    print("среднее квадратичное отклонение: ", values_standard_deviation)
    print("асимметрия: ", values_skewness)
    print("эксцесс: ", values_excess)


#############################################################################


def triangle_area():
    count = int(input())
    for i in range(0, count):
        x1, y1, x2, y2, x3, y3 = (int(s) for s in input().split())
        area = abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2
        print(area, ' ')


def rock_paper_scissors():
    count = int(input())
    winning_map = {"r": "s", "s": "p", "p": "r"}
    for i in range(0, count):
        matches = input().split()
        player_points = [0, 0]
        for match in matches:
            if match[0] == match[1]:
                continue
            if winning_map[match[0]] == match[1]:
                player_points[0] += 1
            else:
                player_points[1] += 1
        print(1 if player_points[0] > player_points[1] else 2, ' ')


def matching_brackets():
    count = int(input())
    opening_brackets = "({[<"
    closing_brackets = ")}]>"
    for i in range(0, count):
        right = True
        brackets_stack = []
        input_string = input()
        for char in input_string:
            if char in opening_brackets:
                brackets_stack.append(char)
            elif (char in closing_brackets) and ((len(brackets_stack) == 0)
                                                 or (
                            char != closing_brackets[opening_brackets.find(brackets_stack.pop())])):
                right = False
                break
        if len(brackets_stack) > 0:
            right = False
        print(1 if right else 0, end=' ')


def cards():
    input()
    suits = ['clubs', 'spades', 'diamonds', 'hearts']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
    for word in input().split():
        card_index = int(word)
        suit_index = int(card_index / 13)
        rank_index = card_index % 13
        print(ranks[rank_index] + '-of-' + suits[suit_index] + ' ')


def fools_day2014():
    count = int(input())
    for test in range(0, count):
        result_sum = 0
        for word in input().split():
            result_sum += int(word) ** 2
        print(result_sum, end=' ')


def bulls_and_cows():
    secret, guess_num = input().split()
    for guess in input().split():
        bulls, cows = 0, 0
        for i in range(0, 4):
            if guess[i] == secret[i]:
                bulls += 1
            elif guess[i] in secret:
                cows += 1
        print(str(bulls) + '-' + str(cows), end=' ')


def combination_counting():
    count = int(input())
    for i in range(0, count):
        n, k = (int(word) for word in input().split())
        c = int(math.factorial(n) / (math.factorial(k) * math.factorial(n - k)))
        print(c, end=' ')


def f(a, b, c, d, x):
    return a * x + b * math.pow(x, 1.5) - c * math.exp(-x / 50) - d


def binary_search():
    count = int(input())
    for i in range(0, count):
        a, b, c, d = (float(word) for word in input().split())
        a, b, precision = 0.0, 100.0, 0.0000001
        while b - a > precision:
            c = (a + b) / 2
            if f(a, b, c, d, a) * f(a, b, c, d, c) < 0:
                b = c
            elif f(a, b, c, d, a) * f(a, b, c, d, c) > 0:
                a = c
            else:
                a = c
                break
        print(a, end=' ')


def selection_sort():
    count = int(input())
    array = list(int(word) for word in input().split())
    for i in range(0, count - 1):
        max_index = 0
        for j in range(1, count - i):
            if array[j] > array[max_index]:
                max_index = j
        print(max_index, end=' ')
        array[max_index], array[count - i - 1] = array[count - i - 1], array[max_index]


def quadratic_equation():
    count = int(input())
    for case in range(0, count):
        a, b, c = (int(word) for word in input().split())
        d = b ** 2 - 4 * a * c
        if d >= 0:
            x1 = int((-b + math.sqrt(d)) / (2 * a))
            x2 = int((-b - math.sqrt(d)) / (2 * a))
            print(x1, x2, end='')
        else:
            real = int(-b / (2 * a))
            imaginary = int(math.sqrt(abs(d)) / (2 * a))
            print(real, '+', imaginary, 'i ', real, '-', imaginary, 'i', sep='', end='')
        if case < count - 1:
            print('; ')


def compare(a, b):
    ret = a, b
    if a > b:
        ret = b, a
    return ret


def greatest_common_divisor(a, b):
    a, b = compare(a, b)
    while a % b != 0:
        a, b = b, a % b
    return b


def least_common_multiple(a, b):
    return a * b / greatest_common_divisor(a, b)


def two_printers():
    count = int(input())
    for case in range(0, count):
        x, y, n = (int(word) for word in input().split())
        if x > y:
            x, y = y, x
        total_x, total_y = 0, 0
        lcm = int(least_common_multiple(x, y))
        lcm_n = int(lcm / x + lcm / y)
        lcm_count = int(n / lcm_n)
        total = lcm * lcm_count
        for page in range(lcm_count * lcm_n, n):
            if (total_x + x <= total_y + y) or (total_x <= total_y):
                total_x += x
            else:
                total_y += y
        print(total + max(total_x, total_y), end=' ')


def blackjack():
    count = int(input())
    ranks = {"t": 10, "j": 10, "q": 10, "k": 10}
    for case in range(0, count):
        result_sum = 0
        aces = 0
        for word in input().split():
            if "0" <= word <= 9:
                result_sum += int(word)
            elif word == "a":
                aces += 1
            else:
                result_sum += ranks[word]
        while aces > 0:
            if 11 - result_sum >= aces:
                result_sum += 11
            else:
                result_sum += 1
            aces -= 1
        print(result_sum if result_sum <= 21 else "bust", end=' ')


def king_and_queen():
    count = int(input())
    for case in range(0, count):
        king, queen = input().split()
        king_x = ord(king[0]) - ord('a') + 1
        king_y = int(king[1])
        queen_x = ord(queen[0]) - ord('a') + 1
        queen_y = int(queen[1])
        if (king_x == queen_x or king_y == queen_y
            or king_x + king_y == queen_x + queen_y
                or king_x - king_y == queen_x - queen_y):
            print("y", end=' ')
        else:
            print("n", end=' ')


def card_shuffling():
    deck = []
    for suit in "cdhs":
        for value in "a23456789tjqk":
            deck.append(suit + value)
    i = 0
    for random in input().split():
        j = int(random) % 52
        deck[i], deck[j] = deck[j], deck[i]
        i += 1
    print(' '.join(deck))


def linear_congruential_generator(a, c, m, x0, n):
    random_numbers = []
    for j in range(0, n):
        x0 = (a * x0 + c) % m
        random_numbers.append(x0)
    return random_numbers, x0


def fib_index(end):
    if end <= 1:
        return end
    current = 1
    previous = 0
    index = 1
    while current < end:
        current, previous = previous, current
        current += previous
        index += 1
    return index


def funny_words_generator():
    letters = ["bcdfghjklmnprstvwxz", "aeiou"]
    count, x0 = (int(word) for word in input().split())
    lengths = (int(word) for word in input().split())
    for length in lengths:
        random_values, x0 = linear_congruential_generator(445, 700001, 2097152, x0, length)
        for i in range(0, length):
            print(letters[i % 2][random_values[i] % len(letters[i % 2])], end='')
        print(' ', end='')


def fibonacci_divisibility():
    input()
    for m in (int(word) for word in input().split()):
        current = 1
        previous = 0
        index = 1
        while current % m != 0:
            current, previous = previous, current
            current += previous
            index += 1
        print(index, end=' ')


def mortgage_calculator():
    p, r, l = (int(word) for word in input().split())
    r = r / 12 / 100
    m = math.ceil(p * (r * pow(r + 1, l)) / (pow(r + 1, l) - 1))
    print(m)


def check_tic_tac_toe_win(turns):
    wins = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for win in wins:
        i = 0
        for num in win:
            if num in turns:
                i += 1
        if i == 3:
            return True
    return False


def tic_tac_toe():
    count = int(input())
    for case in range(0, count):
        players = [[], []]
        first_player = True
        win = False
        turn_num = 1
        for turn in (int(word) for word in input().split()):
            i = int(not first_player)
            players[i].append(turn)
            if check_tic_tac_toe_win(players[i]):
                print(turn_num, end=' ')
                win = True
                break
            first_player = not first_player
            turn_num += 1
        if not win:
            print(0, end=' ')


def prime(n):
    for x in range(2, int(math.sqrt(n) + 1)):
        if n % x == 0:
            return x
    else:
        return 0


def prime_text(n):
    result = 1
    p = prime(n)
    if p:
        while p:
            result += 1
            n = n // p
            p = prime(n)
    return result


def olympics():
    num = int(input())
    if prime_text(num) == 20:
        print("yes")
    else:
        print("no")
        # prime_text(32)


def some_shit():
    input()
    array = list(int(word) for word in input().split())
    for i in range(1, len(array)):
        swap_count = 0
        while array[i] < array[i - 1]:
            array[i], array[i - 1] = array[i - 1], array[i]
            swap_count += 1
        print(swap_count, end=' ')
    print(array)


def some_shit2():
    count = int(input())
    for case in range(0, count):
        a, b = (int(x) for x in input().split())
        print(math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a)) + 1)


def contiguous_sum(array):
    size = len(array)
    if size <= 1:
        return array[0]
    sums = [sum(array)]
    for i in range(2):
        subarray_sum = sum(array[i:(size - 1 + i)])
        if subarray_sum > sums[0]:
            sums.append(contiguous_sum(array[i:(size - 1 + i)]))
    return max(sums)


def max_sum(array):
    size = len(array)
    if size <= 1:
        return array[0]
    return max(sum(array), max_sum(array[:(size - 1)]), max_sum(array[1:]))


def positive_sum(array):
    result_sum = 0
    non_negative = False
    for i in array:
        if i >= 0:
            result_sum += i
            non_negative = True
    return result_sum if non_negative else max(array)


def some_shit3():
    count = int(input())
    for case in range(count):
        input()
        array = list(int(i) for i in input().split())
        print(max_sum(array), positive_sum(array))


def number_of_a(s, n):
    res = 0
    for c in s[:n]:
        if c == 'a':
            res += 1
    return res


def brute(l, n):
    for i in range(n - 3, -1, -1):
        for j in range(n - 2, i, -1):
            for k in range(n - 1, j, -1):
                if l[i] + l[j] > l[k] and l[i] + l[k] > l[j] and l[j] + l[k] > l[i]:
                    return [l[i], l[j], l[k]]
    return [-1]


def hz():
    n = int(input().strip())
    ss = []
    for i in range(0, n):
        ss.append(input().strip())
    for s in ss:
        s = list(s)
        for i in range(len(s) - 2, -1, -1):
            if s[i] < max(s[i + 1:]):
                j = s.index(min([c for c in s[i + 1:] if c > s[i]]))
                s[i], s[j] = s[j], s[i]
                s[i + 1:] = sorted(s[i + 1:])
                print(''.join(s))
                break
        else:
            print("no answer")



