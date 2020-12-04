import re


# Load file
def validate(file, strict):
    count = 0
    with open(file) as file:
        person = 0
        passport = dict()
        for line in file:

            # line = fileline.strip('\n')
            if line == '\n':
                # print(person)

                if 'byr' in passport.keys() and 'iyr' in passport.keys() and 'eyr' in passport.keys() and 'hgt' in passport.keys() and 'hcl' in passport.keys() and 'ecl' in passport.keys() and 'pid' in passport.keys():
                    valid = 0

                    if int(passport['byr']) < 1920:
                        valid = 1
                    if int(passport['byr']) > 2002:
                        valid = 1

                    if int(passport['iyr']) < 2010:
                        valid = 1
                    if int(passport['iyr']) > 2020:
                        valid = 1

                    if int(passport['eyr']) < 2020:
                        valid = 1
                    if int(passport['eyr']) > 2030:
                        valid = 1

                    if not re.match('.*cm|.*in', passport['hgt']):
                        valid = 1
                    if re.match('.*cm', passport['hgt']):
                        height = passport['hgt'].strip('cm')
                        if 193 > int(height) < 150:
                            valid = 1
                    if re.match('.*in', passport['hgt']):
                        height = passport['hgt'].strip('in')
                        if 76 > int(height) < 59:
                            valid = 1

                    if not re.match('#[0-9a-f]{6}', passport['hcl']):
                        valid = 1
                    if not re.match('amb|blu|brn|gry|grn|hzl|oth', passport['ecl']):
                        valid = 1
                    if not re.match('[0-9]{9}', passport['pid']):
                        valid = 1
                    if re.match('[0-9]{10}', passport['pid']):
                        valid = 1
                    if strict == True and valid == 0:
                        count = count + 1
                        # print(str(passport['byr']) + "    " + str(passport['iyr'] )+ "    " + str(passport['eyr'])+ "    " + str(passport['pid']) + "    " + str(passport['hcl'])+ "    " + str(passport['ecl'])+ "    " + str(passport['hgt']))
                    if not strict:
                        count = count + 1
                passport = {}

                person = person + 1
            else:
                line = line.strip('\n')
                fields = line.split(' ')
                for field in fields:
                    field2 = field.split(':')
                    # print(field2[0] + " " + field2[1])
                    passport[field2[0]] = field2[1]

    return count


# Load file
file = 'Day4/day4.txt'
# Part 1
count = validate(file, False)
print(count)

# Part 2
count = validate(file, True)
print(count)
