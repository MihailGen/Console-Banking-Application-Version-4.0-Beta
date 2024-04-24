import datetime
import os.path


# Writing postponed payment to file login.postponed.txt
def  postponed_to_file(login_sender, login_rec, summ):
    if check_log(login_rec):
        if not os.path.isdir('postponed_payments'):
            try:
                os.mkdir('postponed_payments')
            except FileExistsError:
                print('Error! Please contact an administrator.')
                return False
        try:
            # writing in the end of file if the file exist
            with open('postponed_payments/' + login_sender + '.' + 'postponed.txt', 'r+') as pstpnd:
                pstpnd.seek(0, 2)
                pstpnd.write(login_rec + "\n")
                pstpnd.write(summ + "\n")
        except FileNotFoundError:
            # if the file not exist creating new file and writing in the beginning
            try:
                with open('postponed_payments/' + login_sender + '.' + 'postponed.txt', 'w') as pstpnd:
                    pstpnd.write(login_rec + "\n")
                    pstpnd.write(summ + "\n")
            except FileNotFoundError:
                print('Error! Please contact an administrator.')
                return False
        return True
    else:
        return False


# Reading Hash from file
def check_login_and_passw(login, passw):
    if check_log(login):
        try:
            with open('bank_clients/' + login + '.' + 'passwordhash.txt') as file_hash:
                if hash_funct(passw) == file_hash.readline():
                    file_hash.close()
                else:
                    print('Incorrect password\n')
                    return False
        except FileNotFoundError:
            print('A system error has occurred!\n Please contact an administrator.\n')
            return False
    return True


# Writing Hash for password in to file login.passwordhash.txt
def hash_to_file(hsh, login):
    if not os.path.isdir('bank_clients'):
        try:
            os.mkdir('bank_clients')
        except FileExistsError:
            print('Error! Please contact an administrator.')
            return False
    try:
        with open('bank_clients/' + login + '.' + 'passwordhash.txt', 'w') as pswd_hsh:
            pswd_hsh.write(hsh)
    except FileNotFoundError:
        print('Error! Please contact an administrator.')
        return False
    return True


# Checking login
def check_log(login):
    if not os.path.isfile('bank_clients/' + login + '.' + 'passwordhash.txt'):
        print('Unknown login! Please contact an administrator.\n')
        return False
    return True


# Create Hash for password
def hash_funct(pswd):
    summ = 0
    mult = 0
    CONST_FOR_HASH = 68429
    for i in range(len(pswd)):
        summ += ord(pswd[i])
        # print(str(i))
        if i == 0:
            mult = ord(pswd[i])
        else:
            mult = mult * ord(pswd[i])
    summ = summ % CONST_FOR_HASH
    mult = mult % CONST_FOR_HASH
    return str(summ) + str(mult)


# Creating path for transactions filtering
def trans_filtering(trans):
    for comment_tr, amount_tr in trans.items():
        yield comment_tr, amount_tr
    return True


# Realize logics for transactions filtering
# Work with path, created in "trans_filtering" function
def trans_filtering_logics(trans, filter_trans):
    for comment_in_tr, amount_in_tr in trans_filtering(trans):
        if amount_in_tr >= filter_trans:
            print(comment_in_tr + ": " + str(amount_in_tr) + " rubl")
    return True


# new client creation procedure
def account_creation():
    flag = True
    if __name__ == "__main__":
        name = input("Enter your name: ")
        surname = input("Enter your surname: ")
    else:
        name = "Test"
        surname = "Test"
    login = name + surname
    try:
        if __name__ == "__main__":
            year_of_birth = int(input("Enter your year of birth: "))
        else:
            year_of_birth = 0
    except ValueError:
        print("Please enter a number\nThe new client is`nt created\nPlease try again\n")
        flag = False
        return flag
    if flag:
        if __name__ == "__main__":
            password = input("Enter your password: ")
        else:
            password = "Test"
        hash_to_file(hash_funct(password), login)
        clientfout(name, surname, year_of_birth, password, 1_000, 0)  # 1000 - beginning limit.
        # 0 - beginning money balance
        print("Congratulation!!!\nYou have successfully created new account\nYour login:  " + login + "\n")
    return flag


# Money addition
def moneyadd(money_func, bill_func, acc_limit):
    if (money_func + bill_func) > acc_limit:
        print("The limit on your account has been exceeded!\nOperation canceled")
    else:
        money_func += bill_func
        print("Account has been successfully added!\n")
    return money_func


# Money withdraw function
def money_withdr(money_witdrw, bill_withdr):
    print("Your current balance is: " + str(money_witdrw))
    if (money_witdrw - bill_withdr) < 0:
        print("You do not have enough money\nto complete this operation")
    else:
        money_witdrw -= bill_withdr
        print("Withdrawal completed successfully")
        print("Your current balance is: " + str(money_witdrw) + "\n")
    return money_witdrw


# Apply transactions
def apply_trans(money_in_account, limit_account, transactions_func):
    for comment_apply, amount_apply in transactions_func.items():
        if (money_in_account + int(amount_apply)) > limit_account:
            print("Transaction: " + comment_apply + "\ncannot be applied (limit exceeded)\n")
        else:
            if int(transactions_func[comment_apply]) > 0:
                money_in_account += int(amount_apply)
                print("Transaction: " + comment_apply + "\nsuccessfully applied\n")
                transactions_func[comment_apply] = 0
    transactionfout(transactions)  # Commented for Test only
    return money_in_account


# Writing information about client in to file
def clientfout(name_to_file, surname_to_file, year_of_birth_to_file, password_to_file, account_limit_to_file,
               money_to_file):
    with open('bank_client.txt', 'w') as fout:
        fout.write(name_to_file + '\n')
        fout.write(surname_to_file + '\n')
        fout.write(str(year_of_birth_to_file) + '\n')
        fout.write(password_to_file + '\n')
        fout.write(str(account_limit_to_file) + '\n')
        fout.write(str(money_to_file) + '\n')
    fout.close()


# Password checking
def pass_check(passwd_tmp, password_fail):
    if password_fail != passwd_tmp or not password_fail:
        print("Wrong password!")
        return False
    else:
        return True


# Reading client data from file to program
def client_from_file():
    try:
        with open('bank_client.txt') as clientfin:
            count = 0
            for line in clientfin:
                count = count + 1
                if count == 1:
                    name = line[:-1]
                elif count == 2:
                    surname = line[:-1]
                elif count == 3:
                    year_of_birth = int(line[:-1])
                elif count == 4:
                    password = line[:-1]
                elif count == 5:
                    account_limit = int(line[:-1])
                elif count == 6:
                    money_from_file = int(line[:-1])
    except FileNotFoundError:
        print("Your bank data is lost!\nPlease contact to the bank administration!")
        exit()
    clientfin.close()
    try:
        client_from_file_kortezh = (name, surname, year_of_birth, password, account_limit, money_from_file)
    except UnboundLocalError:
        print("Your bank data is lost!\nPlease contact to the bank administration!")
        exit()
    return client_from_file_kortezh


# Reading transaction from file to dictionary
def transaction_from_file():
    transactions_tmp = {}
    count = 0
    with open('transactions.txt') as transfout:
        for line in transfout:
            count += 1
            if (count % 2) != 0:
                comment_tmp = line[:-1]
            else:
                transactions_tmp[comment_tmp] = int(line[:-1])
    return transactions_tmp


# Writing Transaction dictionary in to file
def transactionfout(trans):
    with open('transactions.txt', "w") as tranfout:
        for comment2, amount2 in trans.items():
            if amount2 > 0:
                tranfout.write(comment2 + '\n')
                tranfout.write(str(amount2) + '\n')


# Starting cycle of programs
print("\n******************************************")
print("Welcome to the console banking application")
print("Version 4.0_beta")
print("******************************************\n")

print("Hi! Friend!\nRestore data from file?")
choice = "N"
if __name__ == "__main__":
    choice = input("Y / N: ")
if choice == "Y" or choice == "y":
    count = 0
    login = input("Your login: ")
    passwd = input("Your password: ")
    if check_login_and_passw(login, passwd):
        client_restored = client_from_file()
        transactions = transaction_from_file()
        print("Your data are restored!\n")
    else:
        client_restored = ("", "", 0, "", 0, 0)
        transactions = {}
        print("Your data isn`t restored!\n")
else:
    client_restored = ("", "", 0, "", 0, 0)
    transactions = {}
    print("Your data isn`t restored!\n")
while True:
    print("What would you like to do?")
    print("1. Create a bank account")
    print("2. Put money into the account")
    print("3. Withdraw money")
    print("4. Display")
    print("5. Expected transactions")
    print("6. Account limit setting")
    print("7. Apply transactions")
    print("8. Statistic of expected transactions")
    print("9. Filtering of expected transactions")
    print("10. Postponed payment")
    print("11. Exit\n")
    if __name__ == "__main__":
        choice = int(input("Enter your choice: "))

    # Bank account creation
    if choice == 1:
        account_creation()

    # Money addition
    elif choice == 2:
        if check_log(input("Your login: ")):
            bill_in = 0
            try:
                # if __name__ == "__main__":
                bill_in = int(input("How much money do you want to deposit into your account: "))
            except ValueError:
                print("Please enter a number")
            money = moneyadd(client_from_file()[5], bill_in, client_from_file()[4])
            clientfout(client_from_file()[0], client_from_file()[1], client_from_file()[2], client_from_file()[3],
                       client_from_file()[4], money)

    # Money withdraw
    elif choice == 3:
        withdraw_bill = 0
        if check_log(input("Your login: ")):
            if pass_check(input("Enter your password: "), client_from_file()[3]):
                withdraw_bill = 0
                try:
                    withdraw_bill = int(input("How much money do you want to withdraw from your account: "))
                except ValueError:
                    print("Please enter a number")

            clientfout(client_from_file()[0], client_from_file()[1], client_from_file()[2], client_from_file()[3],
                       client_from_file()[4], money_withdr(client_from_file()[5], withdraw_bill))

    # Display balance
    elif choice == 4:
        login = input("Your login: ")
        passwd = input("Your password: ")
        if check_login_and_passw(login, passwd):
            print("Your current balance is: " + str(client_from_file()[5]) + "\n")

    # Expected transactions
    elif choice == 5:
        if check_log(input("Your login: ")):
            transaction_money = int(input("How much money do you want to get: "))
            transaction_comment = input("Comments for this transaction: ")
            current_date = datetime.datetime.now()
            current_date.strftime('%m/%d/%y %H:%M:%S')
            transactions[transaction_comment + " (" + current_date.strftime('%m/%d/%y %H:%M:%S') + ")"] \
                = transaction_money
            print("\nYour expected transactions is successfully added!\nin transaction list")
            print("You have a " + str(len(transactions)) + " transactions\n")
            transactionfout(transactions)

    # Account limit setting
    elif choice == 6:
        if check_log(input("Your login: ")):
            account_limit = int(input("Enter maximum balance of money,\nthat can be stored in your account?: "))
            print("Please enter a number")
            clientfout(client_from_file()[0], client_from_file()[1], client_from_file()[2], client_from_file()[3],
                       account_limit, client_from_file()[5])
            print("Your maximum balance of money is " + str(account_limit) + "!\n")

    # Apply transactions
    elif choice == 7:
        if check_log(input("Your login: ")):
            clientfout(client_from_file()[0], client_from_file()[1], client_from_file()[2], client_from_file()[3],
                       client_from_file()[4], apply_trans(client_from_file()[5], client_from_file()[4], transactions))

    # Statistics on expected transactions
    elif choice == 8:
        if check_log(input("Your login: ")):
            amounts = {}
            for comment, amount in transactions.items():
                if amount not in amounts and amount > 0:
                    amounts[amount] = 1
                elif amount > 0:
                    amounts[amount] += 1
            print("Expected:")
            for amount, freq in amounts.items():
                print(str(amount) + " eur: " + str(freq) + " transactions")
            print("\n")

    # Filtering of expected transactions
    elif choice == 9:
        trans_filter = 0
        if check_log(input("Your login: ")):
            try:
                trans_filter = int(input("Please, enter a lower filter\n"
                                         "for transactions summ: "))
            except ValueError:
                print("Please enter a number")
            trans_filtering_logics(transactions, trans_filter)

    # postponed payment
    elif choice == 10:
        login = input("Your login: ")
        if check_log(login):
            log_rec = input("Please enter the recipient's login: ")
            if check_log(log_rec):
                try:
                    summ = int(input("Please enter the summ of money: "))
                    postponed_to_file(login, log_rec, str(summ))
                except ValueError:
                    print("Please enter a valid number")

    # Exit
    elif choice == 11:
        print("Thanks, goodbye!")
        break

    # Other operation numbers
    else:
        print("Wrong operation number, please try again!" + "\n")
        # break
