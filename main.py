def main():
   ##################################################
   # Comlete your code here
   ##################################################

    pass


RP = int(input('Regular Price: '))
RT = int(input('Rate: '))
print('Regular Price:  $', format(RP, '.0f'))
print('Discount Amout: $', format(RP*RT/100, '.0f'))
print('The final price:$', format(RP-RP*RT/100, '.0f'))


if __name__ == '__main__':
    main()
