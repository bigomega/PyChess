import copy


#look done for all eyes...
#big prob with look, it has all positions
class board:
	material="  "
	colour=" "
	flag=0
	eye=[]
	look=[]

def printb(a):
	print "   -----------------------------------------"
	for i in range(8):
		print 8-i," |",a[i][0].material,"|",a[i][1].material,"|",a[i][2].material,"|",a[i][3].material,"|",a[i][4].material,"|",a[i][5].material,"|",a[i][6].material,"|",a[i][7].material,"|"
		print "   -----------------------------------------"
	print "     a    b    c    d    e    f    g    h\n"
	print "White:\n\t",a[9]," score- ",a[11]
	print "Black:\n\t",a[10]," score- ",a[12]
	col="White" if a[13]==0 else "Black"
	print "\n%r to move" %col
#	if a[14]==-1: print "\n*Black WON the match =) gg*\n"
#	if a[14]==1: print "\n*White WON the match =) gg*\n"

def initialise():
	a=[]
	for i in range(8):
		a.append([])
		for j in range(8):
			a[i].append(board())
	a.append(0)#8 check (1 - on white, -1 - black, 0 - no shit)
	a.append([])#9 white defeated coins
	a.append([])#10 black defeated coins
	a.append(0)#11 white score
	a.append(0)#12 black score
	a.append(0)#13 move (0 - white, 1 - black)
	a.append(0)#14 win (1 - white, -1 - black, 0 - no shit)
	a.append([7,4])#15 white king
	a.append([0,4])#16 black king
	a.append([0,0,0])#17 white rk,k,rk castle
	a.append([0,0,0])#18 black rk,k,rk castle
	a.append(0)#19 draw (1 - draw)
	for i in range(8):
		a[1][i].material='p\''
		a[6][i].material='P '
	a[0][0].material=a[0][7].material='r\''
	a[7][0].material=a[7][7].material='R '
	a[0][1].material=a[0][6].material='n\''
	a[7][1].material=a[7][6].material='N '
	a[0][2].material=a[0][5].material='b\''
	a[7][2].material=a[7][5].material='B '
	a[0][3].material='q\''
	a[7][3].material='Q '
	a[0][4].material='k\''
	a[7][4].material='K '
	for i in range(8):
		a[0][i].flag=a[1][i].flag=a[6][i].flag=a[7][i].flag=1
		a[0][i].colour=a[1][i].colour='b'
		a[6][i].colour=a[7][i].colour='w'
	return a

def status(a):
	print "\ncheck: ",a[8],"\nmove: ",a[13],"\nwin: ",a[14],"\nWK: ",a[15],"\nBK: ",a[16],"\n"
#	print "eye of knight 0,1 ",a[1][3].eye,a[2][0].eye,a[2][2].eye,"\neye of knight 0,6 ",a[1][4].eye,a[2][5].eye,a[2][7].eye,"\neye of knight 7,1",a[5][0].eye,a[5][2].eye,a[6][3].eye,"\neye of knight 7,6",a[6][4].eye,a[5][5].eye,a[5][7].eye
#	print "eyes at black king ",a[0][4].eye,"white king ",a[7][4].eye
#	print "eyes at black queen ",a[0][3].eye,"white q ",a[7][3].eye
#	print "eyes at 2,1",a[2][1].eye,"eyes at 2,6",a[2][6].eye
#	print "eyes at 5,1",a[5][1].eye,"eyes at 5,6",a[5][6].eye
	print "look of p 00 ",a[1][0].look,"knight 01",a[0][1].look

def eyep(a,i,j):
	if a[i][j].colour=='w':
		if j>0:
			a[i-1][j-1].eye.append([i,j])
			a[i][j].look.append([i-1,j-1])
		if j<7:
			a[i-1][j+1].eye.append([i,j])
			a[i][j].look.append([i-1,j+1])
		if i>0:
			if a[i-1][j].flag==0:
				a[i][j].look.append([i-1,j])
				if ((i==6) and (a[i-2][j].flag==0)):
					a[i][j].look.append([i-2,j])
	if a[i][j].colour=='b':
		if j>0:
			a[i+1][j-1].eye.append([i,j])
			a[i][j].look.append([i+1,j-1])
		if j<7:
			a[i+1][j+1].eye.append([i,j])
			a[i][j].look.append([i+1,j+1])
		if i<7:
			if a[i+1][j].flag==0:
				a[i][j].look.append([i+1,j])
				if ((i==2) and (a[i+2][j].flag==0)):
					a[i][j].look.append([i+2,j])
	return a

def eyer(a,x,y):
	temp=1
	i=x+1
	while ((temp==1) and (i<8)):
		if a[i][y].flag==1:
			temp=0
		a[i][y].eye.append([x,y])
		a[x][y].look.append([i,y])
		i=i+1
	temp=1
	i=x-1
	while ((temp==1) and (i>-1)):
		if a[i][y].flag==1:
			temp=0
		a[i][y].eye.append([x,y])
		a[x][y].look.append([i,y])
		i=i-1
	temp=1
	i=y+1
	while ((temp==1) and (i<8)):
		if a[x][i].flag==1:
			temp=0
		a[x][i].eye.append([x,y])
		a[x][y].look.append([x,i])
		i=i+1
	temp=1
	i=y-1
	while ((temp==1) and (i>-1)):
		if a[x][i].flag==1:
			temp=0
		a[x][i].eye.append([x,y])
		a[x][y].look.append([x,i])
		i=i-1
	return a

def eyeb(a,x,y):
	temp=1
	i=x+1
	j=y+1
	while ((temp==1) and (i<8) and (j<8)):
		if a[i][j].flag==1:
			temp=0
		a[i][j].eye.append([x,y])
		a[x][y].look.append([i,j])
		i=i+1
		j=j+1
	temp=1
	i=x-1
	j=y+1
	while ((temp==1) and (i>-1) and (j<8)):
		if a[i][j].flag==1:
			temp=0
		a[i][j].eye.append([x,y])
		a[x][y].look.append([i,j])
		i=i-1
		j=j+1
	temp=1
	i=x+1
	j=y-1
	while ((temp==1) and (i<8) and (j>-1)):
		if a[i][j].flag==1:
			temp=0
		a[i][j].eye.append([x,y])
		a[x][y].look.append([i,j])
		i=i+1
		j=j-1	
	temp=1
	i=x-1
	j=y-1
	while ((temp==1) and (i>-1) and (j>-1)):
		if a[i][j].flag==1:
			temp=0
		a[i][j].eye.append([x,y])
		a[x][y].look.append([i,j])
		i=i-1
		j=j-1
	return a

def eyeq(a,x,y):
	return eyer(eyeb(a,x,y),x,y)

def eyek(a,x,y):
	i=x-1
	while ((i<x+2) and (i<8)):
		if i>-1:
			j=y-1
			while ((j<y+2) and (j<8)):
				if ((j>-1) and not ((i==x) and (j==y))):
					a[i][j].eye.append([x,y])
					a[x][y].look.append([i,j])
				j=j+1
		i=i+1
	return a

def eyen(a,x,y):
	#i=x-2
	for i in range(x-2,8):
		if ((i<x+3) and (i>-1)):
			if ((i==x-2) or (i==x+2)): k=0
			elif ((i==x-1) or (i==x+1)): k=1
			else: k=10
			if y-1-k>-1:
				a[i][y-1-k].eye.append([x,y])
				a[x][y].look.append([i,y-1-k])
			if y+1+k<8:
				a[i][y+1+k].eye.append([x,y])
				a[x][y].look.append([i,y+1+k])
			#x=x+1
	return a

def movpp(a,x,y,i,j,k,l):
	if k==0:
		a[x][y].flag=0
		a[i][j].flag=1
		a[i][j].colour=a[x][y].colour
		a[i][j].material=a[x][y].material
		a[x][y].colour=" "
		a[x][y].material="  "
	else:
		a[x][y].flag=0
		a[i][j].flag=1
		n=9 if a[i][j].colour=='w' else 10
		a[n].append(a[i][j].material)
		a[n+2]=a[n+2] + score(a[i][j].material[0])
		a[i][j].colour=a[x][y].colour
		a[i][j].material=a[x][y].material
		a[x][y].colour=" "
		a[x][y].material="  "
	a[13]=l
	return a

def smovpa(a,x,y,i,j):
	if ((a[x][y].colour=='b') and (i>x)):
		if j==y:
			if ((i-x==2) and (x==1) and (a[x+1][y].flag==0) and (a[i][j].flag==0)):
				a=smovpp(a,x,y,i,j,0,0)
			elif ((i-x==1) and (a[i][j].flag==0)):
				a=smovpp(a,x,y,i,j,0,0)
		elif ((i-x==1) and (a[i][j].flag==1) and ((j==y+1) or (j==y-1))):
			a=movpp(a,x,y,i,j,1,0)
	elif ((a[x][y].colour=='w') and (i<x)):
		if j==y:
			if ((x-i==2) and (x==6) and (a[x-1][y].flag==0) and (a[i][j].flag==0)):
				a=movpp(a,x,y,i,j,0,1)
			elif ((x-i==1) and (a[i][j].flag==0)):
				a=movpp(a,x,y,i,j,0,1)
		elif ((x-i==1) and (a[i][j].flag==1) and ((j==y+1) or (j==y-1))):
			a=movpp(a,x,y,i,j,1,1)
	return a


def stap(a,x,y):
	snd=[0,0]
	if a[x][y].material[0]=='p':
		if (x+1<8):
			b=smovpa(copy.deepcopy(a),x,y,x+1,y)
			b=eye(b,0)
			b=check(b)
			if b[8]==0: snd[1]==1
			if y+1<8:
				b=smovpa(copy.deepcopy(a),x,y,x+1,y+1)
				b=eye(b,0)
				b=check(b)
				if b[8]==0: snd[1]==1
			if y-1>-1:
				b=smovpa(copy.deepcopy(a),x,y,x+1,y-1)
				b=eye(b,0)
				b=check(b)
				if b[8]==0: snd[1]==1
		if (x==1):
			b=smovpa(copy.deepcopy(a),x,y,x+2,y)
			b=eye(b,0)
			b=check(b)
			if b[8]==0: snd[1]==1
	
	if a[x][y].material[0]=='P':
		if (x-1>-1):
			b=smovpa(copy.deepcopy(a),x,y,x-1,y)
			b=eye(b,0)
			b=check(b)
			if b[8]==0: snd[1]==1
			if y+1<8:
				b=smovpa(copy.deepcopy(a),x,y,x-1,y+1)
				b=eye(b,0)
				b=check(b)
				if b[8]==0: snd[1]==1
			if y-1>-1:
				b=smovpa(copy.deepcopy(a),x,y,x-1,y-1)
				b=eye(b,0)
				b=check(b)
				if b[8]==0: snd[1]==1
		if (x==7):
			b=smovpa(copy.deepcopy(a),x,y,x-2,y)
			b=eye(b,0)
			b=check(b)
			if b[8]==0: snd[1]==1
		
def check(a):
	for i in (a[15],a[16]):#check condition
		l=i[0]
		m=i[1]
		for k in a[l][m].eye:
			n=k[0]
			o=k[1]
#			print n,',',o,a[n][o].colour,l,",",m,a[l][m].colour
			if ((a[n][o].colour!=a[l][m].colour) and (a[n][o].flag==1)):
				a[8]=1 if a[l][m]=='w' else -1
#				print "check ~~ by ",a[n][o].colour,"on",a[l][m].colour, "from",n,',',o,a[8],'\n'
	return a

def stale(a):
	nop=[0,0]
	a=check(a)
	if a[8]!=0:
		return a
	for x in range(8):
		for y in range(8):
			if ((nop[0]==nop[1]==0) and((a[x][y].material[0]=='p') or (a[x][y].material[0]=='P'))):
				a,nop=stap(a,x,y)
			if ((nop[0]==nop[1]==0) and((a[x][y].material[0]=='r') or (a[x][y].material[0]=='R'))):
				a,nop=stap(a,x,y)
			if ((nop[0]==nop[1]==0) and((a[x][y].material[0]=='n') or (a[x][y].material[0]=='N'))):
				a,nop=stap(a,x,y)
			if ((nop[0]==nop[1]==0) and((a[x][y].material[0]=='b') or (a[x][y].material[0]=='B'))):
				a,nop=stap(a,x,y)
			if ((nop[0]==nop[1]==0) and((a[x][y].material[0]=='q') or (a[x][y].material[0]=='Q'))):
				a,nop=stap(a,x,y)
			if ((nop[0]==nop[1]==0) and((a[x][y].material[0]=='k') or (a[x][y].material[0]=='K'))):
				a,nop=stap(a,x,y)
	if nop[0]==0: 
		print "\nwhite at stale mate\n"
		a[19]=1
	if nop[1]==0: 
		print "\nblack at stale mate\n"
		a[19]=1
	return a

def score(a):
	coins={'p':1,'P':1,'b':3,'B':3,'n':3,'N':3,'r':5,'R':5,'q':9,'Q':9,'k':50,'K':50,'':0}
	return coins[a]

def winmk(a,x,y,i,j):
	temp=0
	for k in a[i][j].eye:
		if((k[0]==x) and (k[1]==y) and (temp==0)):
			if a[i][j].flag==0:
				a[x][y].flag=0
				a[i][j].flag=1
				a[i][j].colour=a[x][y].colour
				a[i][j].material=a[x][y].material
				a[x][y].colour=" "
				a[x][y].material="  "
				a[13]=1-a[13]
				n=15 if a[i][j].colour=='w' else 16
				a[n][0]=i
				a[n][1]=j
			elif a[i][j].colour!=a[x][y].colour:
				a[x][y].flag=0
				a[i][j].flag=1
				n=9 if a[i][j].colour=='w' else 10
				a[n].append(a[i][j].material)
				a[n+2]=a[n+2] + score(a[i][j].material[0])
				a[i][j].colour=a[x][y].colour
				a[i][j].material=a[x][y].material
				a[x][y].colour=" "
				a[x][y].material="  "
				a[13]=1-a[13]
				n=15 if a[i][j].colour=='w' else 16
				a[n][0]=i
				a[n][1]=j
			else: pass
			temp=1
	if temp==0:
		pass
	return a

def movewn(a,x,y,i,j):
	if ((x==i) and (y==j)):
		return
	else:
#		print "innn"
		if ((a[x][y].material[0]=='p') or (a[x][y].material[0]=='P')):
			a=movp(a,x,y,i,j)
#			print "2.1"
		elif ((a[x][y].material[0]=='r') or (a[x][y].material[0]=='R')):
			a=movr(a,x,y,i,j)
#			print "2.2"
		elif ((a[x][y].material[0]=='n') or (a[x][y].material[0]=='N')):
			a=movn(a,x,y,i,j)
#			print "2.3"
		elif ((a[x][y].material[0]=='b') or (a[x][y].material[0]=='B')):
			a=movb(a,x,y,i,j)
#			print "2.4"
		elif ((a[x][y].material[0]=='q') or (a[x][y].material[0]=='Q')):
			a=movq(a,x,y,i,j)
#			print "2.5"
		elif ((a[x][y].material[0]=='k') or (a[x][y].material[0]=='K')):
			a=movk(a,x,y,i,j)
#			print "2.6"
		else: pass
	return a

def chkallmoves(a,c):
	k=1
	coll='w' if a[13]==0 else 'b'
	for i in range(8):
		for j in range(8):
			if ((a[i][j].flag==1) and (a[i][j].colour==coll)):
				for m in a[i][j].look:
					b=movewn(copy.deepcopy(a),i,j,m[0],m[1])
					b=eye(b,0)
					b=check(b)
					if b[8]==0:
						return 0
	return k

def win(a):
	b=check(copy.deepcopy(a))
	if b[8]!=0:
		flag=chkallmoves(copy.deepcopy(a),b[8])
		return flag
	else:
		return 0

	k=0
	for z in (a[15],a[16]):
		k=1 if z==a[15] else -1
		x=z[0]
		y=z[1]
		i=x-1
		pos=0
		chk=0
		mat=0
		while ((i<x+2) and (i<8)):
			if i>-1:
				j=y-1
				while ((j<y+2) and (j<8)):
					if ((j>-1) and (a[i][j].colour!=a[x][y].colour) and not ((i==x) and (j==y))):
						b=winmk(copy.deepcopy(a),x,y,i,j)
						b=eye(b,0)
#						print 'in win after eye',c[i][j].eye
						b=check(b)
						if b[8]==k:
							chk=chk+1
						pos=pos+1
					j=j+1
			i=i+1
#	print pos,chk,k," -pos,chk,k in win"
	if ((pos==chk) and (pos!=0)):
		mat=0-k
	return mat
			

def initeye(a):
	for i in range(8):
		for j in range(8):
			a[i][j].eye=[]
	return a

def eye(a,l):
	a=initeye(a)
	for i in range(8):
		for j in range(8):
			#if a[i][j].flag==1:
				if ((a[i][j].material[0]=='p') or (a[i][j].material[0]=='P')):
					a=eyep(a,i,j) 
#					print "1"
				if ((a[i][j].material[0]=='r') or (a[i][j].material[0]=='R')):
					a=eyer(a,i,j)
#					print "2"
				if ((a[i][j].material[0]=='n') or (a[i][j].material[0]=='N')):
					a=eyen(a,i,j)
#					print "3"
				if ((a[i][j].material[0]=='b') or (a[i][j].material[0]=='B')):
					a=eyeb(a,i,j)
#					print "4"
				if ((a[i][j].material[0]=='q') or (a[i][j].material[0]=='Q')):
					a=eyeq(a,i,j)
#					print "5"
				if ((a[i][j].material[0]=='k') or (a[i][j].material[0]=='K')):
					a=eyek(a,i,j)
#					print "6"
	pri="from mov" if l==0 else "from main"
#	print pri
	if l==1:
		a=check(a)
		if a[8]!=0:
			col="white" if a[8]==1 else "black"
			print "\n*CHECK on %r king*\n" %col
	w=0 #win(a) if l==1 else 0
#	print w,'ta ta daa'
	if w==1: 
		print "\n***************************\nWhite WON the match gg =)\n***************************\n"
		a[14]=1
	if w==-1:
		print "\n***************************\nBlack WON the match gg =)\n***************************\n"
		a[14]=-1
	d=0
#	d=stale(a) if l==1 else 0
	if d==1:
		print "\n*****************************\nThe match ends as DRAW gg =)\n*****************************\n"
		a[19]=1
#	if a[a[15][0]][a[15][1]].material[0]!='K':
#		print "Black wins"
#		a[14]=-1
#	if a[a[16][0]][a[16][1]].material[0]!='k':
#		print "White wins"
#		a[14]=1
	return a

def error():
#	print "\n<>Invalid Move<>\n"
	pass







#THE MOVE STATEMENTS HERE ON
def movpp(a,x,y,i,j,k,l):
	if k==0:
#		print "intoo..."
		a[x][y].flag=0
		a[i][j].flag=1
		a[i][j].colour=a[x][y].colour
		a[i][j].material=a[x][y].material
		a[x][y].colour=" "
		a[x][y].material="  "
	else:
		a[x][y].flag=0
		a[i][j].flag=1
		n=9 if a[i][j].colour=='w' else 10
		a[n].append(a[i][j].material)
		a[n+2]=a[n+2] + score(a[i][j].material[0])
		a[i][j].colour=a[x][y].colour
		a[i][j].material=a[x][y].material
		a[x][y].colour=" "
		a[x][y].material="  "
	if ((i==0) or (i==7)):
		while True:
			print "Choose:\n1.Queen\n2.Castle(rook)\n3.Knight\n4.Bishop\n"
			ch=raw_input("> ")
			ch=int(ch)
			if ch==1:
				a[i][j].material="Q " if a[i][j].colour=='w' else "q\'"
				break
			elif ch==2:
				a[i][j].material="R " if a[i][j].colour=='w' else "r\'"
				break
			elif ch==3:
				a[i][j].material="N " if a[i][j].colour=='w' else "n\'"
				break
			elif ch==4:
				a[i][j].material="B " if a[i][j].colour=='w' else "b\'"
				break
			else: print "choice error\n"
	a[13]=l
	return a

def movpa(a,x,y,i,j):
	if ((a[x][y].colour=='b') and (i>x)):
		if j==y:
			if ((i-x==2) and (x==1) and (a[x+1][y].flag==0) and (a[i][j].flag==0)):
				a=movpp(a,x,y,i,j,0,0)
			elif ((i-x==1) and (a[i][j].flag==0)):
				a=movpp(a,x,y,i,j,0,0)
			else: error()
		elif ((i-x==1) and (a[i][j].flag==1) and (a[i][j].colour=='w') and ((j==y+1) or (j==y-1))):
			a=movpp(a,x,y,i,j,1,0)
		else: error()
	elif ((a[x][y].colour=='w') and (i<x)):
#		print "into..",j,y
		if j==y:
#			print "into..1"
			if ((x-i==2) and (x==6) and (a[x-1][y].flag==0) and (a[i][j].flag==0)):
#				print"into...2"
				a=movpp(a,x,y,i,j,0,1)
			elif ((x-i==1) and (a[i][j].flag==0)):
				a=movpp(a,x,y,i,j,0,1)
			else: error()
		elif ((x-i==1) and (a[i][j].flag==1) and (a[i][j].colour=='b') and ((j==y+1) or (j==y-1))):
			a=movpp(a,x,y,i,j,1,1)
		else: error()
	else: error()
	return a

def movp(a,x,y,i,j):
	b=movpa(copy.deepcopy(a),x,y,i,j)
	b=eye(b,0)
	b=check(b)
	k=1 if b[i][j].colour=='b' else -1
	if ((b[8]==0) or (b[8]==k)):
		a=movpa(a,x,y,i,j)
	else:
		col="white" if a[8]==1 else "black"
		print "\nada that moves brings check to the %r king\n" %col
		error()
	return a

def movrr(a,x,y,i,j):
	temp=0
	for k in a[i][j].eye:
		if((k[0]==x) and (k[1]==y) and (temp==0)):
			if a[i][j].flag==0:
				a[x][y].flag=0
				a[i][j].flag=1
				a[i][j].colour=a[x][y].colour
				a[i][j].material=a[x][y].material
				a[x][y].colour=" "
				a[x][y].material="  "
				a[13]=1-a[13]
				if ((x==0) and (y==0)): a[18][0]=1
				if ((x==0) and (y==7)): a[18][2]=1
				if ((x==7) and (y==0)): a[17][0]=1
				if ((x==7) and (y==7)): a[17][2]=1
			elif a[i][j].colour!=a[x][y].colour:
				a[x][y].flag=0
				a[i][j].flag=1
				n=9 if a[i][j].colour=='w' else 10
				a[n].append(a[i][j].material)
				a[n+2]=a[n+2] + score(a[i][j].material[0])
				a[i][j].colour=a[x][y].colour
				a[i][j].material=a[x][y].material
				a[x][y].colour=" "
				a[x][y].material="  "
				a[13]=1-a[13]
				if ((x==0) and (y==0)): a[18][0]=1
				if ((x==0) and (y==7)): a[18][2]=1
				if ((x==7) and (y==0)): a[17][0]=1
				if ((x==7) and (y==7)): a[17][2]=1
			else: error()
			temp=1
	if temp==0:
		error()
	return a
		
def movr(a,x,y,i,j):
	b=movrr(copy.deepcopy(a),x,y,i,j)
	b=eye(b,0)
	b=check(b)
	k=1 if b[i][j].colour=='b' else -1
	print b[8],x,y,i,j
	if ((b[8]==0) or (b[8]==k)):
		a=movrr(a,x,y,i,j)
	else:
		col="white" if a[8]==1 else "black"
		print "\nwow that moves brings check to the %r king\n" %col
		error()
	return a
	
def movnn(a,x,y,i,j):
	temp=0
	for k in a[i][j].eye:
		if((k[0]==x) and (k[1]==y) and (temp==0)):
			if a[i][j].flag==0:
				a[x][y].flag=0
				a[i][j].flag=1
				a[i][j].colour=a[x][y].colour
				a[i][j].material=a[x][y].material
				a[x][y].colour=" "
				a[x][y].material="  "
				a[13]=1-a[13]
			elif a[i][j].colour!=a[x][y].colour:
				a[x][y].flag=0
				a[i][j].flag=1
				n=9 if a[i][j].colour=='w' else 10
				a[n].append(a[i][j].material)
				a[n+2]=a[n+2] + score(a[i][j].material[0])
				a[i][j].colour=a[x][y].colour
				a[i][j].material=a[x][y].material
				a[x][y].colour=" "
				a[x][y].material="  "
				a[13]=1-a[13]
			else: error()
			temp=1
	if temp==0:
		error()
	return a	

def movn(a,x,y,i,j):
	b=movnn(copy.deepcopy(a),x,y,i,j)
	b=eye(b,0)
	b=check(b)
	k=1 if b[i][j].colour=='b' else -1
	if ((b[8]==0) or (b[8]==k)):
		a=movnn(a,x,y,i,j)
	else:
		col="white" if a[8]==1 else "black"
		print "\nei that moves brings check to the %r king\n" %col
		error()
	return a

def movbb(a,x,y,i,j):
	temp=0
	for k in a[i][j].eye:
		if((k[0]==x) and (k[1]==y) and (temp==0)):
			if a[i][j].flag==0:
				a[x][y].flag=0
				a[i][j].flag=1
				a[i][j].colour=a[x][y].colour
				a[i][j].material=a[x][y].material
				a[x][y].colour=" "
				a[x][y].material="  "
				a[13]=1-a[13]
			elif a[i][j].colour!=a[x][y].colour:
				a[x][y].flag=0
				a[i][j].flag=1
				n=9 if a[i][j].colour=='w' else 10
				a[n].append(a[i][j].material)
				a[n+2]=a[n+2] + score(a[i][j].material[0])
				a[i][j].colour=a[x][y].colour
				a[i][j].material=a[x][y].material
				a[x][y].colour=" "
				a[x][y].material="  "
				a[13]=1-a[13]
			else: error()
			temp=1
	if temp==0:
		error()
	return a

def movb(a,x,y,i,j):
	b=movbb(copy.deepcopy(a),x,y,i,j)
	b=eye(b,0)
	b=check(b)
	print "\n %r"%b[8]
	k=1 if b[i][j].colour=='b' else -1
	if ((b[8]==0) or (b[8]==k)):
		a=movbb(a,x,y,i,j)
	else:
		col="white" if a[8]==1 else "black"
		print "\ndimi that moves brings check to the %r king\n" %col
		error()
	return a

def movqq(a,x,y,i,j):
	temp=0
	for k in a[i][j].eye:
		if((k[0]==x) and (k[1]==y) and (temp==0)):
			if a[i][j].flag==0:
				a[x][y].flag=0
				a[i][j].flag=1
				a[i][j].colour=a[x][y].colour
				a[i][j].material=a[x][y].material
				a[x][y].colour=" "
				a[x][y].material="  "
				a[13]=1-a[13]
			elif a[i][j].colour!=a[x][y].colour:
				a[x][y].flag=0
				a[i][j].flag=1
				n=9 if a[i][j].colour=='w' else 10
				a[n].append(a[i][j].material)
				a[n+2]=a[n+2] + score(a[i][j].material[0])
				a[i][j].colour=a[x][y].colour
				a[i][j].material=a[x][y].material
				a[x][y].colour=" "
				a[x][y].material="  "
				a[13]=1-a[13]
			else: error()
			temp=1
	if temp==0:
		error()
	return a

def movq(a,x,y,i,j):
	b=movqq(copy.deepcopy(a),x,y,i,j)
	b=eye(b,0)
	b=check(b)
	k=1 if b[i][j].colour=='b' else -1
	print b[8],k
	if ((b[8]==0) or (b[8]==k)):
		a=movqq(a,x,y,i,j)
	else:
		col="white" if a[8]==1 else "black"
		print "\ndo that moves brings check to the %r king\n" %col
		error()
	return a

def movkk(a,x,y,i,j):
	temp=0
	for k in a[i][j].eye:
		if((k[0]==x) and (k[1]==y) and (temp==0)):
			if a[i][j].flag==0:
				a[x][y].flag=0
				a[i][j].flag=1
				a[i][j].colour=a[x][y].colour
				a[i][j].material=a[x][y].material
				a[x][y].colour=" "
				a[x][y].material="  "
				a[13]=1-a[13]
				n=15 if a[i][j].colour=='w' else 16
				a[n][0]=i
				a[n][1]=j
				if ((x==0) and (y==4)): a[18][1]=1
				if ((x==7) and (y==4)): a[17][1]=1
			elif a[i][j].colour!=a[x][y].colour:
				a[x][y].flag=0
				a[i][j].flag=1
				n=9 if a[i][j].colour=='w' else 10
				a[n].append(a[i][j].material)
				a[n+2]=a[n+2] + score(a[i][j].material[0])
				a[i][j].colour=a[x][y].colour
				a[i][j].material=a[x][y].material
				a[x][y].colour=" "
				a[x][y].material="  "
				a[13]=1-a[13]
				n=15 if a[i][j].colour=='w' else 16
				a[n][0]=i
				a[n][1]=j
				if ((x==0) and (y==4)): a[18][1]=1
				if ((x==7) and (y==4)): a[17][1]=1
			else: error()
			temp=1
	if temp==0:
		error()
	return a

def castlee(a,x,k,l):
	col=a[x][4].colour
	rook='r\'' if col=='b' else 'R '
	a[x][k].material=a[x][4].material
	a[x][k+l].material=rook
	a[x][k].flag=a[x][k+l].flag=1
	a[x][k].colour=a[x][k+l].colour=col
	a[13]=1-a[13]
	n=15 if a[i][j].colour=='w' else 16
	a[n][0]=x
	a[n][1]=k
	m=17 if x==7 else 18
	a[m][1]=1
	if l==-1:
		a[x][7].flag=a[x][4].flag=0
		a[x][7].material=a[x][4].material="  "
		a[x][7].colour=a[x][4].colour=' '
		a[m][2]=1
	if l==1:
		a[x][0].flag=a[x][1].flag=a[x][4].flag=0
		a[x][0].material=a[x][1].material=a[x][4].material="  "
		a[x][0].colour=a[x][1].colour=a[x][4].colour=' '
		a[m][0]=1
	return a

def castle(a,x,y,i,j):
	l=17 if x==7 else 18
	if(j==6):
		if ((a[x][7].material[0]!='r') and (a[x][7].material[0]!='R')):
			print "\nRook not found, castle not possible\n"
			return a
		if ((a[l][1]==1) or (a[l][2]==1)):
			print "\nmovement made, castle not possible\n"
			return a
		for k in (5,6):
			if a[x][k].flag==1:
				error()
				return a
		chk=0
		for k in (4,5,6,7):
			for m in a[x][k].eye:
				n=m[0]
				o=m[1]
#				print n,o,a[n][o].colour,a[n][o].flag
				if ((a[n][o].colour!=a[x][4].colour) and (a[n][o].flag==1)):
					chk=1
		if chk==1:
			print "\ncoins or positions being eyed, castle not possibel\n"
			return a
		a=castlee(a,x,j,-1)
		
	if(j==2):
		if ((a[x][0].material[0]!='r') and (a[x][0].material[0]!='R')):
			print "\nRook not found, castle not possible\n"
			return a
		if ((a[l][1]==1) or (a[l][0]==1)):
			print "\nmovement made, castle not possible\n"
			return a
		for k in (1,2,3):
			if a[x][k].flag==1:
				error()
				return a
		chk=0
		for k in (0,2,3,4):
			for m in a[x][k].eye:
				n=m[0]
				o=m[1]
				if ((a[n][o].colour!=a[x][4].colour) and (a[n][o].flag==1)):
					chk=1
		if chk==1:
			print "\ncoins or positions being eyed, castle not possibel\n"
			return a
		a=castlee(a,x,j,1)	
	return a

def movk(a,x,y,i,j):
	if (((x==i==0) or (x==i==7)) and ((j==6) or (j==2)) and (y==4)): 
		a=castle(a,x,y,i,j)
		return a
	b=movkk(copy.deepcopy(a),x,y,i,j)
	b=eye(b,0)
	b=check(b)
	k=1 if b[i][j].colour=='b' else -1
	if ((b[8]==0) or (b[8]==k)):
		a=movkk(a,x,y,i,j)
	else:
		col="white" if a[8]==1 else "black"
		print "\ncha that moves brings check to the %r king\n" %col
		error()
	return a

def move(a,x,y,i,j):
	if a[x][y].flag==0:
		print "no coin there"
		error()
	elif ((x==i) and (y==j)):
		print "same spot"
		error()
	elif ((a[x][y].colour=='b') and (a[13]==0)):
		print "its white to move"
		error()	
	elif ((a[x][y].colour=='w') and (a[13]==1)):
		print "its black to move"
		error()
	else:
#		print "innn"
		if ((a[x][y].material[0]=='p') or (a[x][y].material[0]=='P')):
			a=movp(a,x,y,i,j)
#			print "2.1"
		elif ((a[x][y].material[0]=='r') or (a[x][y].material[0]=='R')):
			a=movr(a,x,y,i,j)
#			print "2.2"
		elif ((a[x][y].material[0]=='n') or (a[x][y].material[0]=='N')):
			a=movn(a,x,y,i,j)
#			print "2.3"
		elif ((a[x][y].material[0]=='b') or (a[x][y].material[0]=='B')):
			a=movb(a,x,y,i,j)
#			print "2.4"
		elif ((a[x][y].material[0]=='q') or (a[x][y].material[0]=='Q')):
			a=movq(a,x,y,i,j)
#			print "2.5"
		elif ((a[x][y].material[0]=='k') or (a[x][y].material[0]=='K')):
			a=movk(a,x,y,i,j)
#			print "2.6"
		else: pass
	return a

def index(inp):
	pos={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
	if(((inp[0]=='a') or (inp[0]=='b') or (inp[0]=='c') or (inp[0]=='d') or (inp[0]=='e') or (inp[0]=='f') or (inp[0]=='g') or (inp[0]=='h')) and ((inp[1]=='1') or (inp[1]=='2') or (inp[1]=='3') or (inp[1]=='4') or (inp[1]=='5') or (inp[1]=='6') or (inp[1]=='7') or (inp[1]=='8'))):
		j=pos[inp[0]]
		i=int(inp[1])
		i=8-i
	else:
		i=j=9
	return i,j

def backdoor(a):
	for i in range(8):
		for j in range(8):
			if ((a[i][j].colour=='w') and (a[i][j].material!="K ")):
				a[i][j].material="Q "
	printb(a)



a=initialise()
printb(a)
a=eye(a,1)
#castle check
#for k in (4,5,6,7):
#		for m in a[0][k].eye:
#			n=m[0]
#			o=m[1]
#			if ((a[n][o].colour!=a[0][k].colour) and (a[n][o].flag==1)):
#				chk=1			
status(a)
#print a[5][0].eye
while ((a[14]==0) and (a[19]==0)):
	inp1=raw_input("\nEnter from position(in small case): ")
	inp2=raw_input("Enter to position(in small case): ")
	if ((inp1=='') or(inp2=='')):
		print 'huh?'
		continue
	if (inp1[0]=='.'):
		print "\nbackdoor"
		backdoor(a)
		continue
	if (inp1[0]=='/'):
		print "you resigned"
		break
	x,y=index(inp1)
	i,j=index(inp2)
#	print x,y,i,j
	if ((x==9) or (i==9)): 
		print "\nMan look at the co-ordinates and give some reasonable positions"
		continue	
	temp=a[13]
#	print a[x][y].colour,a[i][j].flag,a[i][j].eye,a[8]
	a=move(a,x,y,i,j)
#	print"--\n--\n",a[13]
#	status(a)
	a=eye(a,1)
	if a[13]!=temp:
		printb(a)
	else: print "poda mokka payale... \n invalid move"
print "match ends"
	
