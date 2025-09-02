from datetime import datetime, timezone

print(datetime.now())

def log(msg, *, dt=datetime.now()):
    print(f"{dt}: {msg}")

log("Olá")
log("Como vai ?")

def log(msg, *, dt=None):
    dt = dt or datetime.now()
    print(f"{dt}: {msg}")

log("message 1")
log("message 2")
log("message 3")
log("message 4", dt=datetime.now(timezone.utc))

my_list = [1, 2, 3]
def func(a=my_list):
    print(a)

func()
func(['a', 'b'])
my_list.append(4)
func()
