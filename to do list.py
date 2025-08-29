todo = []
while True:
    task= input ("new work:")
    if task== ("exit") :
        break
    todo.append(task)

print("\n today lists:")   
for i , t in enumerate (todo, 1):
    print(f"{i}.{t}")