Merge Pdfs
---

A python module to merge a bunch of Pdf files.

---
### Why would you want to merge bunch of pdf files?

A few months ago now, I purchased this mobile scanner .
[The IRIScan Anywhere](http://www.irislink.com/EN-FR/c1486/IRIScan-Anywhere-5---IRIScan-Anywhere-5-Wifi---Cordless-Scanner.aspx=) scanner.

![IRIScan Anywhere 5](/READMEImages/iriscanWebsitePhoto.png)

This scanner is very portable and I am using it very often to scan all sort of documents I am receiving over mail and that I want to archive to be sure that I have a digital copy.

It is also useful to scan and store the receipt I receive from stores.

###### but

The scanner can't merge files during scanning. It must be done on post-processing through their software.

That's why I wanted to **automate** the process a little.

---


### 1. Prepare your files.

Let's consider that you scan (or have by any other method) a lot of different pdf files.

You need to rename your files according to the following pattern : 

> "_file name1 - part1.pdf_"
>
> ...
>
> "_file name1 - partN.pdf_"
>
> "_file name2 - part1.pdf_"
>
> ...
>
> "_file name2 - partN.pdf_"


See a folder that is properly prepared on the image below :

![Scanned Images Folder](/READMEImages/scannedFilesToMerge.png)

>The files that have the same name ("_file name1_" for instance) are going to be merged together.


### 2. Installation of the required softwares.

As a start, you need to install the PyPDF2 python module to your computer as it is necessary to manipulate the pdf files.

`pip install PyPDF2`


### 3. Call the module

You could then call the module like this, when you are in the folder that has the "_mergepdfs.py_" file : 

`mergepdfs.py ./path/to/the/pdf/files/I/want/to/merge `

I use powershell to do this on Windows :

![](/READMEImages/commandToLaunch.png)

and you can see that the files were merged properly.

![](/READMEImages/commandResult.png)


### 4. Enjoy the results

A "result" directory is created to store the merged files.

Then the files are named as were their parts and available in the "result" folder.

![](/READMEImages/scannedFilesMerged.png)

<br><br>

---
<center>
Released under the <a href="LICENSE.md">Mozilla Public License, version 2.0</a><br>
Made with  :heart:  in Paris :fr:
</center>