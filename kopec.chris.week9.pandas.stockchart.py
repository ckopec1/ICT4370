import pandas as pd
import matplotlib.pyplot as plt


SPY_path = r'/home/jovyan/demo/SPY.csv'
AIG_path = r'/home/jovyan/demo/AIG.csv'
F_path = r'/home/jovyan/demo/F.csv'
FB_path = r'/home/jovyan/demo/FB.csv'
GOOG_path = r'/home/jovyan/demo/GOOG.csv'
IBM_path = r'/home/jovyan/demo/IBM.csv'
M_path = r'/home/jovyan/demo/M.csv'
MSFT_path = r'/home/jovyan/demo/MSFT.csv'
RDS_path = r'/home/jovyan/demo/RDS-A.csv'

df_SPY = pd.read_csv(SPY_path)
df_owners_SPY = pd.DataFrame(df_SPY,columns=['Date','Open','High','Low','Close','Adj','Close'])
#print(df_owners_SPY)

df_AIG = pd.read_csv(AIG_path)
df_owners_AIG = pd.DataFrame(df_AIG,columns=['Date','Open','High','Low','Close','Adj','Close'])
#print(df_owners_AIG)

df_F = pd.read_csv(F_path)
df_owners_F = pd.DataFrame(df_F,columns=['Date','Open','High','Low','Close','Adj','Close'])
#print(df_owners_F)

df_FB = pd.read_csv(FB_path)
df_owners_F = pd.DataFrame(df_FB,columns=['Date','Open','High','Low','Close','Adj','Close'])
#print(df_owners_FB)

df_GOOG = pd.read_csv(GOOG_path)
df_owners_F = pd.DataFrame(df_GOOG,columns=['Date','Open','High','Low','Close','Adj','Close'])
#print(df_owners_GOOG)

df_IBM = pd.read_csv(IBM_path)
df_owners_IBM = pd.DataFrame(df_IBM,columns=['Date','Open','High','Low','Close','Adj','Close'])
#print(df_owners_IBM)

df_M = pd.read_csv(M_path)
df_owners_M = pd.DataFrame(df_M,columns=['Date','Open','High','Low','Close','Adj','Close'])
#print(df_owners_M)

df_MSFT = pd.read_csv(MSFT_path)
df_owners_MSFT = pd.DataFrame(df_MSFT,columns=['Date','Open','High','Low','Close','Adj','Close'])
#print(df_owners_MSFT)

df_RDS = pd.read_csv(RDS_path)
df_owners_RDS = pd.DataFrame(df_RDS,columns=['Date','Open','High','Low','Close','Adj','Close'])
#print(df_owners_RDS)

print("SPY average: " + str(df_SPY['Close'].mean()))
print("AIG average: " + str(df_AIG['Close'].mean()))
print("F average: " + str(df_F['Close'].mean()))
print("FB average: " + str(df_FB['Close'].mean()))
print("GOOG average: " + str(df_GOOG['Close'].mean()))
print("IBM average: " + str(df_IBM['Close'].mean()))
print("M average: " + str(df_M['Close'].mean()))
print("MSFT average: " + str(df_MSFT['Close'].mean()))
print("RDS average: " + str(df_RDS['Close'].mean()))
print("\n")
print("SPY average: " + str(df_SPY['Close'].std()))
print("AIG average: " + str(df_AIG['Close'].std()))
print("F average: " + str(df_F['Close'].std()))
print("FB average: " + str(df_FB['Close'].std()))
print("GOOG average: " + str(df_GOOG['Close'].std()))
print("IBM average: " + str(df_IBM['Close'].std()))
print("M average: " + str(df_M['Close'].std()))
print("MSFT average: " + str(df_MSFT['Close'].std()))
print("RDS average: " + str(df_RDS['Close'].std()))
print("\n")
print("AIG Correlation: " + str(df_AIG['Close'].corr(df_SPY['Close'])))
print("F Correlation: " + str(df_F['Close'].corr(df_SPY['Close'])))
print("FB Correlation: " + str(df_FB['Close'].corr(df_SPY['Close'])))
print("GOOG Correlation: " + str(df_GOOG['Close'].corr(df_SPY['Close'])))
print("IBM Correlation: " + str(df_IBM['Close'].corr(df_SPY['Close'])))
print("M Correlation: " + str(df_M['Close'].corr(df_SPY['Close'])))
print("MSFT Correlation: " + str(df_MSFT['Close'].corr(df_SPY['Close'])))
print("RDS Correlation: " + str(df_RDS['Close'].corr(df_SPY['Close'])))

plt.plot(df_AIG['Date'],df_AIG['Close'])
plt.plot(df_F['Date'],df_F['Close'])
plt.plot(df_FB['Date'],df_FB['Close'])
plt.plot(df_GOOG['Date'],df_GOOG['Close'])
plt.plot(df_IBM['Date'],df_IBM['Close'])
plt.plot(df_M['Date'],df_M['Close'])
plt.plot(df_MSFT['Date'],df_MSFT['Close'])
plt.plot(df_RDS['Date'],df_RDS['Close'])
plt.title('Stock Data')
#plt.legend(df_M, loc='upper left', prop={'size': 6})
plt.xlabel('Date')
plt.ylabel('Value')
#plt.xticks(df_M)
plt.show()