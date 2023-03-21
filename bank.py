# Prompt user for a greeting:
greeting = input("Greeting: ").lower().strip()
#check hello in greeting
if "hello" in greeting:
    print("$0")
#Check the character at position 0 in greeting, if it is "h" print $20 :
elif "h" == greeting[0] :
    print("$20")
else:
    print("$100")