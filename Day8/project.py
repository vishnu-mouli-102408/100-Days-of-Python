#  Ceaser cypher

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser(direction, text_string, shift):
    newText=""
    if direction == "decrypt":
        shift *= -1;
    for letter in text_string:
        if letter in alphabets:
            position = alphabets.index(letter);
            new_position = position + shift
            newText += alphabets[new_position]
        else:
            newText += letter    
    print(f"Your {direction}d text is {newText}")    


should_continue = True;

while should_continue:
    direction = input("Enter encrypt to encrypt the message or decrypt to decrypt: ")

    text = input("Enter your text: ").lower()

    shift = int(input("Enter your shift number: "))
    shift %= 26



    ceaser(direction, text, shift)   

    x = input("Type yes to continue or no to stop: ").lower()
    if x == "no":
        should_continue = False
        print("Good Bye")



 
