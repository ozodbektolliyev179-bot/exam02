def format_name(full_name: str) -> str:
    words = full_name.split()  
    familiya = words[0]        
    ism_sharif = " ".join(words[1:])  
    
    return ism_sharif + ", " + familiya
print(format_name("Aliyev Vali G'aniyevich"))    
