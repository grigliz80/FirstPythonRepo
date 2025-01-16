numbers = [10, 20, 30, 40]

browsers = ['Chrome', 'Safari', 'Mozilla', 'Opera']

months = ['January', 'February', 'March']

mixed = [1, 'two', 3.0, True]

countries =['Ukraine', 'Belarus', 'Mongolia', 'Bangladesh', 'India', 'France', 'Germany', 'Italy']

img = """kjbkjblk dfgsdfg dfg sdgdgfdf fgdg sdfgdfg sdf sd dfgg sd sdfg sdf sdfg sdfg sd sdfgdfg
sdsg sdf dfg fsdg dfg   adfg dfg sdfgdgfd sdfg  fg sdfg sdfgsdsf    sdfgsdf dfg sdfg sd dsfgs sdfgdfg
    dfgsd sdfg dfgsds sdgg f sdfgsd dsfg dfgsd dff  sdfg sdfg sdfgsdfg sdfg sdfgdfg dfgsdf hsfhfg s
sdfg sdfgsdf gfds dfgsdf dfgs dfg   sfhfdg dfghdf dfgh fdgh dfghdfg dfghhgd dfgh dfgh dfgh dfgh dfgh
 dsg dfgs sdfggfs dfgs sdfg sdfgsdf sdfg    s sdfhfsg       dfgs dsfg sdfhsgh sfghs sfhs dfgsdf fsdf
"""

sym_reg = 'abcdefghijklmnopqrstuvwxyz'

quiz_pairs = [
    ["Who was the first president of the United States?", "George Washington"],
    ["When did World War II take place?", "From 1939 to 1945"],
    ["Which civilization built the pyramids in Egypt?", "Ancient Egyptians"],
    ["What is the tallest mountain in the world?", "Mount Everest"],
    ["Which ocean is the largest?", "Pacific Ocean"],
    ["In which country is the Eiffel Tower located?", "France"],
    ["What element has the chemical symbol H?", "Hydrogen"],
    ["Who formulated the theory of relativity?", "Albert Einstein"],
    ["Which planet in the Solar System is known for its rings?", "Saturn"],
    ["Who painted the Mona Lisa?", "Leonardo da Vinci"],
    ["Which instrument is a symbol of classical music?", "Violin"],
    ["What music style originated in New Orleans?", "Jazz"],
    ["Which sport is called the \"king of sports\"?", "Football"],
    ["Who is considered the greatest basketball player of all time?", "Michael Jordan"],
    ["Which type of wrestling is an Olympic sport?", "Greco-Roman wrestling"],
    ["What is the largest mammal on Earth?", "Blue whale"],
    ["Which tree is considered a symbol of Japan?", "Sakura"],
    ["Which bird cannot fly but swims excellently?", "Penguin"]
]


def fib_func(count):
    fib_list = []

    while len(fib_list) < 10:

        if len(fib_list) < 2:
            fib_list.append(count)
            count += 1
        else:
            fib_list.append(fib_list[-1] + fib_list[-2])

    return print(fib_list)

def fib_2(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b,  a + b
    return a




# When there is some side code in the Modulus file - should write it in main function
def main():
    print(fib_2(int(input('What fib do you need?: '))))


if __name__ == '__main__':
    main()