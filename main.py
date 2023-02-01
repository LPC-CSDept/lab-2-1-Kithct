def main():
   ##################################################
   # Comlete your code here
   ##################################################

    pass


RP = int(input('Regular Price: '))
RT = int(input('Rate: '))
print('Regular Price: $', RP)
print('Discount Amout: $', RP*RT/100)
print('The final price: $', RP-RP*RT/100)


if __name__ == '__main__':
    main()
