def http_status(status):
    match status:
        case 200:
            return "Ok" # If the value is 200 then Prints "Ok"
        
        case 404:
            return "Not found" # If the value is 404 then Prints "Not found"
        
        case 500:
            return "Internal server error" # If the value is 500 then Prints "Internal server error"
        
        case _:
            return "Unknown status" # If the value is not match or blank then Prints "Unknown status"
        
print(http_status(200)) # Prints "Ok"
print(http_status(404)) # Prints "Not found"
print(http_status(500)) # Prints "Internal server error"
print(http_status(721)) # Prints "Unknown status"