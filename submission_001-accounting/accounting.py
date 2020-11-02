import sys
import user.authentication
import transactions.journal
import banking

# from user.authentication import authenticate_user
# from transactions.journal import receive_income
# from transactions.journal import pay_expense
# from banking.reconciliation import do_reconciliation
# from banking.fvb.reconciliation import do_reconciliation
# from banking.ubsa.reconciliation import do_reconciliation
# from banking.online.reconciliation import do_reconciliation


if __name__ == "__main__":

    if len(sys.argv) > 1:
        # help("modules")
        for i in range(1, len(sys. argv)):
            print(sys.argv[i])

    user.authentication.authenticate_user()
    transactions.journal.receive_income(100)
    transactions.journal.pay_expense(100)
    banking.do_reconciliation()

    # banking.reconciliation.do_reconciliation()
    # banking.fvb.reconciliation.do_reconciliation()
    # banking.ubsa.reconciliation.do_reconciliation()
    # banking.online.reconciliation.do_reconciliation()