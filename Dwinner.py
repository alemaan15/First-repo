game = [[2, 0, 2],
	    [1, 2, 0],
	    [2, 2, 0],]


diag = []
for ix in range(len(game)):
	diag.append(game[ix][ix])
print(diag)

diags = []
for i in reversed(range(len(game))):
	diags.append(game[len(game)-i-1][i])
print(diags)

if diag.count(diag[0])==len(diag) and diag[0]!=0:
	print("Winnerrr")

if diags.count(diags[0])==len(diags) and diags[0]!=0:
	print("Winnerrr")

print("Game finshed")