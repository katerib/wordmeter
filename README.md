# WordMeter

A web-based tool designed to analyze writing patterns by identifying the frequency of unique words and phrases, offering deeper insights into textual styles without common stop words.

## Project Inspiration & Development Goals

During my CS post-bacc, I developed a series of book/reading-related projects during my personal time. One of these, a small command-line program I named [INKCTR](https://github.com/katerib/inkCTR), was a very bare-bones command-line program that analyzes a user-specified PDF to determine the most used words in that PDF. The program allowed the user to modify the 'ignored words' list to add names, places, etc., but other than that the code very literally counted every word in the PDF.

I wanted to improve the program by improving the:

- User experience: a CLI program is very straight forward, but not user-friendly for non-techy users. Develop a simple web app for users.
- File input method: PDFs are a common format, but allow the user to also upload a txt file, csv, or actual text input.
- Analysis method: incorporate natural language processing to perform a deeper anaylsis on present words and develop the ability to identify common phrases as well. Maintain the ability for the user to modify the 'ignored words' list.
- Long-term storage of stored results: have a way to output the results in a way that will be easy for the user to access again. 
- Results analysis: analyze the counted words - are they all common phrases that might be difficult to replace? Are they unique to the story and truly overused? 

**Goals:** In addition to the actual project requirements, I want to use this as a learning experience to begin familiarizing myself with NLP concepts, tools, and libraries.