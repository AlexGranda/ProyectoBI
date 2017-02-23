#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import unicodedata


def elimina_tildes(cadena):
    	s = ''.join((c for c in unicodedata.normalize('NFD',unicode(cadena)) if unicodedata.category(c) != 'Mn'))
	return s.decode()

cadena1=argv[1].decode('utf-8')

cadena= elimina_tildes(cadena1)


url = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
url2= '(www\.)(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
emoticons= "['\&\-\.\/()=:;]+"


patron = re.compile('#|@|'+url+'|'+url2+'|'+emoticons)

cadena=patron.sub('',cadena)

#cadena1= cadena.replace(patron,"")
print cadena

