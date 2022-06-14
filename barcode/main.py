
#https://github.com/wintun-devop
#https://www.youtube.com/channel/UCz9ebjc-_3t3p49gGpwyAKA (Please subscribe my channel.Thank You!)
import barcode
from barcode.writer import ImageWriter

#we can get supported format for barcode generator
def get_supported_barcode_format():
    supported_barcode_formates=barcode.PROVIDED_BARCODES
    print(supported_barcode_formates)

#To create barcode with desire number and barcode format parameter
def create_barcode(barcodNumber,barcodeFormat):
    number = barcodNumber
    get_format = barcode.get_barcode_class(barcodeFormat)
    format= get_format
    #creating barcode
    barcode_result = format(number, writer=ImageWriter())
    barcode_file_name=number+barcodeFormat+"barcode"
    #save barcode to file
    barcode_result.save(barcode_file_name)    
    
def main():
    #get_supported_barcode_format()
    create_barcode("4901885757543","jan")
    
if __name__ == "__main__":
    main()
