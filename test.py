#!/usr/bin/env python
import sys
import nltk

from nltk.corpus import wordnet as wn

magician = wn.synsets('magician')[0]
hare = wn.synsets('hare')[0]
hair = wn.synsets('hair')[0]
print "Magician and Hare: " + str(magician.wup_similarity(hare))
print "Magician and Hair: " + str(magician.wup_similarity(hair))
