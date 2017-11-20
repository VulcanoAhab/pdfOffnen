from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.layout import LAParams
from io import StringIO

class Read:
    """
    """
    _resourceManager=PDFResourceManager()
    _codec="utf-8"
    _laparams=LAParams()


    def __init__(self, filePath, pages=[]):
        """
        """
        self._fp=filePath
        self._fd=open(filePath, "rb")
        self._pages=PDFPage.get_pages(self._fd, pagenos=pages)
        self._pages_text=[]


    def __del__(self):
        self._fd.close()

    @property
    def text(self):
        """
        """
        if self._pages_text:return self._pages_text
        for page in self._pages:
            #set interpreter per page - multiprocess?
            _fileLike=StringIO()
            _device=TextConverter(self._resourceManager, _fileLike,
                                  codec=self._codec, laparams=self._laparams)
            _interpreter = PDFPageInterpreter(self._resourceManager, _device)
            #mine content
            _interpreter.process_page(page)
            processedText=_fileLike.getvalue()
            self._pages_text.append(processedText)
        return self._pages_text
