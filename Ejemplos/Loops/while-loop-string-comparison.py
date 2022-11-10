confirmPrompt = input("Please confirm [Yes/No]: ")

# validate entry; ignore case
while not(confirmPrompt.upper() == "YES" or confirmPrompt.upper() == "NO"):
    confirmPrompt = input("Invalid choice, please re-enter: ")    
else:
    print("Valid choice.")