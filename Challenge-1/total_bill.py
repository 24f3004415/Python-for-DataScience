bill_amount = int(input("Enter the bill amount: "))

if bill_amount>5000:
    discount = bill_amount*0.25
    final_bill = bill_amount-discount   
    print("Your bill after discount is", final_bill)

elif bill_amount>3000 and bill_amount<=5000:
    discount = bill_amount*0.15
    final_bill = bill_amount-discount   
    print("Your bill after discount is", final_bill)

elif bill_amount>1000 and bill_amount<=3000:
    discount = bill_amount*0.10
    final_bill = bill_amount-discount   
    print("Your bill after discount is", final_bill)

else:
    print("sorry!! No discount available")