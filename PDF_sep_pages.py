import PyPDF2
import os
import sys
  
def PDFsplit(pdf, start, end):

    # check if the file exists
    exists = os.path.isfile(pdf)
    if not exists:
        return [1,'The selected file does not exist. Please chosse an existing file.']

    # creating input pdf file object
    pdfFileObj = open(pdf, 'rb')
    
    # creating pdf reader object 
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 

    # output pdf file name
    pages = pdfReader.numPages
    if end > pages:
        return [2,'The pdf document has less than ' + str(end) + ' pages. Please choose a lower number for the end page. Max: ' + str(pages)]

    if end < start:
        return [3,'The number of the end page is below the start page. This seems stupid.']

    # Define the name of the output-file
    if end > start:
        outputpdf = pdf.split('.pdf')[0] + '_p' + str(start) + '_to_' + str(end) + '.pdf'
    else:
        outputpdf = pdf.split('.pdf')[0] + '_p' + str(start) + '.pdf'
      
    # creating pdf writer object for (i+1)th split 
    pdfWriter = PyPDF2.PdfFileWriter() 

    # adding pages to pdf writer object 
    for page in range(start-1,end): 
        pdfWriter.addPage(pdfReader.getPage(page)) 
      
    # writing split pdf pages to pdf file 
    with open(outputpdf, "wb") as f: 
        pdfWriter.write(f) 
          
    # closing the input pdf file object 
    pdfFileObj.close()

    return [0,'The file ' + outputpdf + ' was generated successfully!']

              
def main():

    print('')
    if len(sys.argv) == 1:
        print('No file for extracting pages selected...')
        print('An extra argument containing the file-path is mandatory.')
        return 0
    elif len(sys.argv) == 2:
        pdf = sys.argv[1]
        start_page = 1
        end_page = 1
        print('Arguments for start and end page missing...')
        print('Trying to extract the first page')
    elif len(sys.argv) == 3:
        pdf = sys.argv[1]
        start_page = int(sys.argv[2])
        end_page = start_page
        print('Arguments for end page missing...')
        print('Trying to extract the ' + str(start_page) + '. page')
    elif len(sys.argv) == 4:
        pdf = sys.argv[1]
        start_page = int(sys.argv[2])
        end_page = int(sys.argv[3])
    else:
        print('Too many input arguments...')
        print('Typical arguments:')
        print('- path of the original file')
        print('- page number of the first page to extract')
        print('- page number of the last page to extract')

    
    # calling PDFsplit function to split pdf 
    err_msg = PDFsplit(pdf, start_page, end_page)
    
    # Print the error messages
    print(err_msg[1])


  
if __name__ == "__main__": 
    # calling the main function 
    main() 
