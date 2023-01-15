staff = ["Arshiya", "Usman", "Iftikhar", "Usman", "Anmol","Zainab","Iftikhar", "Arshiya","Jake","Iftikhar"]

def countElement(staff, element):
	return staff.count(element)


sample_list = ["a", "ab", "a", "abc", "ab", "ab"]
element = "ab"
print('{} has occurred {} times'.format(element, countElement(staff, element)))
