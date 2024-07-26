import datetime
currentDatetime = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")
def readFurniture():
    try:
        file = open('furniture.txt', 'r')
        furniture = file.readlines()
        file.close()
    except:
        print("\n📁 File not found named furniture.txt")
    data = []
    for elems in furniture:
        furnitureData = elems.strip("\n").split(',')
        data.append({
            'id': furnitureData[0],
            'company': furnitureData[1],
            'name': furnitureData[2],
            'qty': int(furnitureData[3]), 
            'price': float(furnitureData[4]) 
        })
    return data

def displayFurniture(furnitureData):
    print(f"\n{'~'*91}\n|{'ID':^5}|{'MANUFACTURER':^35}|{'ITEMS':^15}|{'QUANTITY':^14}|{'PRICE/QTY':^15} |\n{'~'*91}")
    for elems in furnitureData:
        print(f"|{elems['id']:^5}|{elems['company']:^35}|{elems['name']:^15}|{elems['qty']:^14}|{'$ '+str(elems['price']):^15} |")
    print(f"{'~'*91}\n")

def writeFile(fileData, furnitureData,filePath, person):
    isAddingInvoiceRunning = True
    while isAddingInvoiceRunning:
        while True:
            try:
                nameOfCostumer = input("Enter your name >> ")
                if len(nameOfCostumer) <=1:
                    print("❌ Please enter your valid name  ")
                else:
                    break
            except:
                print("Error reading name")
                continue
        while True:
            try:
                addressOfCostumer = input("Enter your address >> ")
                if len(addressOfCostumer) <=1:
                    print("❌ Please enter your valid address ")
                else:
                    break
            except:
                print("Error reading name")
                continue
        subTotal = 0
        for elems in fileData:  
            subTotal+= float(elems['price'] * elems['qty'])
        vatAmt = subTotal * 13/100
        while True:   
            shippingCostInp = input("Do you want to add shipping cost (yes/y or no/n)>> ")
            shippingCost = 0
            if shippingCostInp.upper() == "YES" or shippingCostInp.upper() == "Y" :
                if subTotal+vatAmt > 1000 and subTotal+vatAmt < 3000:
                    shippingCost = 150
                elif subTotal+vatAmt > 3000:
                    shippingCost = 300
                else:
                    shippingCost = 50
                break
            elif shippingCostInp.upper() == "NO" or shippingCostInp.upper() == "N":
                shippingCost = 0
                break
            else:
                print("Please type valid answer")
        file = open(f"invoice/{filePath}/{currentDatetime}.txt", 'w')
        invoiceNumber = int(currentDatetime.split('-')[-1]) * 3000
        file.write(
        f"{'='*85}\n"
        f"|{filePath.upper()+'/INVOICE':^83}|\n"
        f"{'='*85}\n"
        f"{'|':<3}{'Invoice no : ' + str(invoiceNumber):<81}|\n"
        f"{'|':<3}{person+' Name : ' + nameOfCostumer.title():<81}|\n"
        f"{'|':<3}{person+' Address : ' + addressOfCostumer.title():<81}|\n"
        f"{'|':<3}{'Purchase Date : ' + str(datetime.datetime.now().strftime("%Y-%m-%d")):<81}|\n"
        f"{'='*85}\n"
        f"|{'ID':^5}|{'Company':^30}|{'ITEM':^19}|{'QUANTITY':^12}|{'PRICE':^13}|\n"
        f"{'-'*85}\n")
        for elems in fileData:
            file.write(
                f"|{elems['id']:^5}|{elems['company']:^30}|{elems['name']:^19}|{elems['qty']:^12}|{'$ '+str(elems['price']):^13}|\n"
            )         
        file.write(
        f"{'='*85}\n"
        f"{'|':<3}{'Sub Total : $' + str(subTotal):<81}|\n"
        f"{'|':<3}{'Shipping Cost : $' + str(shippingCost):<81}|\n"
        f"{'|':<3}{'Tax/Vat(13%) : $' + str(vatAmt):<81}|\n"
        f"{'|':<3}{'Total Price : $' + str(subTotal+vatAmt+shippingCost):<81}|\n"
        f"{'='*85}"
        )
        file.close()
        print(
        f"\n"
        f"{'='*85}\n"
        f"|{filePath.upper()+'/INVOICE':^83}|\n"
        f"{'='*85}\n"
        f"{'|':<3}{'Invoice no : ' + str(invoiceNumber):<81}|\n"
        f"{'|':<3}{person+' Name : ' + nameOfCostumer.title():<81}|\n"
        f"{'|':<3}{person+' Address : ' + addressOfCostumer.title():<81}|\n"
        f"{'|':<3}{'Purchase Date : ' + str(datetime.datetime.now().strftime("%Y-%m-%d")):<81}|\n"
        f"{'='*85}\n"
        f"|{'ID':^5}|{'Company':^30}|{'ITEM':^19}|{'QUANTITY':^12}|{'PRICE':^13}|\n"
        f"{'-'*85}")
        for elems in fileData:
            print(
                f"|{elems['id']:^5}|{elems['company']:^30}|{elems['name']:^19}|{elems['qty']:^12}|{'$ '+str(elems['price']):^13}|"
            )         
        print(
        f"{'='*85}\n"
        f"{'|':<3}{'Sub Total : $' + str(subTotal):<81}|\n"
        f"{'|':<3}{'Shipping Cost : $' + str(shippingCost):<81}|\n"
        f"{'|':<3}{'Tax/Vat(13%) : $' + str(vatAmt):<81}|\n"
        f"{'|':<3}{'Total Price : $' + str(subTotal+vatAmt+shippingCost):<81}|\n"
        f"{'='*85}"
        )
        isAddingInvoiceRunning = False
    furnitureFile = open(f"furniture.txt", 'w')
    for elems in furnitureData:
        furnitureFile.write(f"{elems['id']},{elems['company']},{elems['name']},{elems['qty']},{elems['price']}\n")
    furnitureFile.close()
    print(f"\n{'~'*30}\n|{'CHOOSE ONE OPTION':^28}|\n{'~'*30}\n{'|':<2}{'1. Show furniture':<27}|\n{'|':<2}{'2. Purchase furniture':<27}|\n{'|':<2}{'3. Order furniture':<27}|\n{'|':<2}{'4. Exit program':<27}|\n{'~'*30}\n")
    isAddingInvoiceRunning = False
    
def displayCartItem(addedItemList):
    print(f"\n{'='*64}\n|{'ID':^20}|{'ITEM':^20}|{'QUANTITY':^20}|\n{'='*64}")
    for elems in addedItemList:
        print(f"|{elems['id']:^20}|{elems['name']:^20}|{elems['qty']:^20}|") 
    print(f"{'-'*64}")

def addQuantity(cartCollection, furnitureData):
    displayCartItem(cartCollection)
    isQtyAddingProcessRunning = True
    while isQtyAddingProcessRunning:
        try:
            reQtyOption = int(input("Enter the ID of a product from your cart that you want to add >> "))
            isAvailable = False
            for e in cartCollection:
                if int(e['id']) == reQtyOption:
                    while True:
                        prodQty = input("Enter how many quantity you want to add or exit >> ")
                        isAvailable = True
                        if prodQty.upper() == "EXIT":
                            break
                        elif prodQty.isdigit():  
                            prodQty = int(prodQty)
                            if prodQty <= 0:
                                print("\n❌ Please add atleast one quantity!!")
                            elif furnitureData[reQtyOption - 1]['qty'] >= prodQty:
                                e['qty'] += prodQty
                                furnitureData[reQtyOption - 1]['qty'] -= prodQty
                                print(f"\n✅ {prodQty} quantity is added for {e['name']} successfully!!")
                                print(f"\n{'~'*30}\n|{'CHOOSE ONE OPTION':^28}|\n{'~'*30}\n{'|':<2}{'1. Add more quantity':<27}|\n{'|':<2}{'2. Add more items':<27}|\n{'|':<2}{'3. Exit with bill.':<27}|\n{'~'*30}\n")
                                isQtyAddingProcessRunning = False
                                break
                            elif furnitureData[reQtyOption - 1]['qty'] > 0 and prodQty > furnitureData[reQtyOption - 1]['qty']:
                                print(f"\n❌ {prodQty} is not available Only {furnitureData[reQtyOption - 1]['qty']} is available in stock.")
                            else:
                                print("\n❌ This product is out of stock! 🛒")
                                isQtyAddingProcessRunning = False
                                break
                        else:
                            print("\n❌ Please enter a valid quantity")
            if not isAvailable:
                print("\n❌ Please enter the id of a product available in the table above only!")
                continue
        except:
            print("\n⛔ Invalid input! Please enter quantity in numbers only.")                        

def purchaseItems(furnitureData):
    cartCollection = []
    isRunning = True
    displayFurniture(furnitureData)
    while isRunning:
        choice = input("Enter the id of the item you want to purchase or type exit >> ")
        if choice.lower() == "exit":
            print(f"\n{'~'*30}\n|{'CHOOSE ONE OPTION':^28}|\n{'~'*30}\n{'|':<2}{'1. Show furniture':<27}|\n{'|':<2}{'2. Purchase furniture':<27}|\n{'|':<2}{'3. Order furniture':<27}|\n{'|':<2}{'4. Exit program':<27}|\n{'~'*30}\n")
            isRunning = False
        elif choice.isdigit():
            numChoice = int(choice)
            if numChoice > len(furnitureData):
                print(f"\n❌ Sorry ! There is no item with ID {choice}")
            elif numChoice == 0:
                print("\n❌ Sorry ! There is no item with ID 0")
            else:
                choosedItem = furnitureData[numChoice - 1]
                isAddingQtyRunning = True
                while isAddingQtyRunning:
                    try:
                        qty = int(input("Enter how many quantity you want >> ")) 
                        if choosedItem['qty'] == 0:
                            print("❌ This product is out of stock! 🛒")
                            isAddingQtyRunning = False
                        if  choosedItem['qty'] > 0 and qty > choosedItem['qty'] :
                            print(f"\n❌ {qty} Quantity is not available. Only {choosedItem['qty']} is available in stock.")
                        elif qty <= 0:
                            print("❌ Please choose at least one quantity")
                        else:
                            if len(cartCollection) <= 0:
                                cartCollection.append({
                                    "id": choosedItem['id'],
                                    "company":choosedItem['company'],
                                    "name": choosedItem['name'],
                                    "qty": qty,
                                    "price": choosedItem['price']
                                }) 
                                choosedItem['qty'] -= qty
                                print(f"\n✅ {choosedItem['name']} is added to your item list successfully!!")
                            else:
                                isAvailableItem = False
                                for elem in cartCollection:
                                    if int(elem['id']) == numChoice:
                                        isAvailableItem = True                                 
                                        if choosedItem['qty'] >= qty:
                                            elem['qty'] += qty
                                            choosedItem['qty'] -= qty
                                if isAvailableItem == False:
                                    cartCollection.append({
                                        "id": choosedItem['id'],
                                        "company":choosedItem['company'],
                                        "name": choosedItem['name'],
                                        "qty": qty,
                                        "price": choosedItem['price']
                                    }) 
                                    choosedItem['qty'] -= qty
                                    print(f"\n✅ {choosedItem['name']} is added to your item list successfully!!") 
                            isOptionRunning = True
                            print(f"\n{'~'*30}\n|{'CHOOSE ONE OPTION':^28}|\n{'~'*30}\n{'|':<2}{'1. Add more quantity':<27}|\n{'|':<2}{'2. Add more items':<27}|\n{'|':<2}{'3. Exit with bill.':<27}|\n{'~'*30}\n")
                            while isOptionRunning:
                                try:
                                    userNextChoice = int(input("Enter your choice >> "))
                                    if userNextChoice == 1:       
                                        addQuantity(cartCollection, furnitureData)
                                    elif userNextChoice == 2:
                                        displayFurniture(furnitureData)
                                        isAddingQtyRunning = False
                                        isOptionRunning = False
                                        break
                                    elif userNextChoice == 3:
                                        isAddingQtyRunning = False
                                        writeFile(cartCollection, furnitureData, "purchase", 'Costumer')
                                        isRunning  = False
                                        break
                                    else:
                                        print("\n⛔ Invalid Choice! choose 1 to 3 only.")
                                except:
                                    print("\n⛔ Invalid! Please enter number only")
                    except:
                        print("\n⛔ Invalid input! Please enter quantity in number only!!")
        else:
            print(f"\n❌ Please enter valid input or type exit")
            
def orderItems(furnitureData):
    isOrderItemRunning = True
    addedItemList = []
    print(f"\n{'~'*76}\n|{'ID':^5}|{'MANUFACTURER':^35}|{'ITEMS':^15}|{'PRICE/QTY':^15} |\n{'~'*76}")
    for elems in furnitureData:
        print(f"|{elems['id']:^5}|{elems['company']:^35}|{elems['name']:^15}|{'$ '+str(elems['price']):^15} |")
    print(f"{'~'*76}\n")
    while isOrderItemRunning:
            employeeChoice = input("Enter the id of item or type exit >> ")
            if employeeChoice == "exit":
                isOrderItemRunning = False
            elif employeeChoice.isdigit():
                employeeChoice = int(employeeChoice)
                if employeeChoice == 0:
                    print("\n❌ Sorry ! There is no item with ID 0")
                elif employeeChoice > len(furnitureData):
                    print("\n❌ Sorry ! There is no item with ID", employeeChoice)
                else:
                    choosedFurniture = furnitureData[employeeChoice-1]
                    isQtyAddingProcessRunning = True
                    while isQtyAddingProcessRunning:
                        try:
                            quantityInput = int(input("Enter quantity you wanna add >> "))
                            if len(addedItemList) <=0:
                                addedItemList.append({
                                    "id": choosedFurniture["id"],
                                    "company": choosedFurniture["company"],
                                    "name": choosedFurniture["name"],
                                    "qty": quantityInput,
                                    "price": choosedFurniture["price"]
                                })
                                choosedFurniture['qty']+=quantityInput
                                isQtyAddingProcessRunning = False
                                print(f"\n✅ {choosedFurniture['name']} is added to your item list successfully!!") 
                            else:
                                isProductAvailable = False
                                for item in addedItemList:
                                    if int(item["id"]) == employeeChoice:
                                        isProductAvailable = True
                                        item["qty"] += quantityInput
                                        choosedFurniture['qty']+=quantityInput
                                if isProductAvailable == False:
                                    addedItemList.append({
                                    "id": choosedFurniture["id"],
                                    "company": choosedFurniture["company"],
                                    "name": choosedFurniture["name"],
                                    "qty": quantityInput,
                                    "price": choosedFurniture["price"]
                                    })
                                    choosedFurniture['qty']+=quantityInput
                                    print(f"\n✅ {choosedFurniture['name']} is added to your item list successfully!!") 
                            employeeChoiceOptRunning = True
                            print(f"\n{'~'*30}\n|{'CHOOSE ONE OPTION':^28}|\n{'~'*30}\n{'|':<2}{'1. Add more quantity':<27}|\n{'|':<2}{'2. Add more items':<27}|\n{'|':<2}{'3. Exit with bill.':<27}|\n{'~'*30}\n")
                            while employeeChoiceOptRunning:
                                try:
                                    employeeChoiceOpt = int(input("Enter your choice from above >> "))
                                    if employeeChoiceOpt == 1:
                                        displayCartItem(addedItemList)
                                        isChoosingQtyRunning = True
                                        while isChoosingQtyRunning:
                                            try:
                                                itemChoice= int(input("Choose quantity by id >> "))
                                                itemAvailable = False
                                                for elem in addedItemList:
                                                    if int(elem['id']) == itemChoice:
                                                        itemAvailable = True
                                                        while True:
                                                            try:
                                                                reQtyInput = int(input("Enter quantity you wanna add >> "))
                                                                if reQtyInput <=0:
                                                                    print("\n❌ Please enter quantity more then 0")
                                                                else:
                                                                    elem['qty']+=reQtyInput
                                                                    choosedFurniture['qty']+=reQtyInput
                                                                    print(f"\n✅ {reQtyInput} quantity is added for {elem['name']} successfully!!")
                                                                    print(f"\n{'~'*30}\n|{'CHOOSE ONE OPTION':^28}|\n{'~'*30}\n{'|':<2}{'1. Add more quantity':<27}|\n{'|':<2}{'2. Add more items':<27}|\n{'|':<2}{'3. Exit with bill.':<27}|\n{'~'*30}\n")
                                                                    break
                                                            except:
                                                                print("\n⛔ Please enter input in number only!!")
                                                        isChoosingQtyRunning = False      
                                                if itemAvailable == False:
                                                    print(f"\n🆔 {itemChoice} is not available in the above table")
                                            except:
                                                print("\n❌ Invalid input ! Please enter number only !")
                                    elif employeeChoiceOpt == 2:
                                        print(f"\n{'~'*76}\n|{'ID':^5}|{'MANUFACTURER':^35}|{'ITEMS':^15}|{'PRICE/QTY':^15} |\n{'~'*76}")
                                        for elems in furnitureData:
                                            print(f"|{elems['id']:^5}|{elems['company']:^35}|{elems['name']:^15}|{'$ '+str(elems['price']):^15} |")
                                        print(f"{'~'*76}\n")
                                        isQtyAddingProcessRunning = False
                                        employeeChoiceOptRunning = False
                                    elif employeeChoiceOpt == 3:
                                        employeeChoiceOptRunning = False
                                        isQtyAddingProcessRunning = False
                                        writeFile(addedItemList, furnitureData,"order", "Employee") 
                                        isOrderItemRunning = False
                                    else:
                                        print("\n❌ Sorry ! Invalid choice !")
                                except:
                                    print("\n❌ Sorry ! Invalid input !")
                            isQtyAddingProcessRunning = False
                        except:
                            print("\n⛔ Invalid input! Please enter quantity in number only")
            else:
                print("\n⛔ Invalid input! Please enter numbers only or exit.")

def main():
    furnitureData = readFurniture()
    print(f"\n{'~'*30}\n|{'CHOOSE ONE OPTION':^28}|\n{'~'*30}\n{'|':<2}{'1. Show furniture':<27}|\n{'|':<2}{'2. Purchase furniture':<27}|\n{'|':<2}{'3. Order furniture':<27}|\n{'|':<2}{'4. Exit program':<27}|\n{'~'*30}\n")
    while True:
        try:
            choice = int(input("Enter your choice from table >> "))
            if choice == 1:
                furnitureData = readFurniture()
                print(f"\n{'~'*30}\n|{'CHOOSE ONE OPTION':^28}|\n{'~'*30}\n{'|':<2}{'1. Show furniture':<27}|\n{'|':<2}{'2. Purchase furniture':<27}|\n{'|':<2}{'3. Order furniture':<27}|\n{'|':<2}{'4. Exit program':<27}|\n{'~'*30}\n")
                displayFurniture(furnitureData)
            elif choice == 2:
                purchaseItems(furnitureData)
            elif choice == 3:
                orderItems(furnitureData)
            elif choice == 4:
                print("\nThanks for your purchase! We're excited to have you with us! 🌟\n")
                break
            else:
                print("\n⛔ Invalid Choice! choose 1 to 4 only.")
        except:
            print("\n⛔ Invalid input! Please enter numbers only.")
main()