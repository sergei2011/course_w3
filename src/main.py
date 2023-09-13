from src.util import open_list, sort_execut, sort_list, five_last, time, from_out, to_in

q = open_list('../operations.json')
w = sort_execut(q)
e = sort_list(w)
last_pay = five_last(e)

for x in last_pay:
   time_pay = time(x['date'])
   sender = from_out(x)
   receiver = to_in(x)
   print(f"{time_pay}  {x['description']} \n{sender} -> {receiver}\n{x['operationAmount']['amount']} {x['operationAmount']['currency']['name']}\n")


