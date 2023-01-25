#!/usr/bin/python3

# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 # counter for fails
loginok= 0 # counter for successfully


# open the file for reading
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:

    # loop over the file
    for line in kfile:
        # if this 'fail pattern' appears in the line...
        if "- - - - -] Authorization failed" in line:
            loginfail += 1 # this is the same as loginfail = loginfail + 1
            # Separate string into list, then IP is the last item in the list
            print(line)
            print("Failed login is from IP: " +line.split(" ")[-1])
        # if this POST pattern appears in the line...
        elif "-] Authorization failed" in line:
            loginok += 1
            print("Successful login is from IP: " +line.split(" ")[-1])

print("The number of failed log in attempts is", loginfail)
print("The number of succeed log in attempts is", loginok)

