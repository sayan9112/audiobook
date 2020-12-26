import pyttsx3
import PyPDF2
book = open('the pdf we want the code will read out.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

speaker = pyttsx3.init()
for num in range(8, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
    

#author: Sayan Mukherjee (kalbhairab)
#mail: almighty.kalbhairab@gmail.com
#linkedIn: https://www.linkedin.com/in/sayan-mukherjee-7845421a7/
#github: github.com/sayan9112 (Personal Website)    
            
 
