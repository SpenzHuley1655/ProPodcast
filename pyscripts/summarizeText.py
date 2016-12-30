# 11/4/16 Spencer Hurley

# Module handles the summarization of text blocks
# The data flow concept is as follows:
# module should accept a text block that has been parsed from the podcast .mp3
# And output a summary of the text block

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from sumy.summarizers.lsa import LsaSummarizer as Summarizer

LANGUAGE = "english"

# str->
# print to console a summary of the document
def main(docname):
    smry = get_summary(docname)
    print smry
    return

# string Number-> string
# extract a Number sentence summary of a .txt document
# parameter docname is the name of the .txt file to summarize
def get_summary(docname, numsentences=7):
    parser = PlaintextParser.from_file(docname, Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)
    summarizer = Summarizer(stemmer)
    final_summary = write_summary(parser, summarizer)
    return final_summary

# parser summarizer Number -> String
# write summary of a file to a string
def write_summary(parser, summarizer, num_sentences=7):
    summary = []
    for sentence in summarizer(parser.document, num_sentences):
        summary.append(str(sentence))
        summary.append("\n")
    final = ''.join(summary)
    return final

if __name__ == '__main__':
    main('document.txt')
