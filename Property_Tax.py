# Function to get the assment value of the property
def assess_value(base_value):
    assessed_value = base_value * 0.6
    calc_tax(assessed_value)

# Divide assessed value by 100, then multiply by .72 to get the final tax amount.
def calc_tax(assessed_value):
    tax = (assessed_value / 100) * .72
    print('Your tax is $', format(tax, ',.2f'), sep='')


# Main function will get base property value and pass to assess_value
def main():
    base_value = base_value = float(input('What is the base value of your property? $'))
    assess_value(base_value)


main()
