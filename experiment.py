# file = open(f"invoice/{currentDatetime}.txt", 'w')
# invoiceNumber = int(currentDatetime.split('-')[-1]) * 3000
# file.write(
#     f"{'='*85}\n"
#     f"|{'INVOICE/BILL':^83}|\n"
#     f"{'='*85}\n"
#     f"{'|':<3}{'Invoice no : ' + str(invoiceNumber):<81}|\n"
#     f"{'|':<3}{'Customer Name : ' + 'Shiridhar Khatri':<81}|\n"
#     f"{'|':<3}{'Customer Address : ' + 'Rambazar':<81}|\n"
#     f"{'|':<3}{'Purchase Date : ' + str(datetime.datetime.now().strftime("%Y-%m")):<81}|\n"
#     f"{'='*85}\n"
#     f"|{'ID':^19}|{'ITEM':^19}|{'QUANTITY':^19}|{'PRICE':^23}|\n"
#     f"{'-'*85}\n"
#     f"|{'ID':^19}|{'ITEM':^19}|{'QUANTITY':^19}|{'PRICE':^23}|\n"
#     f"{'='*85}\n"
#     f"{'|':<3}{'Sub Total : ' + '345':<81}|\n"
#     f"{'|':<3}{'Shipping Cost : ' + '345':<81}|\n"
#     f"{'|':<3}{'Tax/Vat : ' + '345':<81}|\n"
#     f"{'|':<3}{'Total Price : ' + '345':<81}|\n"
#     f"{'='*85}"
# )
# file.close()