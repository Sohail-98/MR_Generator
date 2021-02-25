#relevant module
from mrz.generator.mrvb import MRVBCodeGenerator

#inputs for the generators
document_type = "VC"
country_code = input('Enter 3 letters code or country name :').upper()
surname = input('Enter your surname : ').upper()
given_names = input('Enter your first name : ').upper()
document_number = input('Enter your document number (only 8 char): ').upper()
nationality = input('Enter your Nationality : ').upper()
birth_date = input('Enter your D.O.B (yymmdd) : ').upper()
sex = input('Enter your sex (M/F) : ').upper()
expiry_date = input('Enter expiry date (yymmdd) : ').upper()
esbd = input('Enter empty string by deafult(max 8 char): ')
   
#code generator
code = MRVBCodeGenerator(document_type,country_code,given_names,surname,document_number,nationality,birth_date,sex,expiry_date,esbd)


print(code)
