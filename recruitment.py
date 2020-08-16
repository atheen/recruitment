def main():
	#write your code here
	skills = ["Python", "C++", "JavaScript", "Meeting", "Leeting", "Eating"]
	cv = {}
	print("Welcome to the special recruitment program, please answer the following questions:")
	cv["name"] = input("What's your name? ")
	cv["age"] = input("How old are you? ")
	cv["experience"] = input("How many years of experience do you have? ")
	cv["skills"] = []
	print("\nSkills:")
	n = 1
	for i in skills:
		print("%d. %s"%(n,i))
		n += 1
	first_skill = input("Choose a skill from above by entering its number: ")
	first_index = int(first_skill)-1
	cv["skills"].append(skills[first_index])
	second_skill = input("Choose another skill from above by entering its number: ")
	second_index = int(second_skill)-1
	cv["skills"].append(skills[second_index])

	if int(cv["age"]) >=25 and int(cv["age"]) <=40 and int(cv["experience"]) > 5 and (skills[5] in cv["skills"]):
		print("You have been accepted, %s"%(cv["name"]))
	else:
		print("Sorry %s, you have been rejected"%(cv["name"]))



if __name__ == '__main__':
	main()
