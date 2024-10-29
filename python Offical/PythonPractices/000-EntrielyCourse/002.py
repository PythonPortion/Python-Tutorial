principal = 500000
rate = 0.05
payment = 2684.11
total_paid = 0.0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

start_month = 1

while principal > 0:

    tmp = payment
    # if start_month <= 12:
    #     tmp = payment + extra_payment

    if start_month >= extra_payment_start_month and start_month <= extra_payment_end_month:
        tmp = payment + extra_payment

    principal = principal * (1 + rate / 12) - tmp
    total_paid += tmp

    start_month += 1


print("Payment: ", total_paid) ## Payment:  929965.6199999959
