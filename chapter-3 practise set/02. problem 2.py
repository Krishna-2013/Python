letter = ''' Dear <|Name|>,
 You are selected! 
 <|Date|>'''

print(letter.replace("<|Name|>", "Harry").replace("<|Date|>","13 May 2013"))