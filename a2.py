# disease rule based expert system IF-THEN

print("---- Disease Diagnosis Expert System ----")

# Taking inputs
fever = input("Do you have fever? (yes/no): ")
cough = input("Do you have cough? (yes/no): ")
rash = input("Do you have rash? (yes/no): ")
headache = input("Do you have headache? (yes/no): ")
vomiting = input("Do you have vomiting? (yes/no): ")

# Applying Rules
if fever == "yes" and cough == "yes":
    print("Diagnosis: You may have Flu.")

elif fever == "yes" and rash == "yes":
    print("Diagnosis: You may have Measles.")

elif headache == "yes" and vomiting == "yes":
    print("Diagnosis: You may have Migraine.")

else:
    print("Diagnosis: Unable to determine disease. Please consult a doctor.")



#     Q1: What is an Expert System?
# An expert system is a computer program designed to simulate the decision-making
# ability of a human expert. It uses stored knowledge and predefined rules to solve
# specific problems. It is widely used in medical, financial, and technical fields.
# Q2: What is Forward Chaining?
# Forward chaining is a reasoning technique used in expert systems. It starts with
# known facts provided by the user. Rules are applied step by step to derive new
# facts. The process continues until a conclusion is reached.
# Q3: What is Backward Chaining?
# Backward chaining is a goal-oriented reasoning method. It begins with a possible
# conclusion or goal. The system checks whether available facts support that goal. It
# works backward until the goal is proven or rejected.
# Q4: What are the advantages?
# Expert systems provide fast and accurate decision-making. They ensure
# consistency in results every time. They are available 24/7 without fatigue. They
# reduce dependency on human experts.
# Q5: What are the limitations?
# Expert systems are limited to predefined rules and knowledge. They cannot think
# creatively like humans. They struggle to handle uncertainty and incomplete data.
# They require regular updates and expert maintenance.