import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os

Bot = commands.Bot(command_prefix='//')
x=0
y=0
q=0
w=0
e=0
r=0
t=0
i=0
o=0
p=0
a=0
s=0
d=0
f=0
g=0
h=0
j=0
z=0
@Bot.event
async def on_ready():
	print('online')

@Bot.command()
async def tutorial(ctx):
	author = ctx.message.author
	await ctx.send('Write: \n //givepoint [nickname] [value] \n //checkbalance [nickname] \n //clearpoint [nickname] [value] \n //allpoints')


@Bot.command()
async def allpoints(ctx):
	global x
	global y
	global q
	global w
	global e
	global r
	global t
	global i
	global o
	global p
	global a
	global s
	global d
	global f
	global g
	global h
	global j
	global z
	                          
	xx='Not Named have: %s points'
	await ctx.send(xx % x )
	xm='KUZNETSOV have: %s points'
	await ctx.send(xm % y)
	xq='s1zer have: %s points'
	await ctx.send(xq % q)
	xw="natasupernova have: %s points"
	await ctx.send(xw % w)
	xe='Smart have: %s points'
	await ctx.send(xe % e)
	xz='Kwinston have: %s points'
	await ctx.send(xz % z)
	xs='fantom have: %s points'
	await ctx.send(xs % s)
	xp='ka1ser have: %s points'
	await ctx.send(xp % p)
	xr='krebetka have: %s points'
	await ctx.send(xr % r)
	xa='MINUTA have: %s points'
	await ctx.send(xa % a)
	xt='askedwool have: %s points'
	await ctx.send(xt % t)
	xi='KentPro have: %s points'
	await ctx.send(xi % i)
	xo='Amega have: %s points'
	await ctx.send(xo % o)

@Bot.command()
async def clearpoint_NotNamed_10(ctx):
	global x
	x=x-10
	xy='He have: %s points'                            
	await ctx.send(xy % x)

@Bot.command()
async def clearpoint_NotNamed_100(ctx):
	global x
	x=x-100
	xy='He have: %s points'                            
	await ctx.send(xy % x)	

@Bot.command()
async def clearpoint_NotNamed_5(ctx):
	global x
	x=x-100
	xy='He have: %s points'                            
	await ctx.send(xy % x)	

@Bot.command()
async def clearpoint_NotNamed_50(ctx):
	global x
	x=x-50
	xy='He have: %s points'                            
	await ctx.send(xy % x)	

@Bot.command()
async def checkbalance_NotNamed(ctx):
	await ctx.send(x)

@Bot.command()
async def givepoint_NotNamed_10(ctx):
	global x
	x=x+10 
	xy='He have: %s points'                            
	await ctx.send(xy % x)

@Bot.command()
async def givepoint_NotNamed_50(ctx):
	global x
	x=x+50 
	xy='He have: %s points'                            
	await ctx.send(xy % x)

@Bot.command()
async def givepoint_NotNamed_100(ctx):
	global x
	x=x+100 
	xy='He have: %s points'                            
	await ctx.send(xy % x)

@Bot.command()
async def givepoint_NotNamed_5(ctx):
	global x
	x=x+5 
	xy='He have: %s points'                            
	await ctx.send(xy % x)







@Bot.command()
async def clearpoint_KUZNETSOV_100(ctx):
	global y
	y=y-100
	xy='He have: %s points'                            
	await ctx.send(xy % y)	

@Bot.command()
async def clearpoint_KUZNETSOV_50(ctx):
	global y
	y=y-50
	xy='He have: %s points'                            
	await ctx.send(xy % y)

@Bot.command()
async def clearpoint_KUZNETSOV_10(ctx):
	global y
	y=y-10
	xy='He have: %s points'                            
	await ctx.send(xy % y)

@Bot.command()
async def clearpoint_KUZNETSOV_5(ctx):
	global y
	y=y-5
	xy='He have: %s points'                            
	await ctx.send(xy % y)

@Bot.command()
async def checkbalance_KUZNETSOV(ctx):
	await ctx.send(y)

@Bot.command()
async def givepoint_KUZNETSOV_5(ctx):
	global y
	y=y+5 
	xy='He have: %s points'                            
	await ctx.send(xy % y)

@Bot.command() 
async def givepoint_KUZNETSOV_10(ctx):
	global y
	y=y+10 
	xy='He have: %s points'                            
	await ctx.send(xy % y)

@Bot.command()
async def givepoint_KUZNETSOV_50(ctx):
	global y
	y=y+50 
	xy='He have: %s points'                            
	await ctx.send(xy % y)

@Bot.command()
async def givepoint_KUZNETSOV_100(ctx):
	global y
	y=y+100 
	xy='He have: %s points'                            
	await ctx.send(xy % y)










@Bot.command()
async def clearpoint_s1zer_5(ctx):
	global q
	q=q-5
	xy='He have: %s points'
	await ctx.send(xy%q)

@Bot.command()
async def clearpoint_s1zer_50(ctx):
	global q
	q=q-50
	xy='He have: %s points'
	await ctx.send(xy%q)

@Bot.command()
async def clearpoint_s1zer_10(ctx):
	global q
	q=q-10
	xy='He have: %s points'
	await ctx.send(xy%q)

@Bot.command()
async def clearpoint_s1zer_100(ctx):
	global q
	q=q-100
	xy='He have: %s points'
	await ctx.send(xy%q)

@Bot.command()
async def checkbalance_s1zer(ctx):
	await ctx.send(q)

@Bot.command()
async def givepoint_s1zer_100(ctx):
	global q
	q=q+100 
	xy='He have: %s points'                            
	await ctx.send(xy % q)

@Bot.command()
async def givepoint_s1zer_10(ctx):
	global q
	q=q+10
	xy='He have: %s points'                            
	await ctx.send(xy % q)

@Bot.command()
async def givepoint_s1zer_5(ctx):
	global q
	q=q+5 
	xy='He have: %s points'                            
	await ctx.send(xy % q)

@Bot.command()
async def givepoint_s1zer_50(ctx):
	global q
	q=q+50 
	xy='He have: %s points'                            
	await ctx.send(xy % q)





@Bot.command()
async def givepoint_natasupernova_100(ctx):
	global w
	w=w+100 
	xy='He have: %s points'                            
	await ctx.send(xy % w)

@Bot.command()
async def givepoint_natasupernova_10(ctx):
	global w
	w=w+10
	xy='He have: %s points'                            
	await ctx.send(xy % w)

@Bot.command()
async def givepoint_natasupernova_5(ctx):
	global w
	w=w+5
	xy='He have: %s points'                            
	await ctx.send(xy % w)

@Bot.command()
async def givepoint_natasupernova_50(ctx):
	global w
	w=w+50
	xy='He have: %s points'                            
	await ctx.send(xy % w)

@Bot.command()
async def checkbalance_natasupernova(ctx):
	await ctx.send(w)

@Bot.command()
async def clearpoint_natasupernova_100(ctx):
	global w
	w=w-100
	xy='He have: %s points'
	await ctx.send(xy%w)

@Bot.command()
async def clearpoint_natasupernova_10(ctx):
	global w
	w=w-10
	xy='He have: %s points'
	await ctx.send(xy%w)

@Bot.command()
async def clearpoint_natasupernova_50(ctx):
	global w
	w=w-50
	xy='He have: %s points'
	await ctx.send(xy%w)

@Bot.command()
async def clearpoint_natasupernova_5(ctx):
	global w
	w=w-5
	xy='He have: %s points'
	await ctx.send(xy%w)






@Bot.command()
async def clearpoint_smart_5(ctx):
	global e
	e=e-5
	xy='He have: %s points'
	await ctx.send(xy%e)\

@Bot.command()
async def clearpoint_smart_50(ctx):
	global e
	e=e-50
	xy='He have: %s points'
	await ctx.send(xy%e)

@Bot.command()
async def clearpoint_smart_10(ctx):
	global e
	e=e-10
	xy='He have: %s points'
	await ctx.send(xy%e)

@Bot.command()
async def clearpoint_smart_100(ctx):
	global e
	e=e-100
	xy='He have: %s points'
	await ctx.send(xy%e)

@Bot.command()
async def checkbalance_smart(ctx):
	await ctx.send(e)

@Bot.command()
async def givepoint_smart_50(ctx):
	global e
	e=e+50
	xy='He have: %s points'                            
	await ctx.send(xy % e)


@Bot.command()
async def givepoint_smart_5(ctx):
	global e
	e=e+5
	xy='He have: %s points'                            
	await ctx.send(xy % e)

@Bot.command()
async def givepoint_smart_10(ctx):
	global e
	e=e+10
	xy='He have: %s points'                            
	await ctx.send(xy % e)

@Bot.command()
async def givepoint_smart_100(ctx):
	global e
	e=e+100
	xy='He have: %s points'                            
	await ctx.send(xy % e)






@Bot.command()
async def givepoint_krebetka_50(ctx):
	global r
	r=r+50
	xy='He have: %s points'                            
	await ctx.send(xy % r)

@Bot.command()
async def givepoint_krebetka_5(ctx):
	global r
	r=r+5
	xy='He have: %s points'                            
	await ctx.send(xy % r)

@Bot.command()
async def givepoint_krebetka_10(ctx):
	global r
	r=r+10
	xy='He have: %s points'                            
	await ctx.send(xy % r)

@Bot.command()
async def givepoint_krebetka_100(ctx):
	global r
	r=r+100
	xy='He have: %s points'                            
	await ctx.send(xy % r)

@Bot.command()
async def checkbalance_krebetka(ctx):
	await ctx.send(r)

@Bot.command()
async def clearpoint_krebetka_50(ctx):
	global r
	r=r-50
	xy='He have: %s points'                            
	await ctx.send(xy % r)

@Bot.command()
async def clearpoint_krebetka_5(ctx):
	global r
	r=r-5
	xy='He have: %s points'                            
	await ctx.send(xy % r)

@Bot.command()
async def clearpoint_krebetka_100(ctx):
	global r
	r=r-100
	xy='He have: %s points'                            
	await ctx.send(xy % r)	

@Bot.command()
async def clearpoint_krebetka_10(ctx):
	global r
	r=r-10
	xy='He have: %s points'                            
	await ctx.send(xy % r)	




@Bot.command()
async def clearpoint_MINUTA_10(ctx):
	global a
	a=a-10
	xy='He have: %s points'                            
	await ctx.send(xy % a)

@Bot.command()
async def clearpoint_MINUTA_100(ctx):
	global a
	a=a-100
	xy='He have: %s points'                            
	await ctx.send(xy % a)

@Bot.command()
async def clearpoint_MINUTA_50(ctx):
	global a
	a=a-50
	xy='He have: %s points'                            
	await ctx.send(xy % a)

@Bot.command()
async def clearpoint_MINUTA_5(ctx):
	global a
	a=a-5
	xy='He have: %s points'                            
	await ctx.send(xy % a)

@Bot.command()
async def checkbalance_MINUTA(ctx):
	await ctx.send(a)

@Bot.command()
async def givepoint_MINUTA_100(ctx):
	global a
	a=a+100
	xy='He have: %s points'                            
	await ctx.send(xy % a)


@Bot.command()
async def givepoint_MINUTA_10(ctx):
	global a
	a=a+10
	xy='He have: %s points'                            
	await ctx.send(xy % a)

@Bot.command()
async def givepoint_MINUTA_50(ctx):
	global a
	a=a+50
	xy='He have: %s points'                            
	await ctx.send(xy % a)

@Bot.command()
async def givepoint_MINUTA_5(ctx):
	global a
	a=a+5
	xy='He have: %s points'                            
	await ctx.send(xy % a)




@Bot.command()
async def givepoint_askedwool_5(ctx):
	global t
	t=t+5
	xy='He have: %s points'                            
	await ctx.send(xy % t)

@Bot.command()
async def givepoint_askedwool_50(ctx):
	global t
	t=t+50
	xy='He have: %s points'                            
	await ctx.send(xy % t)

@Bot.command()
async def givepoint_askedwool_10(ctx):
	global t
	t=t+10
	xy='He have: %s points'                            
	await ctx.send(xy % t)

@Bot.command()
async def givepoint_askedwool_100(ctx):
	global t
	t=t+100
	xy='He have: %s points'                            
	await ctx.send(xy % t)

@Bot.command()
async def checkbalance_askedwool(ctx):
	global t
	await ctx.send(t)

@Bot.command()
async def clearpoint_askedwool_5(ctx):
	global t
	t=t-5
	xy='He have: %s points'                            
	await ctx.send(xy % t)

@Bot.command()
async def clearpoint_askedwool_50(ctx):
	global t
	t=t-50
	xy='He have: %s points'                            
	await ctx.send(xy % t)

@Bot.command()
async def clearpoint_askedwool_10(ctx):
	global t
	t=t-10
	xy='He have: %s points'                            
	await ctx.send(xy % t)

@Bot.command()
async def clearpoint_askedwool_100(ctx):
	global t
	t=t-100
	xy='He have: %s points'                            
	await ctx.send(xy % t)



@Bot.command()
async def clearpoint_KentPro_5(ctx):
	global i
	i=i-5
	xy='He have: %s points'                            
	await ctx.send(xy % i)

@Bot.command()
async def clearpoint_KentPro_50(ctx):
	global i
	i=i-50
	xy='He have: %s points'                            
	await ctx.send(xy % i)

@Bot.command()
async def clearpoint_KentPro_10(ctx):
	global i
	i=i-10
	xy='He have: %s points'                            
	await ctx.send(xy % i)

@Bot.command()
async def clearpoint_KentPro_100(ctx):
	global i
	i=i-100
	xy='He have: %s points'                            
	await ctx.send(xy % i)


@Bot.command()
async def checkbalance_KentPro(ctx):
	global t
	await ctx.send(t)

@Bot.command()
async def givepoint_KentPro_100(ctx):
	global i
	i=i+100
	xy='He have: %s points'                            
	await ctx.send(xy % i)

@Bot.command()
async def givepoint_KentPro_10(ctx):
	global i
	i=i+10
	xy='He have: %s points'                            
	await ctx.send(xy % i)

@Bot.command()
async def givepoint_KentPro_50(ctx):
	global i
	i=i+50
	xy='He have: %s points'                            
	await ctx.send(xy % i)

@Bot.command()
async def givepoint_KentPro_5(ctx):
	global i
	i=i+5
	xy='He have: %s points'                            
	await ctx.send(xy % i)






@Bot.command()
async def givepoint_Amega_5(ctx):
	global o
	o=o+5
	xy='He have: %s points'                            
	await ctx.send(xy % o)

@Bot.command()
async def givepoint_Amega_50(ctx):
	global o
	o=o+50
	xy='He have: %s points'                            
	await ctx.send(xy % o)

@Bot.command()
async def givepoint_Amega_10(ctx):
	global o
	o=o+10
	xy='He have: %s points'                            
	await ctx.send(xy % o)

@Bot.command()
async def givepoint_Amega_100(ctx):
	global o
	o=o+100
	xy='He have: %s points'                            
	await ctx.send(xy % o)

@Bot.command()
async def checkbalance_Amega(ctx):
	global o
	await ctx.send(o)

@Bot.command()
async def clearpoint_Amega_5(ctx):
	global o
	o=o-5
	xy='He have: %s points'                            
	await ctx.send(xy % o)

@Bot.command()
async def clearpoint_Amega_50(ctx):
	global o
	o=o-50
	xy='He have: %s points'                            
	await ctx.send(xy % o)

@Bot.command()
async def clearpoint_Amega_10(ctx):
	global o
	o=o-10
	xy='He have: %s points'                            
	await ctx.send(xy % o)

@Bot.command()
async def clearpoint_Amega_100(ctx):
	global o
	o=o-100
	xy='He have: %s points'                            
	await ctx.send(xy % o)




@Bot.command()
async def clearpoint_ka1ser_5(ctx):
	global p
	p=p-5
	xy='He have: %s points'                            
	await ctx.send(xy % p)


@Bot.command()
async def clearpoint_ka1ser_50(ctx):
	global p
	p=p-50
	xy='He have: %s points'                            
	await ctx.send(xy % p)

@Bot.command()
async def clearpoint_ka1ser_10(ctx):
	global p
	p=p-10
	xy='He have: %s points'                            
	await ctx.send(xy % p)


@Bot.command()
async def clearpoint_ka1ser_100(ctx):
	global p
	p=p-100
	xy='He have: %s points'                            
	await ctx.send(xy % p)

@Bot.command()
async def checkbalance_ka1ser(ctx):
	global p
	await ctx.send(p)

@Bot.command()
async def givepoint_ka1ser_100(ctx):
	global p
	p=p+100
	xy='He have: %s points'                            
	await ctx.send(xy % p)	

@Bot.command()
async def givepoint_ka1ser_10(ctx):
	global p
	p=p+10
	xy='He have: %s points'                            
	await ctx.send(xy % p)	

@Bot.command()
async def givepoint_ka1ser_50(ctx):
	global p
	p=p+50
	xy='He have: %s points'                            
	await ctx.send(xy % p)	

@Bot.command()
async def givepoint_ka1ser_5(ctx):
	global p
	p=p+5
	xy='He have: %s points'                            
	await ctx.send(xy % p)	



@Bot.command()
async def givepoint_fantom_100(ctx):
	global s
	s=s+100
	xy='He have: %s points'                            
	await ctx.send(xy % s)

@Bot.command()
async def givepoint_fantom_10(ctx):
	global s
	s=s+10
	xy='He have: %s points'                            
	await ctx.send(xy % s)

@Bot.command()
async def givepoint_fantom_5(ctx):
	global s
	s=s+5
	xy='He have: %s points'                            
	await ctx.send(xy % s)

@Bot.command()
async def givepoint_fantom_50(ctx):
	global s
	s=s+50
	xy='He have: %s points'                            
	await ctx.send(xy % s)

@Bot.command()
async def checkbalance_fantom(ctx):
	global s
	await ctx.send(s)

@Bot.command()
async def clearpoint_fantom_100(ctx):
	global s
	s=s-100
	xy='He have: %s points'                            
	await ctx.send(xy % s)

@Bot.command()
async def clearpoint_fantom_10(ctx):
	global s
	s=s-10
	xy='He have: %s points'                            
	await ctx.send(xy % s)

@Bot.command()
async def clearpoint_fantom_5(ctx):
	global s
	s=s-5
	xy='He have: %s points'                            
	await ctx.send(xy % s)

@Bot.command()
async def clearpoint_fantom_50(ctx):
	global s
	s=s-50
	xy='He have: %s points'                            
	await ctx.send(xy % s)





@Bot.command()
async def clearpoint_Kwinston_100(ctx):
	global z
	z=z-100
	xy='He have: %s points'                            
	await ctx.send(xy % z)

@Bot.command()
async def clearpoint_Kwinston_5(ctx):
	global z
	z=z-5
	xy='He have: %s points'                            
	await ctx.send(xy % z)

@Bot.command()
async def clearpoint_Kwinston_50(ctx):
	global z
	z=z-50
	xy='He have: %s points'                            
	await ctx.send(xy % z)

@Bot.command()
async def clearpoint_Kwinston_10(ctx):
	global z
	z=z-10
	xy='He have: %s points'                            
	await ctx.send(xy % z)

@Bot.command()
async def checkbalance_Kwinston(ctx):
	global z
	await ctx.send(z)

@Bot.command()
async def givepoint_Kwinston_5(ctx):
	global z
	z=z+5
	xy='He have: %s points'                            
	await ctx.send(xy % z)

@Bot.command()
async def givepoint_Kwinston_50(ctx):
	global z
	z=z+50
	xy='He have: %s points'                            
	await ctx.send(xy % z)

@Bot.command()
async def givepoint_Kwinston_10(ctx):
	global z
	z=z+10
	xy='He have: %s points'                            
	await ctx.send(xy % z)

@Bot.command()
async def givepoint_Kwinston_100(ctx):
	global z
	z=z+100
	xy='He have: %s points'                            
	await ctx.send(xy % z)

token = os.environ.get('BOT_TOKEN')
Bot.run(str(token))
