public class Bank {

    private long[] bal;
    private int n;

    public Bank(long[] balance) {
        bal = balance;
        n = balance.Length;
    }

    public bool isvalid(int account){
        return account>=1 && account<=n;
    }
    
    public bool Transfer(int account1, int account2, long money) {
        if(!isvalid(account1) || !isvalid(account2) || bal[account1-1]<money)
            return false;
        bal[account1-1]-=money;
        bal[account2-1]+=money;   
        return true;
    }
    public bool Deposit(int account, long money) {
        if(!isvalid(account)) return false;
        bal[account-1]+=money;
        return true;
    }
    
    public bool Withdraw(int account, long money) {
        if(!isvalid(account) || bal[account-1]<money) return false;
        bal[account-1]-=money;
        return true;
    }
}
