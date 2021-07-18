game = [[2, 0, 2],
	    [1, 2, 0],
	    [2, 2, 0],]

#Diagonal
diag = []
for ix in range(len(game)):
	diag.append(game[ix][ix])

diags = []
for i in reversed(range(len(game))):
	diags.append(game[len(game)-i-1][i])

if diag.count(diag[0])==len(diag) and diag[0]!=0:
	print("Diagonal Winnerrr")

if diags.count(diags[0])==len(diags) and diags[0]!=0:
	print("Diagonal Winnerrr")

#Vertical
for col in range(len(game)):
	check = []

	for row in game:
		check.append(row[col])

	if check.count(check[0]) == len(check) and check[0]!=0:
				print("Vertical Winnerrr!")

#Vertical
for row in game:
		
		if row.count(row[0]) == len(row) and row[0]!=0:
			print("Vertical Winnerrr!")