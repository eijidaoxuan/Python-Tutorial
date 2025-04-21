import re

email = input("Email: ").strip()

if re.search(r"..*@..*\.com", email):
    print("Valid 1")
else:
    pass
if re.search(r".+@.+\.com", email):
    print("Valid 2")
else:
    pass
if re.search(r"[abcdefghijklmnopqrstuvwxyz]@[a-z]+\.com", email):
    print("Valid 3")
else:
    pass
if re.search(r"[a-zA-Z0-9_]+@\w+\.com", email):
    print("Valid 4")
else:
    pass
if re.search(r"[^@|<>]+@[^@ ]+\.com", email):
    print("Valid 5")
else:
    pass
if re.search(r"^\w{5,12}@\w{4,}\.com$", email):
    print("Valid 6")
else:
    pass
if re.search(r"^\w+@\w+\.(com|org|edu)$", email):
    print("Valid 7")
else:
    pass
if re.search(r"^[A-Z0-9_]+@(\w+\.)?\w+\.com$", email, re.IGNORECASE):
    print("Valid 8")
else:
    pass
if match := re.search(r"^([A-Z0-9_]+)@(\w+\.)?(\w+)(\.com)$", email, re.IGNORECASE):
    print("Username:", match.group(1))
    print("Subdomain:", match.group(2))                     #Often used to differentiate between departments, services, or divisions within a company
    print("Second-Level Domain (SLD):", match.group(3))     #Organization, company, or email service provider
    print("Top-Level Domain (TLD):", match.group(4))        #Domain name extension, such as .com, .org, .net, etc.
else:  
    pass
if match := re.search(r"^([A-Z0-9_]+)@(?:\w+\.)?(\w+)(\.com)$", email, re.IGNORECASE):
    print("Gmail:", match.group())                          #Match the entire pattern
    print("Username:", match.group(1))
    print("Second-Level Domain (SLD):", match.group(2))     #Organization, company, or email service provider
    print("Top-Level Domain (TLD):", match.group(3))        #Domain name extension, such as .com, .org, .net, etc.
else:
    pass
if username := email.replace("@gmail.com", ""):             #Replace "@gmail.com" with "" (empty string)
    print("Username:", username)
else:
    pass
if domain := email.removeprefix("JohnDoe@"):                #Remove "JohnDoe@", not work if "JohnDoe@" is not at the beginning of the string
    print("Domain:", domain)
else:
    pass
if username := email.removesuffix("@gmail.com"):            #Remove "@gmail.com", not work if "@gmail.com" is not at the end of the string
    print("Username:", username)
else:
    pass
if username := re.sub(r"@(?:\w+\.)?(\w+)(\.com)$", "", email, count=0, flags=re.IGNORECASE):      #Replace "@(?:\w+\.)?(\w+)(\.com)$" with "" (empty string)    count= how many times to replace, 0 = all
    print("Username:", username)
else:  
    pass

# . = any character except newline
# * = 0 or more repetitions
# + = 1 or more repetitions
# ? = 0 or 1 repetitions
# {m} = m repetitions
# {m,n} = between m and n repetitions

# replacement (.) :
#   [] = any character in the brackets
#   [^] = any character not in the brackets

# ^ = start of string
# $ = end of string

# r"..." = to ignore escape sequences (\)
# \w = any alphanumeric character (a-z, A-Z, 0-9, _) = [a-zA-Z0-9_]
# \W = any non-alphanumeric character
# \s = any whitespace character (space, tab, newline)
# \S = any non-whitespace character
# \d = any digit [0-9]
# \D = any non-digit [^0-9]

# a|b = a or b  (only inside group)
# (?P<name>...) = named capturing group (name = name of the group)
# (...) = capturing group
# (?:...) = non-capturing group

# flags :
#   re.IGNORECASE = ignore case
#   re.MULTILINE = treat string as multiple lines
#   re.DOTALL = treat string as single line (.) matches newline too

# re.match() = match at the beginning of the string
# re.fullmatch() = match the entire string
# re.search() = search anywhere in the string