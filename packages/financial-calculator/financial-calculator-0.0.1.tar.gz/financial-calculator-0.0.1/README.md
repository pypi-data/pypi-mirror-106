# Financial Calculator

## 1. EMI Calculator: It takes in 3 mandatory arguments along with 2 optional arguments.
#### amount: the total loan amount
#### tenure: duration of the loan in years. It can also be specified in months, but we need to then pass the optional parameter  "is_year=False"
#### interest: the rate of interest (ROI) per annum. This is specified in per cent. It can also be specified as a decimal value, but we need to then pass the optional parameter "is_percent=False"
#### and returns the EMI amount

## 2. SIP Calculator: it takes in 3 mandatory arguments along with 3 optional arguments.
#### investment: monthly investment amount
#### tenure: duration of the loan in years. It can also be specified in months, but we need to then pass the optional parameter "is_year=False"
#### interest: expected investment return per annum. It is specified in terms of per cent. It can also be specified as a decimal value, but we need to then pass the optional parameter "is_percent=False"
#### amount: the initial amount for the investment. by default, it is set to 0
#### show_amount_list: if true, the output will include a detailed growth list
#### and returns the maturity amount of the SIP 