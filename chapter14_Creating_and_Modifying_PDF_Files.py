from Common import _section_str as sec, _segment_str as seg, _segment_str as sysout
from PyPDF2 import PdfFileReader
from pathlib import Path

print(f"""{sec}
Chapter 14 Creating and Modifying PDF Files
{sec}

""")


print(f"""
{sec}
14.1 Extract Text From a PDF
{sec}

In this section, you’ll learn how to read a PDF file and extract the text
using the PyPDF2 package.
""")

print(r"""
Administrator@MYE420 /cygdrive/e/pythonProject/PythonTutorials
$ pip install PyPDF2
Collecting PyPDF2
  Downloading PyPDF2-1.26.0.tar.gz (77 kB)
     |████████████████████████████████| 77 kB 153 kB/s
  Preparing metadata (setup.py) ... done
Using legacy 'setup.py install' for PyPDF2, since package 'wheel' is not installed.
Installing collected packages: PyPDF2
    Running setup.py install for PyPDF2 ... done
Successfully installed PyPDF2-1.26.0


Administrator@MYE420 /cygdrive/e/pythonProject/PythonTutorials
$ pip list
Package                           Version
--------------------------------- ----------
backports.entry-points-selectable 1.1.1
certifi                           2021.10.8
cycler                            0.11.0
distlib                           0.3.4
filelock                          3.4.0
fonttools                         4.28.4
Jinja2                            3.0.3
joblib                            1.1.0
kiwisolver                        1.3.2
MarkupSafe                        2.0.1
matplotlib                        3.5.1
numpy                             1.21.4
packaging                         21.3
pandas                            1.3.5
Pillow                            8.4.0
pip                               21.3.1
pipenv                            2021.11.23
platformdirs                      2.4.0
pyparsing                         3.0.6
PyPDF2                            1.26.0
python-dateutil                   2.8.2
pytz                              2021.3
pyxlsb                            1.0.9
scikit-learn                      1.0.1
scipy                             1.7.3
setuptools                        57.4.0
six                               1.16.0
threadpoolctl                     3.0.0
virtualenv                        20.10.0
virtualenv-clone                  0.5.7
xgboost                           1.5.1

Administrator@MYE420 /cygdrive/e/pythonProject/PythonTutorials
$ pip show PyPDF2
Name: PyPDF2
Version: 1.26.0
Summary: PDF toolkit
Home-page: http://mstamy2.github.com/PyPDF2
Author: Mathieu Fenniak
Author-email: biziqe@mathieu.fenniak.net
License: UNKNOWN
Location: d:\program files\python39\lib\site-packages
Requires:
Required-by:

""")


print(f"""{seg}
Open a PDF File
{seg}

after installing PyPDF2 package, check what are in there
""")

print(r"""
>>> dir(PyPDF2)
['PageRange', 'PdfFileMerger', 'PdfFileReader', 'PdfFileWriter',
'__all__', '__builtins__', '__cached__', '__doc__', '__file__',
'__loader__', '__name__', '__package__', '__path__', '__spec__',
'__version__', '_version', 'filters', 'generic', 'merger', 'pagerange',
'parse_filename_page_ranges', 'pdf', 'utils']

>>> dir(PdfFileReader)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
'__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
'__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
'__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
'__str__', '__subclasshook__', '__weakref__', '_authenticateUserPassword',
'_buildDestination', '_buildField', '_buildOutline', '_checkKids',
'_decrypt', '_decryptObject', '_flatten', '_getObjectFromStream',
'_getPageNumberByIndirect', '_pairs', '_writeField', '_zeroXref',
'cacheGetIndirectObject', 'cacheIndirectObject', 'decrypt', 'documentInfo',
'getDestinationPageNumber', 'getDocumentInfo', 'getFields',
'getFormTextFields', 'getIsEncrypted', 'getNamedDestinations',
'getNumPages', 'getObject', 'getOutlines', 'getPage', 'getPageLayout',
'getPageMode', 'getPageNumber', 'getXmpMetadata', 'isEncrypted',
'namedDestinations', 'numPages', 'outlines', 'pageLayout', 'pageMode',
'pages', 'read', 'readNextEndLine', 'readObjectHeader', 'xmpMetadata']

>>> dir(pdf_reader.documentInfo)
['__class__', '__class_getitem__', '__contains__', '__delattr__',
'__delitem__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__',
'__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__',
'__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__',
'__module__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__',
'__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__',
'__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'author',
'author_raw', 'clear', 'copy', 'creator', 'creator_raw', 'fromkeys',
'get', 'getObject', 'getText', 'getXmpMetadata', 'items', 'keys', 'pop',
'popitem', 'producer', 'producer_raw', 'raw_get', 'readFromStream',
'setdefault', 'subject', 'subject_raw', 'title', 'title_raw', 'update',
'values', 'writeToStream', 'xmpMetadata']
""")


pdf_file = Path(Path.cwd()/"chapter14_Exercise"/"Pride_and_Prejudice.pdf")

with pdf_file.open(mode="rb") as file:
    pdf_reader = PdfFileReader(file)
    print(f"pdf_reader.getNumPages() is {pdf_reader.getNumPages()}")
    print(f"pdf_reader.documentInfo is {pdf_reader.documentInfo}")
    print(f"pdf_reader.documentInfo.title is {pdf_reader.documentInfo.title}")
    print(pdf_reader.documentInfo.keys())
    print(type(pdf_reader.getPage(4).getContents()))
    print(f"pdf_reader.getPage(4).getContents() is {pdf_reader.getPage(4).getContents()}")
    print(f"pdf_reader.getPage(4).getContents().keys() is {pdf_reader.getPage(4).getContents().keys()}")
    print(f"pdf_reader.getPage(4).getContents()['/Filter'] is {pdf_reader.getPage(4).getContents()['/Filter']}")
    print(f"pdf_reader.documentInfo.getText('/Author') is {pdf_reader.documentInfo.getText('/Author')}")
    print(f"pdf_reader.getDocumentInfo() is {pdf_reader.getDocumentInfo()}")


print(f"""
{seg}
Extract Text From a Page
{seg}
""")

print(r"""
>>> dir(pdf_reader.getPage(10))
['__class__', '__class_getitem__', '__contains__', '__delattr__',
'__delitem__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__',
'__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__',
'__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__',
'__module__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__',
'__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__',
'__sizeof__', '__str__', '__subclasshook__', '__weakref__',
'_addTransformationMatrix', '_contentStreamRename', '_mergePage',
'_mergeResources', '_pushPopGS', '_rotate', 'addTransformation', 'artBox',
'bleedBox', 'clear', 'compressContentStreams', 'copy', 'createBlankPage',
'cropBox', 'extractText', 'fromkeys', 'get', 'getContents', 'getObject',
'getXmpMetadata', 'indirectRef', 'items', 'keys', 'mediaBox', 'mergePage',
'mergeRotatedPage', 'mergeRotatedScaledPage',
'mergeRotatedScaledTranslatedPage', 'mergeRotatedTranslatedPage',
'mergeScaledPage', 'mergeScaledTranslatedPage', 'mergeTransformedPage',
'mergeTranslatedPage', 'pdf', 'pop', 'popitem', 'raw_get', 'readFromStream',
'rotateClockwise', 'rotateCounterClockwise', 'scale', 'scaleBy', 'scaleTo',
'setdefault', 'trimBox', 'update', 'values', 'writeToStream', 'xmpMetadata']
""")

cnt_of_pages = 0
with pdf_file.open(mode="rb") as file:
    pdf_reader = PdfFileReader(file)
    page_10 = pdf_reader.getPage(10).extractText()
    print(page_10)

    for page in pdf_reader.pages:
        #print(type(page.extractText()))
        cnt_of_pages +=1
print(cnt_of_pages)
