import yfinance                                           # (1)
tic = "QAN.AX"                                            # (2)
start = '2020-01-01'                                      # (3)
end = None                                                # (4)
df = yfinance.download(tic, start, end, ignore_tz=True)   # (5)
print(df)                                                 # (6)
df.to_csv('qan_stk_prc.csv')

a=1
print(a)


x= 1+2
print (x)

x=1
x=2+x
print(x)

#variables cant start with number - error
#2x = 1

#1=x error
#print (x)
