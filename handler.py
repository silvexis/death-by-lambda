# -*- coding: utf-8 -*-
# Copyright (c) CloudZero, Inc. All rights reserved.
# Licensed under the MIT License. See LICENSE file in the project root for full license information.
#
# DANGER DANGER DANGER DANGER DANGER DANGER DANGER DANGER DANGER DANGER DANGER DANGER DANGER DANGER
# This code includes examples of what _NOT_ to do. You should never use this code, ever.
#
# Also note, all comments below this one have the sarcasm bit set to TRUE
#

import urllib.request
import os
import base64


def hello(event, context):
    """
    This is my awesome hello world function that encrypts text! It's like my first web site, only in Lambda.

    Maybe I can add a hit counter later? What about <blink>?

    Args:
        event:
        context:

    Returns:

    """
    # General run of the mill dangerous, but it will be ok right?
    stuff = event['query'].get('stuff', "")
    url = event['query'].get('url')
    eval_stuff = event['query'].get('eval', "")
    my_secret = os.environ.get('my_secret', "default_secret")

    print("processing a request, using super secret code: {}".format(my_secret))

    # You wanna do what?! Dangerous.
    if url:
        with urllib.request.urlopen(url) as response:
            extra_stuff = response.read()
    else:
        extra_stuff = ""

    # OK Like WTF?! Are you suicidal? level of danger.
    if eval_stuff.lower() == "yes":
        eval_result = "<pre>{}</pre><hr/>".format(eval(stuff))  # Seriously crazy dangerous!
    else:
        eval_result = ""

    body = """
    <html>
    <header><title>Hello World!</title></header>
    <body>
        Encrypted stuff: {}
        <hr/>
            {}<br/>
            Some random URL's Content:<br/>{}
        <hr/>
    </body>
    </html>
    """.format(encrypt(stuff, my_secret), eval_result, extra_stuff)

    return body


def encrypt(clear, key):
    """
    Super bad ass encryption routine I got from my cousin, he says it's legit.
    He said it was called a Vigenere cipher, how cool sounding is that? Gotta be awesome right?
    Args:
        key:
        clear:

    Returns:

    """
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()
