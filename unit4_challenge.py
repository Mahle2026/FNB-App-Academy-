# Smart ATM Withdrawal Simulator

#Fixed bank balance
balance = 500

#Ask user for Withdrawal amount
withdrawal = float(input("Enter amount  to withdraw: R"))

#Check withdrawal conditions
if withdrawal <= balance and withdrawal > 0:
  balance -=withdrawal
  print(f"Withdrawal successful! Remaining balance: R{balance}")
elif withdrawal <=0:
  print("Invalid amount. You must withdraw more than R0.")
else:
  print("Decline. Insufficient funds.")
  